import sys, os
from PySide6.QtWidgets import QWidget,QMainWindow, QApplication,QLabel, QLineEdit,QTextEdit, QGridLayout, QTextBrowser, QTabWidget, QBoxLayout, QPushButton, QDialog, QFormLayout, QMessageBox, QFileDialog, QInputDialog
from PySide6.QtGui import QIcon, QAction, QPainter, QColor, QPixmap,QFont, QPen, QPainterPath, QStandardItemModel, QStandardItem, QGuiApplication
from PySide6.QtCore import Qt,QRect,QPropertyAnimation,QThread,Signal,QObject

import sys, os
from ui_main_window import Ui_MainWindow
from unit_seperator import get_unit, get_unit_scaling, get_unit_value,get_uv_scaled
from gui_add_electronic import DialogAddElectronic
from gui_add_cavity import DialogAddCavity
from gui_add_pulse import DialogAddPulse
from gui_add_chirp import DialogAddChirp
from gui_parse_components import component_parser
from gui_dialog_small import InputDialogSmall
from gui_time_grid_or_tolerance import DialogAddGridOrTolerance
import numpy as np
from parse_ansi import replace_ansi_escape_sequences
from collections import defaultdict
from subprocess import Popen, PIPE, call
from multiprocessing import Process
import re

# todo: alles in funktionen umwälzen die über kontextmenü callbar sind
# save/loading.

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        self.filepath = os.path.dirname(os.path.realpath(__file__))
        # Config
        self.colors = {"Background" : "#DDDDDD", 
        "State" : "#88282A3A",
        "StateName" : "#FFFFFF",
        "Transition" : "#88282A3A",
        "Cavity" : ("#aaf4501e", "#aaf4501e"),
        "Neutral" : "#000000"}
        self.resources = {
            "Icon" : os.path.join(self.filepath,"resources/test.png"),
        }
        self.plot_system_details = False
        # System Components that contribute to the execution string
        self.system_components = defaultdict(lambda: {})
        self.system_components_fields = {}
        # Hoverable Widgets
        self.system_widgets = {}

        # Clipboard
        self.clipboard = QGuiApplication.clipboard()

        # Cache sizes:
        self.fixed_energy_w, self.fixed_energy_h = None, None

        # Add functionality to buttons
        self.connect_functionality()

        # Unfinished Tabs
        for i in [10,11]:
            self.tabWidget.setTabIcon(i, QIcon(self.resources["Icon"]))

        self.show()
        self.connect_config_to_fields()
        self.set_components_from_fields()
        
        path = os.path.dirname(os.path.realpath(__file__))
        self.load_from_qdlc_file(os.path.join(path,"biexction_display.qdlc"))
        self.update_component_list()
        self.drawSystem()

    def save_to_qdlc_file(self, filepath = "settings.qdlc"):
        from pickle import dump, HIGHEST_PROTOCOL
        print(f"Saving to {filepath}")
        self.set_components_from_fields()
        with open(filepath, "wb") as f:
            print(f"Current Dict: {dict(self.system_components)}")
            dump(dict(self.system_components), f, protocol=HIGHEST_PROTOCOL)

    def load_from_qdlc_file(self, filepath = "settings.qdlc"):
        from pickle import load
        print(f"Loading from {filepath}")
        with open(filepath, "rb") as f:
            loaded = load(f)
            self.system_components.update(loaded)
            print(f"Current Dict: {dict(self.system_components)}")
        self.set_fields_from_components()

    def connect_functionality(self):
        # "Next" Buttons
        for button in [self.button_next_tab_system_to_config, self.button_next_tab_config_to_timeline, self.button_next_tab_timeline_to_spectrum, self.button_next_tab_spectrum_to_indist, self.button_next_tab_indist_to_conc, self.button_next_tab_sconc_to_stats, self.button_next_tab_stats_to_detector, self.button_next_tab_detector_to_generate]:
            button.clicked.connect( lambda: self.tabWidget.setCurrentIndex( self.tabWidget.currentIndex() + 1 ) )
        # Add Stuff Dialog
        self.button_add_electronic_state.clicked.connect(lambda: DialogAddElectronic(main_window=self))
        self.button_add_cavity.clicked.connect(lambda: DialogAddCavity(main_window=self))
        self.button_add_optical_pulse.clicked.connect(lambda: DialogAddPulse(main_window=self))
        self.button_add_electronic_shift.clicked.connect(lambda: DialogAddChirp(main_window=self))
        # Modify Stuff
        self.button_modify_clear.clicked.connect(self.clearSystem)
        
        def modify():
            self.plot_system_details = self.input_draw_details.isChecked()
            self.drawSystem()
        self.input_draw_details.clicked.connect(modify)

        def delete_input():
            current = self.list_components.currentIndex().data()
            if current is None or current == "None":
                return
            name, category = current.split(" - ")
            self.system_components[category].pop(name)
            print(f"Dropped {name} from {category}")
            self.drawSystem()
            self.update_component_list()
        self.button_modify_delete.clicked.connect(delete_input)

        def edit_input():
            current = self.list_components.currentIndex().data()
            print(current)
            if current is None or current == "None":
                return
            name, category = current.split(" - ")
            if category == "EnergyLevels":
                DialogAddElectronic(main_window=self, load_existing=name)
            elif category == "CavityLevels":
                DialogAddCavity(main_window=self, load_existing=name)
            elif category == "Pulse":
                DialogAddPulse(main_window=self, load_existing=name)
            elif category == "Chirp":
                DialogAddChirp(main_window=self, load_existing=name)
        self.button_modify_edit.clicked.connect(edit_input)

        # Config Inputs
        self.button_time_config_tol.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Tolerances"))
        self.button_time_config_grid.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Grid"))


        # Loading / Saving
        def export_command():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptSave)
            dlg.setNameFilters(["*.qdlc", "*.log"])

            if dlg.exec():
                filenames = dlg.selectedFiles()
                print(filenames)
                print(f"Exporting to {filenames[0]}")
                self.save_to_qdlc_file(filepath = filenames[0])

        def import_command():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setNameFilters(["*.qdlc", "*.log"])
            if dlg.exec():
                filenames = dlg.selectedFiles()
                self.load_from_qdlc_file(filepath = filenames[0])
                self.drawSystem()
                self.update_component_list()

        # File Path
        def set_file_path():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.Directory)
            if dlg.exec():
                filename = dlg.selectedFiles()[0]
                if not filename.endswith("/"):
                    filename += "/"
                self.textinput_file_destination.setText(filename)
        def set_qdlc_filepath():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setNameFilters(["*.exe", "*.out", "*.*"])
            if dlg.exec():
                filenames = dlg.selectedFiles()
                #path = os.path.relpath(filenames[0], os.getcwd())
                self.textinput_file_qdlc.setText(filenames[0])
        self.input_destination.clicked.connect(set_file_path) 
        self.input_path_to_qdlc.clicked.connect(set_qdlc_filepath) 
        
        # Save Settings
        def set_settingfile_path():
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)
            dlg.setAcceptMode(QFileDialog.AcceptSave)
            dlg.setNameFilters(["*.txt", "*.*"])
            if dlg.exec():
                filename = dlg.selectedFiles()[0]
                self.textinput_path_to_settingfile.setText(filename)
        self.button_set_setting_file_path.clicked.connect(set_settingfile_path)
        
        def save_to_setting_file(filepath, project_name):

            class SettingfileWorker(QObject):
                finished = Signal()
                progress = Signal(float)
                text = Signal(str)
                def __init__(self, parent = None):
                    super().__init__()
                    self.parent = parent
                def run(self):
                    with open(filepath, "w") as f:
                        f.write(f"# {project_name}\n")
                        self.text.emit(f"# {project_name}")
                        if self.parent.checkbox_activate_scan_parameter_1.isChecked():
                            runstring = self.parent.text_output_program_qdlc_command_sweep.toPlainText()
                            for i,(p1,p2) in enumerate(zip(self.parent.scan_sweep_values_1.flatten(),self.parent.scan_sweep_values_2.flatten())):
                                if self.parent.checkbox_activate_scan_parameter_2.isChecked():
                                    runstr = self.parent.qdlc_start_command_to_real(runstring.replace("[QDLC]", f"QDLC --lfc {p1},{p2}").replace("[FILEPATH]",""))
                                    f.write(f"{runstr.format(p1,p2)}\n")
                                    self.text.emit(f"{runstr.format(p1,p2)}")
                                else:
                                    runstr = self.parent.qdlc_start_command_to_real(runstring.replace("[QDLC]", f"QDLC --lfc {p1}").replace("[FILEPATH]",""))
                                    f.write(f"{runstr.format(p1)}\n")
                                    self.text.emit(f"{runstr.format(p1)}")
                                self.progress.emit(100*(i+1)/(self.parent.scan_sweep_values_1.shape[0]*self.parent.scan_sweep_values_1.shape[1]))
                        else:
                            runstring = self.parent.text_output_program_qdlc_command.toPlainText()
                            runstr = self.parent.qdlc_start_command_to_real(runstring.replace("[QDLC]", "QDLC").replace("[FILEPATH]",""))
                            f.write(f"{runstr}\n")
                            self.text.emit(runstr)
                    self.text.emit("Done!")
                    self.finished.emit()
            self.thread = QThread()
            self.worker = SettingfileWorker(self)
            def update_text(new_line):
                self.text_output_program_qdlc_command_sweep_display.append(new_line)
                self.text_output_program_main.append(new_line)
            def update_pb(percent):
                self.progressBar.setValue(percent)
            self.worker.progress.connect(update_pb)
            self.worker.text.connect(update_text)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
            
        def save_settings_file():
            filepath = self.textinput_path_to_settingfile.text()
            if filepath == "":
                return
            project_name, ok = QInputDialog.getText(self, "Save Settings", "Project Name", QLineEdit.Normal, filepath.split("/")[-1].replace(".txt", ""))
            self.text_output_program_main.append(f"Saving Settingfile to {filepath}")
            if not ok or not len(project_name):
                self.sendErrorMessage("No Name given")
                return
            save_to_setting_file(filepath, project_name)
        self.button_generate_setting_file.clicked.connect(save_settings_file)

        def set_qdlc_runstr_to_settingfile():
            runstr = f"[QDLC] --file [SETTINGFILE] [FILEPATH]"
            self.text_output_program_qdlc_command.setPlainText(runstr)
        self.button_change_rungstring_to_settingfile.clicked.connect(set_qdlc_runstr_to_settingfile)

        def generate_list_of_available_states():
            available_states = []
            for state in self.system_components["EnergyLevels"]:
                new_state = f"{state}" + "".join([f":0{name}" for name in self.system_components["CavityLevels"]])
                available_states.append(new_state)
            return available_states
        def pick_from_list_of_available_states():
            items = generate_list_of_available_states()
            print(items)
            item, ok = QInputDialog.getItem(self, "Select Input State", "Valid States", items, 0, False)
            if ok and item:
                self.textinput_initial_state.setText(item)
        self.input_initial_state.clicked.connect(pick_from_list_of_available_states)

        # Dynamic change phonons
        def toggle_phonon_inputs():
            enable = self.input_phonons_use_qd.isChecked()
            for a in [self.textinput_phonons_sd_qd_de,self.textinput_phonons_sd_qd_dh,self.textinput_phonons_sd_qd_rho,self.textinput_phonons_sd_qd_cs,self.textinput_phonons_sd_qd_aeah_ratio,self.textinput_phonons_sd_qd_size]:
                a.setEnabled(enable)
            self.textinput_phonons_sd_alpha.setEnabled(not enable)
        self.input_phonons_use_qd.stateChanged.connect(toggle_phonon_inputs)

        # Set ListView Models
        self.list_components.setModel(QStandardItemModel())
        self.text_output_list_of_spectra.setModel(QStandardItemModel())

        # Add/Remove Spectrum Buttons
        def spectrum_add():
            spec_modes = self.textinput_spectrum_modes.text().split(",")
            spec_range = self.textinput_spectrum_range.text()
            spec_center = self.textinput_spectrum_center.text()
            spec_res = self.textinput_spectrum_res.text()
            spec_order = self.input_spectrum_order.currentIndex()
            spec_norm = self.input_spectrum_normalize.isChecked()
            name = f"{''.join(spec_modes)}{spec_range}{spec_center}{spec_res}{spec_order}{spec_norm}"
            self.add_component( "Spectrum", {"Name" : name, "Modes" : spec_modes, "Range" : spec_range, "Center" : spec_center, "Res" : spec_res, "Order" : spec_order, "Norm": spec_norm} )
            #self.text_output_list_of_spectra.model().appendRow(QStandardItem(f"For modes {','.join(spec_modes)} at center {spec_center} with resolution {spec_res} and range {spec_range}. Identifier: {name}"))
            self.update_component_list()
        def spectrum_remove():
            index = self.text_output_list_of_spectra.currentIndex().row()
            name = self.text_output_list_of_spectra.model().item(index).toolTip()
            self.system_components["Spectrum"].pop(name)
            self.update_component_list()
            #self.text_output_list_of_spectra.model().removeRow(self.text_output_list_of_spectra.currentIndex().row().row())
        def spectrum_active_change():
            try:
                index = self.text_output_list_of_spectra.currentIndex().row()
                name = self.text_output_list_of_spectra.model().item(index).toolTip()
            except:
                return
            struct = self.system_components["Spectrum"][name]
            for text, field in zip( [",".join(struct["Modes"]), struct["Range"], struct["Center"], struct["Res"]], [self.textinput_spectrum_modes, self.textinput_spectrum_range, self.textinput_spectrum_center, self.textinput_spectrum_res] ):
                field.setText(text)
            self.input_spectrum_order.setCurrentIndex(struct["Order"])
            self.input_spectrum_normalize.setChecked(struct["Norm"])
        def spectrum_predict_plot():
            # alle cavs. und transitions durchgehen
            # alle energien rausschreiben
            # für jede cav lorentzpeak
            # für jede transition lorentzpeak
            from matplotlib.lines import Line2D
            def normalize(y):
                return (y-np.min(y))/(np.max(y)-np.min(y))
            def lorentzian(x, a, x0):
                return normalize(1 / ((x-x0)**2 + a**2) / np.pi)
            energies_cavity = [ get_uv_scaled(struct["Energy"]) for struct in self.system_components["CavityLevels"].values() ]
            #transition = list(set([ abs(get_uv_scaled(struct["Energy"]) - get_uv_scaled(other["Energy"])) for struct in self.system_components["EnergyLevels"].values() for other in self.system_components["EnergyLevels"].values() ]))
            transition = list(set([ abs(get_uv_scaled(struct["Energy"]) - get_uv_scaled(self.system_components["EnergyLevels"][other]["Energy"])) for struct in self.system_components["EnergyLevels"].values() for other in struct["CoupledTo"] ]))
            self.label_plot_spectral_prediction.canvas.axes.clear()
            mmax = np.max(energies_cavity + transition)
            mmin = np.min(energies_cavity + transition)
            mean = np.median(energies_cavity + transition)/5000
            x = np.linspace( mmin-4*mean,mmax+4*mean, 10000)
            cavity_kappa = get_uv_scaled(self.textinput_rates_cavity_loss.text())
            cavity_g = get_uv_scaled(self.textinput_rates_cavity_coupling.text())
            electronic_gamma = get_uv_scaled(self.textinput_rates_radiative_decay.text())+get_uv_scaled(self.textinput_rates_pure_dephasing.text())
            ev_scaling = 1/get_unit_scaling("eV")
            if len(energies_cavity):
                self.label_plot_spectral_prediction.canvas.axes.plot(x*ev_scaling, normalize(sum([lorentzian(x-cavity_g, cavity_kappa, cav)+lorentzian(x+cavity_g, cavity_kappa, cav) for cav in energies_cavity])), color="blue")
            if len(transition):
                self.label_plot_spectral_prediction.canvas.axes.plot(x*ev_scaling, normalize(sum([lorentzian(x, electronic_gamma, tra) for tra in transition])), color="red")
            lines = [Line2D([0], [0], color="blue"), Line2D([0], [0], color="red")]
            self.label_plot_spectral_prediction.canvas.axes.legend(lines,["Cavity", "Transition"])
            self.label_plot_spectral_prediction.canvas.draw()
        
        self.text_output_list_of_spectra.selectionModel().selectionChanged.connect(spectrum_active_change)
        self.button_add_spectrum_to_output.clicked.connect(spectrum_add)
        self.button_remove_spectrum_from_output.clicked.connect(spectrum_remove)
    
        # Indist
        self.text_output_list_of_indists.setModel(QStandardItemModel())
        def indist_add():
            indist_modes = self.textinput_indist_modes.text().split(",")
            if not len(indist_modes):
                return
            for mode in indist_modes:
                if not len(mode):
                    continue
                self.add_component( "Indistinguishability", {"Name" : mode, "Mode" : mode} )
            self.update_component_list()
        def indist_remove():
            index = self.text_output_list_of_indists.currentIndex().row()
            name = self.text_output_list_of_indists.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Indistinguishability"]:
                return
            self.system_components["Indistinguishability"].pop(name)
            self.update_component_list()
        self.button_add_indist_to_output.clicked.connect(indist_add)
        self.button_remove_indist_from_output.clicked.connect(indist_remove)

        # Concurrence
        self.text_output_list_of_concurrences.setModel(QStandardItemModel())
        def concurrence_add():
            concurrence_mode_1 = self.textinput_concurrence_first.text()
            concurrence_mode_2 = self.textinput_concurrence_second.text()
            if not len(concurrence_mode_1) or not len(concurrence_mode_2):
                return
            self.add_component( "Concurrence", {"Name" : concurrence_mode_1+concurrence_mode_2, "Mode" : concurrence_mode_1+"+"+concurrence_mode_2} )
            self.update_component_list()
        def concurrence_remove():
            index = self.text_output_list_of_concurrences.currentIndex().row()
            name = self.text_output_list_of_concurrences.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Concurrence"]:
                return
            self.system_components["Concurrence"].pop(name)
            self.update_component_list()
        def toggle_concurrence_spectrum():
            enable = self.input_concurrence_add_spectra.isChecked()
            for a in [self.textinput_concurrence_spec_freq,self.textinput_concurrence_spec_range,self.textinput_concurrence_spec_res]:
                a.setEnabled(enable)
        self.input_concurrence_add_spectra.stateChanged.connect(toggle_concurrence_spectrum)
        self.button_add_concurrence_to_output.clicked.connect(concurrence_add)
        self.button_remove_concurrence_from_output.clicked.connect(concurrence_remove)

        # G1 and G2
        self.text_output_list_of_gfuncs.setModel(QStandardItemModel())
        def gfunc_add():
            modes = self.textinput_correlation_modes.text().split(",")
            order = self.input_gfunc_order.currentIndex()
            method = self.input_gfunc_integration.currentIndex()
            if not len(modes):
                return
            for mode in modes:
                if not len(mode):
                    continue
                name = mode+str(order)+str(method)
                self.add_component( "G1G2", {"Name" : name, "Mode" : mode, "Order" : order, "Method" : method} )
            self.update_component_list()
        def gfunc_remove():
            index = self.text_output_list_of_gfuncs.currentIndex().row()
            name = self.text_output_list_of_gfuncs.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["G1G2"]:
                return
            self.system_components["G1G2"].pop(name)
            self.update_component_list()
        self.button_add_gfunc_to_output.clicked.connect(gfunc_add)
        self.button_remove_gfunc_from_output.clicked.connect(gfunc_remove)

        # Detector
        self.text_output_list_of_detector_time.setModel(QStandardItemModel())
        def detector_time_add():
            t0 = self.textinput_detector_t0.text()
            t1 = self.textinput_detector_t1.text()
            power = self.textinput_detector_tpower.text()
            if not len(t0) or not len(t1) or not len(power):
                return
            name = t0+t1+power
            self.add_component( "DetectorTime", {"Name" : name, "t0" : t0, "t1" : t1, "Power" : power} )
            self.update_component_list()
        def detector_time_remove():
            index = self.text_output_list_of_detector_time.currentIndex().row()
            name = self.text_output_list_of_detector_time.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["DetectorTime"]:
                return
            self.system_components["DetectorTime"].pop(name)
            self.update_component_list()
        self.text_output_list_of_detector_spec.setModel(QStandardItemModel())
        def detector_spec_add():
            w0 = self.textinput_detector_wcenter.text()
            w1 = self.textinput_detector_wrange.text()
            res = self.textinput_detector_wnum.text()
            power = self.textinput_detector_wpower.text()
            if not len(w0) or not len(w1) or not len(res) or not len(power):
                return
            name = w0+w1+res+power
            self.add_component( "DetectorSpectrum", {"Name" : name, "w0" : w0, "w1" : w1, "Points" : res, "Power" : power} )
            self.update_component_list()
        def detector_spec_remove():
            index = self.text_output_list_of_detector_spec.currentIndex().row()
            name = self.text_output_list_of_detector_spec.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["DetectorSpectrum"]:
                return
            self.system_components["DetectorSpectrum"].pop(name)
            self.update_component_list()
        self.button_add_detector_time.clicked.connect(detector_time_add)
        self.button_add_detector_spectral.clicked.connect(detector_spec_add)
        self.button_remove_detector_time.clicked.connect(detector_time_remove)
        self.button_remove_detector_spectral.clicked.connect(detector_spec_remove)
        

        # Wigner Function
        self.text_output_list_of_wigner_funcs.setModel(QStandardItemModel())
        def wigner_func_add():
            modes = self.textinput_wigner_modes.text().split(",")
            xmax = self.textinput_wigner_x.text()
            ymax = self.textinput_wigner_y.text()
            res = self.textinput_wigner_resolution.text()
            skip = self.textinput_wigner_skip.text()
            if not len(modes):
                return
            for mode in modes:
                if not len(mode):
                    continue
                name = mode+xmax+ymax+res+skip
                self.add_component( "Wigner", {"Name" : name, "Mode" : mode, "XMax" : xmax, "YMax" : ymax, "Resolution" : res, "Skip" : skip} )
            self.update_component_list()
        def wigner_func_remove():
            index = self.text_output_list_of_wigner_funcs.currentIndex().row()
            name = self.text_output_list_of_wigner_funcs.model().item(index).toolTip()
            if name is None or not len(name):
                return
            if name not in self.system_components["Wigner"]:
                return
            self.system_components["Wigner"].pop(name)
            self.update_component_list()
        self.button_add_wigner.clicked.connect(wigner_func_add)
        self.button_remove_wigner.clicked.connect(wigner_func_remove)

        # Phonon Spectral functions
        def phonon_spectral_function(multi: bool = False):
            phonon_ohm = get_uv_scaled(self.textinput_phonons_sd_ohmamp.text())
            phonon_cutoff = get_uv_scaled(self.textinput_phonons_sd_wcutoff.text())
            x = np.linspace(0, 6*phonon_cutoff, 1000)
            if multi:
                phonon_rho = get_uv_scaled(self.textinput_phonons_sd_qd_rho.text())
                phonon_de = get_uv_scaled(self.textinput_phonons_sd_qd_de.text())
                phonon_dh = get_uv_scaled(self.textinput_phonons_sd_qd_dh.text())
                phonon_cs = get_uv_scaled(self.textinput_phonons_sd_qd_cs.text())
                phonon_ahr = get_uv_scaled(self.textinput_phonons_sd_qd_aeah_ratio.text())
                phonon_s = get_uv_scaled(self.textinput_phonons_sd_qd_size.text())
                ac_over_cs = phonon_s**2/(4*phonon_cs**2)
                hbar = get_unit_scaling("hbar")
                y = hbar*x**phonon_ohm / (4*np.pi**2*phonon_rho*phonon_cs**5)*( phonon_de*np.exp(-x**2*ac_over_cs) - phonon_dh*np.exp(-x**2*ac_over_cs/phonon_ahr**2) )**2
            else:
                phonon_alpha = get_uv_scaled(self.textinput_phonons_sd_alpha.text())
                y = phonon_alpha * x**phonon_ohm * np.exp(-x**2/phonon_cutoff**2/2)
            return x,y
        def plot_phonon_spectral_function():
            self.label_plot_spectral_density.canvas.axes.clear()
            x,y = phonon_spectral_function()
            self.label_plot_spectral_density.canvas.axes.plot(x,y)
            if self.input_phonons_use_qd.isChecked():
                x,y = phonon_spectral_function(True)
                self.label_plot_spectral_density.canvas.axes.plot(x,y)
            # legend
            self.label_plot_spectral_density.canvas.axes.legend(["Simple", "QD Params"])
            self.label_plot_spectral_density.canvas.draw()
        
        # Experimental: Add N coupled TLS
        def get_N_level_couplings(cl: str, prefix: str, energy):
            coupled_to = []
            for i in range(len(cl)):
                if cl[i] != "1":
                    state = f"{cl[:i] + '1' + cl[i+1:]}"
                    coupled_to.append( state ) 
            # Add state to system
            self.addEnergyLevel({"Name": f"{prefix}{cl}","Energy": energy(),"CoupledTo": tuple([f"{prefix}{ct}" for ct in coupled_to]),"DecayScaling" : "1" if "1" in cl else "0","DephasingScaling": "1","PhononScaling": "1" if "1" in cl else "0"} )
            return coupled_to
        def add_N_levels(nTLS: int = 2, energy: float = 1.0, sd = 1E-3, unit: str = "eV", prefix: str = "X"):
            states = ["0"*nTLS]
            current_deph = 0
            while len(states):
                # random value between -sd and +sd
                senergy = lambda: f"{current_deph * (energy + (np.random.rand() - 0.5) * sd)}{unit}"
                states = [get_N_level_couplings(state, prefix, senergy) for state in states]
                states = [item for sebstates in states for item in sebstates]
                states = list(set(states))
                current_deph += 1
            len(states)
        def dialog_add_N_levels():
            nTLS, ok = QInputDialog.getInt(self, "Add N TLS", "Number of TLS", 2, 1, 30, 1)
            if ok:
                energy, ok2 = QInputDialog.getDouble(self, "Energy", "Singe State Energy in eV", 1, 0, 1000, 1)
            if ok and ok2:
                stv, ok3 = QInputDialog.getDouble(self, "Energy Uncertainty", "Energy Uncertainty in mueV", 0, 0, 100000,1)
            if ok and ok2 and ok3:
                add_N_levels(nTLS, energy, stv*1E-6)

        def get_all_transitions():
            transitions = []
            for state in self.system_components["EnergyLevels"].values():
                for transition in state["CoupledTo"]:
                    transitions.append(f"{state['Name']}={transition}")
            return transitions
        def print_all_transitions():
            print(",".join(get_all_transitions()))

        def clipboard_copy_transition_list():
            self.clipboard.setText(",".join(get_all_transitions()))
        def clipboard_copy_sum_of_transition_list():
            self.clipboard.setText("+".join(get_all_transitions()))

        # Run
        def generate_command():
            self.set_components_from_fields()
            command = self.qdlc_generate_start_command()
            self.text_output_program_qdlc_command.setText(command)
            self.clipboard.setText(self.qdlc_start_command_to_real(command))
        self.button_generate_run.clicked.connect(generate_command)

        class QDLCWorker(QObject):
            finished = Signal()
            progress = Signal(str)
            def __init__(self, command, cwd, dest, sf = None):
                super().__init__()
                self.command = command
                self.cwd = cwd
                self.dest = dest
                self.process = None
                self.running = False
                self.appendix = [dest] if sf is None else ["--file", sf, dest]
            def run(self):
                print("Running QDLC")
                self.running = True
                print(self.command.split() + self.appendix)
                self.process = Popen(self.command.split() + self.appendix, stdout=PIPE, universal_newlines = True, cwd=self.cwd, shell=True)
                while True and self.running:
                    output = self.process.stdout.readline()
                    if output == '' and self.process.poll() is not None:
                        break
                    print(f"RAW: {repr(output)}")
                    self.progress.emit(replace_ansi_escape_sequences(output.strip()))
                    #print(output.strip())
                    #self.pipe.setText(output.strip())
                self.process.communicate()
                self.finished.emit()
        def run_command():
            # Get Command
            command = self.text_output_program_qdlc_command.toPlainText()
            # Insert Destination and QDLC Path
            command = self.qdlc_start_command_to_real(command)
            # Strip QDLC Path and Destination Path
            qdlc_path_str = self.textinput_file_qdlc.text()
            destination = self.textinput_file_destination.text()
            settingfilepath = self.textinput_path_to_settingfile.text()
            qdlc_path = qdlc_path_str.split("/")
            qdlc_executable = qdlc_path[-1]
            print(f"QDLC Executable: {qdlc_executable}")
            cwd = qdlc_path_str.replace(qdlc_executable, "")
            command = command.replace(qdlc_path_str, qdlc_executable).replace("'"+destination+"'", "")
            use_settingfile = "--file" in command
            if use_settingfile:
                command = command.replace("--file '"+settingfilepath+"'", "")
                
            print(f"QDLC Working Directory: {cwd}\nDestination: {destination}\nRunning command: {command}")
            if not len(command):
                return
            self.thread = QThread()
            self.worker = QDLCWorker(command, cwd, destination, settingfilepath if use_settingfile else None)
            def update(new_line):
                self.text_output_program_main.append(new_line)
                if "%" in new_line:
                    try:
                        percent = int(new_line.split("%")[0].split()[-1])
                        current_percent = self.progressBar.value()
                        self.progressBar.setValue(max(percent,current_percent))
                    except:
                        pass
                if "Done" in new_line:
                    self.progressBar.setValue(0)
            self.worker.progress.connect(update)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        
        def kill_command():
            self.text_output_program_main.append("Killed QDLC!")
            self.worker.running = False
            from signal import CTRL_C_EVENT 
            self.worker.process.send_signal(CTRL_C_EVENT)
            self.worker.process.kill()
            self.thread.quit()
            self.thread.wait()
            self.progressBar.setValue(0)

        self.button_run_program.clicked.connect(run_command)
        self.button_run_kill.clicked.connect(kill_command)

        # Sweeper
        self.button_sweeper_get_runstring.clicked.connect(lambda: self.text_output_program_qdlc_command_sweep.setText(self.text_output_program_qdlc_command.toPlainText()))

        actions_to_add = [  
            ["Print Component Dict", lambda: print(self.system_components), self.menuDeveloper_Tools],
            ["Set Components from Fields", self.set_components_from_fields, self.menuDeveloper_Tools],
            ["Set Fields from Components", self.set_fields_from_components, self.menuDeveloper_Tools],
            ["Connect Fields", self.connect_config_to_fields, self.menuDeveloper_Tools],
            ["Plot Predicted Spectra", spectrum_predict_plot, self.menuFunctions],
            ["Plot Phonon Functions", plot_phonon_spectral_function, self.menuFunctions],
            ["Add N TLS", dialog_add_N_levels, self.menuEdit],
            ["Print All Transitions", print_all_transitions, self.menuFunctions],
            ["Copy List of Transitions", clipboard_copy_transition_list, self.menuFunctions],
            ["Copy Sum of Transitions", clipboard_copy_sum_of_transition_list, self.menuFunctions],
            ["Export QDLC Command", export_command, self.menuMenu],
            ["Import QDLC Command", import_command, self.menuMenu],
            ["Redraw System", self.drawSystem, self.menuFunctions],
            ["Clear System", self.clearSystem, self.menuFunctions],
            ["Generate QDLC Command", generate_command, self.menuFunctions],
            ["Set initial State", pick_from_list_of_available_states, self.menuFunctions],
            ["Set File Destination", set_file_path, self.menuMenu],
            ["Set QDLC Filepath", set_qdlc_filepath, self.menuMenu],
            ["Run QDLC", run_command, self.menuMenu],
        ]
        for name, connect, where in actions_to_add:
            action = QAction(name, self)
            action.triggered.connect(connect)
            where.addAction(action)

        # Connect Sweeper
        self.button_sweeper_plot.clicked.connect(self.generate_scan_or_sweep)

        self.button_generate_copy.clicked.connect(lambda: self.clipboard.setText(self.qdlc_start_command_to_real(self.text_output_program_qdlc_command.toPlainText())))

    def sendMessage(self, bar: str, title: str, message: str):
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(bar)
        msg.setStyleSheet(self.styleSheet())
        msg.exec()
    def sendErrorMessage(self, error: str = "Error!", message: str = "Error!"):
        self.sendMessage("Error!",error,message)
    def sendWarningMessage(self, warning: str = "Warning!", message: str = "Warning!"):
        self.sendMessage("Warning!",warning,message)
    def sendHintMessage(self, message: str = "Attention!"):
        self.sendMessage("Attention!","Attention!",message)

    def clearSystem(self):
        self.system_components["EnergyLevels"] = {}
        self.system_energy_level_groups = list()
        self.system_components["CavityLevels"] = {}
        self.system_cavity_level_groups = list()
        self.system_components["Pulse"] = {}
        self.system_components["Shift"] = {}
        self.update_component_list()
        self.drawSystem()

    def sort_energy_levels(self, group_threshold: float = 0.05) -> None:
        levels = [a for a in self.system_components["EnergyLevels"].values()]
        if len(levels) < 2:
            return
        levels.sort(key=lambda l: get_uv_scaled(l["Energy"]))
        # Check grouping
        grouping_threshold = abs(get_uv_scaled(levels[0]["Energy"]) - get_uv_scaled(levels[-1]["Energy"])) * group_threshold
        self.system_energy_level_groups = list()
        self.system_energy_level_groups.append([levels[0]]) # List of Groupings
        for level in levels[1:]:
            if abs(get_uv_scaled(level["Energy"]) - get_uv_scaled(self.system_energy_level_groups[-1][-1]["Energy"])) < grouping_threshold:
                # Is Part of Group
                self.system_energy_level_groups[-1].append(level)
            else:
                self.system_energy_level_groups.append([level])

    ###########################################################################################################
    ########################################### Adding System Components ######################################
    ###########################################################################################################
    def add_component(self, category: str, struct: dict) -> None:
        name = struct["Name"]
        changed = "Added" if name not in self.system_components[category] else "Replaced"
        self.system_components[category][name] = struct

        self.update_component_list()
        self.drawSystem()
        print(changed, self.system_components[category][name])

    def update_component_list(self):
        model = self.list_components.model()
        model.clear()
        for cat in self.system_components:
            if cat not in ["EnergyLevels", "CavityLevels", "Pulse", "Shift"]:
                continue 
            for name in self.system_components[cat]:
                item = QStandardItem(name + " - " + cat)
                model.appendRow(item)
        model = self.text_output_list_of_spectra.model()
        model.clear()
        for name,struct in self.system_components["Spectrum"].items():
            item = QStandardItem(f"For modes {','.join(struct['Modes'])} at center {struct['Center']} with resolution {struct['Res']} and range {struct['Range']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_indists.model()
        model.clear()
        for name, struct in self.system_components["Indistinguishability"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_concurrences.model()
        model.clear()
        for name, struct in self.system_components["Concurrence"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_gfuncs.model()
        model.clear()
        for name, struct in self.system_components["G1G2"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']} using G{2 if struct['Order'] else 1} with output method {struct['Method']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_wigner_funcs.model()
        model.clear()
        for name, struct in self.system_components["Wigner"].items():
            item = QStandardItem(f"For mode(s): {struct['Mode']} with x in [-{struct['XMax']},{struct['XMax']}] and y in [-{struct['YMax']},{struct['YMax']}] at resoultion {struct['Resolution']}. Outputting every {struct['Skip']} timesteps.")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_detector_time.model()
        model.clear()
        for name, struct in self.system_components["DetectorTime"].items():
            item = QStandardItem(f"At t0 = {struct['t0']} with width {struct['t1']} and power falloff {struct['Power']}")
            item.setToolTip(name)
            model.appendRow(item)
        model = self.text_output_list_of_detector_spec.model()
        model.clear()
        for name, struct in self.system_components["DetectorSpectrum"].items():
            item = QStandardItem(f"At w0 = {struct['w0']} with width {struct['w1']} and power falloff {struct['Power']}. Using {struct['Points']} fourier points.")
            item.setToolTip(name)
            model.appendRow(item)

    def addEnergyLevel(self, p: dict ):
        self.add_component( "EnergyLevels", p )
        
    def addCavity(self, p: dict):
        self.add_component( "CavityLevels", p )

    def addPulse(self, p: dict):
        # Confirm that Pulse sizes are the same:
        a,f,c,w,t = len(p["Amplitudes"]), len(p["Frequencies"]), len(p["Centers"]), len(p["Widths"]), len(p["Type"])
        if not (a==f and f==c and c==w and w==t):
            self.sendErrorMessage("Wrong Pulse Dimensions", "The arrays you entered for the Pulse parameters must be of equal length!")
            return
        self.add_component( "Pulse", p )
        
    def addShift(self, p: dict):
        self.add_component( "Shift", p )

    # Parses All configs from always-on entries like time, solver, etc.
    def connect_config_to_fields(self):
        # Time
        self.system_components_fields["ConfigTime"] = {
            "Start" : {"parse": self.textinput_time_startingtime.text, "set": self.textinput_time_startingtime.setText, "typeof" : str},
            "End" : {"parse": self.textinput_time_endtime.text, "set": self.textinput_time_endtime.setText, "typeof" : str},
            "Step" : {"parse": self.textinput_time_timestep.text, "set": self.textinput_time_timestep.setText, "typeof" : str}
        }
        self.system_components_fields["ConfigGrid"] = {
            "Resolution" : {"parse": self.textinput_time_gridresolution.text, "set": self.textinput_time_gridresolution.setText, "typeof" : str}
        }
        self.system_components_fields["ConfigTolerances"] = {
            "Resolution" : {"parse": self.textinput_time_tolerance.text, "set": self.textinput_time_tolerance.setText, "typeof" : str}
        }
        self.system_components_fields["ConfigSolver"] = {
            "Solver" : {"parse": self.input_rungekutta_order.currentIndex, "set": self.input_rungekutta_order.setCurrentIndex, "typeof" : int},
            "Interpolator" : {"parse": self.input_interpolator_t.currentIndex, "set": self.input_interpolator_t.setCurrentIndex, "typeof" : int},
            "InterpolatorGrid" : {"parse": self.input_interpolator_tau.currentIndex, "set": self.input_interpolator_tau.setCurrentIndex, "typeof" : int},
            "NC" : {"parse": self.textinput_phonons_nc.text, "set": self.textinput_phonons_nc.setText, "typeof" : str},
        }
        self.system_components_fields["ConfigSystem"] = {
            "Coupling" : {"parse": self.textinput_rates_cavity_coupling.text, "set": self.textinput_rates_cavity_coupling.setText, "typeof" : str},
            "CavityLosses" : {"parse": self.textinput_rates_cavity_loss.text, "set": self.textinput_rates_cavity_loss.setText, "typeof" : str},
            "RadiativeLosses" : {"parse": self.textinput_rates_radiative_decay.text, "set": self.textinput_rates_radiative_decay.setText, "typeof" : str},
            "DephasingLosses" : {"parse": self.textinput_rates_pure_dephasing.text, "set": self.textinput_rates_pure_dephasing.setText, "typeof" : str},
        }
        self.system_components_fields["ConfigPhonons"] = {
            "Temperature" : {"parse": self.textinput_phonons_temperature.text, "set": self.textinput_phonons_temperature.setText, "typeof" : str},
            "IteratorStep" : {"parse": self.textinput_phonons_iterator_stepsize.text, "set": self.textinput_phonons_iterator_stepsize.setText, "typeof" : str},
            "Approximation" : {"parse": self.input_phonons_approximation.currentIndex, "set": self.input_phonons_approximation.setCurrentIndex, "typeof" : int},
            "ARRad" : {"parse": self.input_phonons_adjust_radiativeloss.isChecked, "set": self.input_phonons_adjust_radiativeloss.setChecked, "typeof" : bool},
            "ARDep" : {"parse": self.input_phonons_adjust_pure_dephasing.isChecked, "set": self.input_phonons_adjust_pure_dephasing.setChecked, "typeof" : bool},
            "Renormalization" : {"parse": self.input_phonons_adjust_renormalization.isChecked, "set": self.input_phonons_adjust_renormalization.setChecked, "typeof" : bool},
            "Alpha" : {"parse": self.textinput_phonons_sd_alpha.text, "set": self.textinput_phonons_sd_alpha.setText, "typeof" : str},
            "SpectralCutoff" : {"parse": self.textinput_phonons_sd_wcutoff.text, "set": self.textinput_phonons_sd_wcutoff.setText, "typeof" : str},
            "SpectralDelta" : {"parse": self.textinput_phonons_sd_wdelta.text, "set": self.textinput_phonons_sd_wdelta.setText, "typeof" : str},
            "TimeCutoff" : {"parse": self.textinput_phonons_sd_tcutoff.text, "set": self.textinput_phonons_sd_tcutoff.setText, "typeof" : str},
            "Ohm" : {"parse": self.textinput_phonons_sd_ohmamp.text, "set": self.textinput_phonons_sd_ohmamp.setText, "typeof" : str},
            "UseQD" : {"parse": self.input_phonons_use_qd.isChecked, "set": self.input_phonons_use_qd.setChecked, "typeof" : bool},
            "QDde" : {"parse": self.textinput_phonons_sd_qd_de.text, "set": self.textinput_phonons_sd_qd_de.setText, "typeof" : str},
            "QDdh" : {"parse": self.textinput_phonons_sd_qd_dh.text, "set": self.textinput_phonons_sd_qd_dh.setText, "typeof" : str},
            "QDrho" : {"parse": self.textinput_phonons_sd_qd_rho.text, "set": self.textinput_phonons_sd_qd_rho.setText, "typeof" : str},
            "QDcs" : {"parse": self.textinput_phonons_sd_qd_cs.text, "set": self.textinput_phonons_sd_qd_cs.setText, "typeof" : str},
            "QDeh" : {"parse": self.textinput_phonons_sd_qd_aeah_ratio.text, "set": self.textinput_phonons_sd_qd_aeah_ratio.setText, "typeof" : str},
            "QDs" : {"parse": self.textinput_phonons_sd_qd_size.text, "set": self.textinput_phonons_sd_qd_size.setText, "typeof" : str},
        }
        self.system_components_fields["InitialState"] = {
            "State" : {"parse" : self.textinput_initial_state.text, "set": self.textinput_initial_state.setText, "typeof" : str},
        }
        self.system_components_fields["RunConfig"] = {
            "PathQDLC" : {"parse" : self.textinput_file_qdlc.text, "set" : self.textinput_file_qdlc.setText, "typeof" : str},
            "PathOutput" : {"parse" : self.textinput_file_destination.text, "set" : self.textinput_file_destination.setText, "typeof" : str},
            "LoggingLevel" : {"parse" : self.input_logginglevel.currentIndex, "set" : self.input_logginglevel.setCurrentIndex, "typeof" : int},
            "DMOutputMode" : {"parse" : self.input_dm_mode.currentIndex, "set" : self.input_dm_mode.setCurrentIndex, "typeof" : int},
            "OutputFrame" : {"parse" : self.input_dm_frame.currentIndex, "set" : self.input_dm_frame.setCurrentIndex, "typeof" : int},
            "CPUCores" : {"parse" : self.textinput_cpucores.text, "set" : self.textinput_cpucores.setText, "typeof" : str},
            "Settingfile" : {"parse" : self.textinput_path_to_settingfile.text, "set" : self.textinput_path_to_settingfile.setText, "typeof" : str},
            "QDLCRun" : {"parse" : self.text_output_program_qdlc_command.toPlainText, "set" : self.text_output_program_qdlc_command.setPlainText, "typeof" : str},
        }
        self.system_components_fields["OutputFlags"] = {
            "eigenvalues" : {"parse" : self.input_add_output_eigenvalues.isChecked, "set" : self.input_add_output_eigenvalues.setChecked, "typeof" : bool},
            "operators" : {"parse" : self.input_add_output_operators.isChecked, "set" : self.input_add_output_operators.setChecked, "typeof" : bool},
            "rkerror" : {"parse" : self.input_add_output_rkerror.isChecked, "set" : self.input_add_output_rkerror.setChecked, "typeof" : bool},
            "path" : {"parse" : self.input_add_output_vonneumannpath.isChecked, "set" : self.input_add_output_vonneumannpath.setChecked, "typeof" : bool},
            "detectortrafo" : {"parse" : self.input_add_output_detecotrtrafo.isChecked, "set" : self.input_add_output_detecotrtrafo.setChecked, "typeof" : bool},
            "greenf" : {"parse" : self.input_add_output_greenf.isChecked, "set" : self.input_add_output_greenf.setChecked, "typeof" : bool}, # also for PIkernel if PI is used
            "phononJ" : {"parse" : self.input_add_output_phononj.isChecked, "set" : self.input_add_output_phononj.setChecked, "typeof" : bool},
            "phononcoefficients" : {"parse" : self.input_add_output_phononcoeffs.isChecked, "set" : self.input_add_output_phononcoeffs.setChecked, "typeof" : bool}, 
            "conc" : {"parse" : self.input_add_output_concurrence_eigs.isChecked, "set" : self.input_add_output_concurrence_eigs.setChecked, "typeof" : bool},
            "tpm" : {"parse" : self.input_add_output_tpm.isChecked, "set" : self.input_add_output_tpm.setChecked, "typeof" : bool},
            "chirpf" : {"parse" : self.input_add_output_chirp_fourier.isChecked, "set" : self.input_add_output_chirp_fourier.setChecked, "typeof" : bool},
            "pulsef" : {"parse" : self.input_add_output_pulse_fourier.isChecked, "set" : self.input_add_output_pulse_fourier.setChecked, "typeof" : bool},
        }
        self.system_components_fields["ConcurrenceSpectrum"] = {
            "Active" : {"parse" : self.input_concurrence_add_spectra.isChecked, "set" : self.input_concurrence_add_spectra.setChecked, "typeof" : bool},
            "Center" : {"parse" : self.textinput_concurrence_spec_freq.text, "set" : self.textinput_concurrence_spec_freq.setText, "typeof" : str},
            "Range" : {"parse" : self.textinput_concurrence_spec_range.text, "set" : self.textinput_concurrence_spec_range.setText, "typeof" : str},
            "Res" : {"parse" : self.textinput_concurrence_spec_res.text, "set" : self.textinput_concurrence_spec_res.setText, "typeof" : str},
        }
        self.system_components_fields["Sweeper"] = {
            "Parameter1" : {"parse" : self.checkbox_activate_scan_parameter_1.isChecked, "set" : self.checkbox_activate_scan_parameter_1.setChecked, "typeof" : bool},
            "Parameter2" : {"parse" : self.checkbox_activate_scan_parameter_1.isChecked, "set" : self.checkbox_activate_scan_parameter_1.setChecked, "typeof" : bool},
            "From1" : {"parse" : self.textinput_scan_parameter_1_from.text, "set" : self.textinput_scan_parameter_1_from.setText, "typeof" : str},
            "From2" : {"parse" : self.textinput_scan_parameter_2_from.text, "set" : self.textinput_scan_parameter_2_from.setText, "typeof" : str},
            "to1" : {"parse" : self.textinput_scan_parameter_1_to.text, "set" : self.textinput_scan_parameter_1_to.setText, "typeof" : str},
            "to2" : {"parse" : self.textinput_scan_parameter_2_to.text, "set" : self.textinput_scan_parameter_2_to.setText, "typeof" : str},
            "Points1" : {"parse" : self.textinput_scan_parameter_1_points.text, "set" : self.textinput_scan_parameter_1_points.setText, "typeof" : str},
            "Points2" : {"parse" : self.textinput_scan_parameter_2_points.text, "set" : self.textinput_scan_parameter_2_points.setText, "typeof" : str},
            "Lambda1" : {"parse" : self.textinput_scan_parameter_1_lambda.text, "set" : self.textinput_scan_parameter_1_lambda.setText, "typeof" : str},
            "Lambda2" : {"parse" : self.textinput_scan_parameter_2_lambda.text, "set" : self.textinput_scan_parameter_2_lambda.setText, "typeof" : str},
            "DisplayField" : {"parse" : self.text_output_program_qdlc_command_sweep.toPlainText, "set" : self.text_output_program_qdlc_command_sweep.setPlainText, "typeof" : str},
        }
        self.system_components_fields["Detector"] = {}

    def set_fields_from_components(self):
        for cat, content in self.system_components_fields.items():
            for name, struct in content.items():
                print(cat, name)
                print(f"Setting {cat} {name} to {struct['typeof'](self.system_components[cat][name])}")
                struct["set"]( struct["typeof"](self.system_components[cat][name]) )
    
    def set_components_from_fields(self):
        for cat,content in self.system_components_fields.items():
            for name, struct in content.items():
                self.system_components[cat][name] = struct["parse"]()

    def generate_scan_or_sweep(self):
        # Generate scans
        x1,x2 = 0,0
        lambda_str = "x1"
        span1,span2 = (0,0), (0,0)
        self.scan_sweep_values_1,self.scan_sweep_values_2 = None,None
        if self.checkbox_activate_scan_parameter_1.isChecked():
            span1 = (float(self.textinput_scan_parameter_1_from.text()), float(self.textinput_scan_parameter_1_to.text()))
            points = int(self.textinput_scan_parameter_1_points.text())
            x1 = np.linspace(span1[0], span1[1], points, endpoint=True)
        if self.checkbox_activate_scan_parameter_2.isChecked():
            span2 = (float(self.textinput_scan_parameter_2_from.text()), float(self.textinput_scan_parameter_2_to.text()))
            points = int(self.textinput_scan_parameter_2_points.text())
            x2 = np.linspace(span2[0], span2[1], points, endpoint=True)   
        lambda_str_1 = self.textinput_scan_parameter_1_lambda.text()
        lambda_str_2 = self.textinput_scan_parameter_2_lambda.text()
        print(f"Executing scan with x1 in [{np.min(x1)},{np.max(x1)}] and x2 in [{np.min(x2)},{np.max(x2)}] using P1(x1,x2) = {lambda_str_1} and P2(x1,x2) = {lambda_str_2}")
        mgx,mgy = np.meshgrid(x1,x2)
        eval_dict = {"x1" : mgx, 
                     "x2" : mgy, 
                     "np": np, 
                     "g" : get_uv_scaled(self.textinput_rates_cavity_coupling.text()),
                     "G" : get_unit_value(self.textinput_rates_cavity_coupling.text()),
                     "k" : get_uv_scaled(self.textinput_rates_cavity_loss.text()),
                     "K" : get_unit_value(self.textinput_rates_cavity_loss.text()),
                     "y" : get_uv_scaled(self.textinput_rates_radiative_decay.text()),
                     "Y" : get_unit_value(self.textinput_rates_radiative_decay.text()),
                     "d" : get_uv_scaled(self.textinput_rates_pure_dephasing.text()),
                     "D" : get_unit_value(self.textinput_rates_pure_dephasing.text()),
                     "T" : float(self.textinput_phonons_temperature.text()) if self.textinput_phonons_temperature.text() != "No Phonons" else 0,
                     }
        self.scan_sweep_values_1 = eval(lambda_str_1, eval_dict)
        self.scan_sweep_values_2 = eval(lambda_str_2, eval_dict)
        # Plot
        self.plot_sweep_parameter_first.canvas.axes.clear()
        self.plot_sweep_parameter_second.canvas.axes.clear()
        if "x2" in lambda_str_1:
            self.plot_sweep_parameter_first.canvas.axes.pcolormesh(x1, x2, self.scan_sweep_values_1)
        else:
            self.plot_sweep_parameter_first.canvas.axes.plot(x1, self.scan_sweep_values_1[0])
        if "x1" in lambda_str_2:
            self.plot_sweep_parameter_second.canvas.axes.pcolormesh(x1, x2, self.scan_sweep_values_2)
        else:
            self.plot_sweep_parameter_second.canvas.axes.plot(x2, self.scan_sweep_values_2[:,0])
        self.plot_sweep_parameter_first.canvas.draw()
        self.plot_sweep_parameter_second.canvas.draw()



    ###########################################################################################################
    ################################################ Draw #####################################################
    ###########################################################################################################
    def drawSystem(self) -> None:
        self.sort_energy_levels()
        #if self.fixed_energy_h is None:
        self.fixed_energy_x,self.fixed_energy_y,self.fixed_energy_w, self.fixed_energy_h = self.label_output_system.geometry().getCoords()
        x0,y0,w,h = self.fixed_energy_x, self.fixed_energy_y, int(self.fixed_energy_w), int(self.fixed_energy_h) 
        self.output_system_canvas = QPixmap(w, h)
        qp = QPainter(self.output_system_canvas)
        qp.setRenderHint(QPainter.RenderHints.Antialiasing)
        #qp.setRenderHints(qp.Antialiasing)
        self.output_system_canvas.fill( QColor(self.colors["Background"]) )
        if len(self.system_components["EnergyLevels"].keys()) < 2:
            qp.end()
            self.label_output_system.setPixmap(self.output_system_canvas)
            self.update()
            return 
        
        state_color = QColor(self.colors["State"])
        statename_color = QColor(self.colors["StateName"])
        transition_color = QColor(self.colors["Transition"])
        reset_color = QColor(self.colors["Neutral"])

        def draw_rect(_x,_y,_w,_h, name = None, offset_name = (0,0), font_size = 0.8):
            pen = QPen(reset_color)
            pen.setWidth(1)
            qp.setPen(pen)   
            qp.setBrush(state_color)
            #qp.drawRect(int(_x),int(_y),int(_w), int(_h))
            path = QPainterPath()
            path.addRoundedRect(int(_x),int(_y),int(_w), int(_h), int(0.4*_h), int(0.4*_w))
            qp.fillPath(path, state_color)
            qp.drawPath(path)
            if name is not None:
                pen = QPen(statename_color)
                pen.setWidth(2)
                qp.setPen(pen)   
                font = QFont()
                font.setFamily('Times')
                font.setBold(True)
                font.setPointSize(int(font_size*_h))
                qp.setFont(font)
                qp.drawText(int(_x - 12 + offset_name[0]), int(_y+0.9*_h + offset_name[1]), name)

        def draw_line(x1,y1,x2,y2, _w = 8, _color = transition_color, _style = Qt.PenStyle.DotLine):
            pen = QPen(_color)
            pen.setWidth(_w)
            pen.setStyle(_style)
            qp.setPen(pen)   
            qp.drawLine(int(x1),int(y1),int(x2),int(y2))

        def draw_arc(x1,y1,_w,_h,startangle,arcangle, _pw = 2, _color = transition_color):
            pen = QPen(_color)
            pen.setWidth(int(_pw))
            #pen.setStyle(Qt.PenStyle.DotLine)
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)
            qp.setPen(pen)
            qp.drawArc(int(x1),int(y1),int(_w),int(_h),int(startangle),int(arcangle))

        def draw_exp(x1,y1,_w,_h,_lw = 3,_color = transition_color):
            x = np.linspace(-1,1,300)
            xfunc = _w*x
            func = _h*np.exp(-8*x*x)*np.sin(10*np.pi*x)
            for x1,x2,y1,y2 in zip(x1+xfunc,x1+xfunc[1:],y1-func,y1-func[1:]):
                draw_line(int(x1), int(y1), int(x2),int(y2), _w = _lw, _style = Qt.PenStyle.SolidLine, _color = _color)
            

        # Draw Energy Levels from bottom to top
        lowest_energy = 0 if len(self.system_components["EnergyLevels"].keys()) < 1 else min(get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values())
        energy_normalization = max([get_uv_scaled(a["Energy"]) for a in self.system_components["EnergyLevels"].values()]) - lowest_energy
        lowest_level = 0.8*h
        highest_level = 0.2*h
        level_height = (lowest_level - highest_level) * 0.05
        level_width_factor = 0.3
        artificial_y_seperation = 0 # Group members get seperated by this much times the level height at least
        for group_of_levels in self.system_energy_level_groups:
            level_width = max(2,w*level_width_factor if len(group_of_levels) < 2 else 0.6*w/(len(group_of_levels)))
            last_y = lowest_energy
            for l,level in enumerate(group_of_levels,1):
                # X,Y
                y_seperation = 0 
                if abs(last_y - get_uv_scaled(level["Energy"])) / energy_normalization < artificial_y_seperation * level_height: 
                    y_seperation = level_height*artificial_y_seperation*(l-1)
                level_y = lowest_level - (lowest_level - highest_level)*(get_uv_scaled(level["Energy"])-lowest_energy) / energy_normalization - y_seperation
                level_x = w/(len(group_of_levels)+1)*l - level_width/2.# center of individual level - delta/2
                last_y = get_uv_scaled(level["Energy"])
                if self.plot_system_details:
                    name = f"{level['Name']} - E = {level['Energy']}, |{level['DecayScaling']}|{level['DephasingScaling']}|{level['PhononScaling']}|"
                else:
                    name = f"{level['Name']}"
                draw_rect(level_x,level_y,level_width,level_height,name,(0.05*level_width,0) if self.plot_system_details else (0.5*level_width,0))
                # Save Coordinates for easier drawing
                level["Coords"] = (level_x, level_y, level_width, level_height) #x,y,w,h
        # Draw Transitions
        for level in self.system_components["EnergyLevels"].values():
            for t,transto in enumerate(level["CoupledTo"]):
                if transto is None or len(transto) == 0 or transto not in self.system_components["EnergyLevels"]:
                    continue
                level2 = self.system_components["EnergyLevels"][transto]
                if len(level2) == 0:
                    continue
                x1 = level["Coords"][0] + level["Coords"][2]/2.
                y1 = level["Coords"][1] + level["Coords"][3]/2 - level_height
                x2 = level2["Coords"][0] + level2["Coords"][2]/2.
                y2 = level2["Coords"][1] + level2["Coords"][3]/2 + level_height
                draw_line(x1, y1, x2, y2)

        # Draw Cavities
        self.system_cavity_level_groups = [a for a in self.system_components["CavityLevels"].values()]
        for c,cavity in enumerate(self.system_cavity_level_groups):
            cavity_x1 = 0.1*w
            cavity_width = 0.03*w
            cavity_x_delta = 0.04*w
            cavity_strokewidth = 0.011*w
            cavity_x2 = 0.9*w - cavity_width
            cavity_color = QColor(self.colors["Cavity"][c%len(self.colors["Cavity"])])
            # Special Case where cavity is alone:
            if len(cavity["CoupledTo"]) == 0 or None in cavity["CoupledTo"]:
                cavity_y1 = lowest_level
                cavity_height = -get_uv_scaled(cavity["Energy"])/energy_normalization*(lowest_level-highest_level)#-abs(e1[1]-e0[1])
                detuning = 0
                cavity_color.setAlpha(255-int(min(200,10.*detuning/get_uv_scaled(cavity['Energy']))))
                draw_arc(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,90*16,16*180,cavity_strokewidth,cavity_color)
                draw_arc(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,270*16,16*180,cavity_strokewidth,cavity_color)
            else:
                for transition in cavity["CoupledTo"]:
                    t0,t1 = transition.split("=")
                    if t0 not in self.system_components["EnergyLevels"] or t1 not in self.system_components["EnergyLevels"]:
                        if t0 not in self.system_components["CavityLevels"] or t1 not in self.system_components["CavityLevels"]:
                            continue
                    e0,e1 = self.system_components["EnergyLevels"][t0]["Coords"], self.system_components["EnergyLevels"][t1]["Coords"]
                    cavity_y1 = e0[1] + level_height/2
                    cavity_height = -get_uv_scaled(cavity["Energy"])/energy_normalization*(lowest_level-highest_level)#-abs(e1[1]-e0[1])
                    detuning = abs(abs(e0[1]-e1[1]) - abs(cavity_height))
                    cavity_color.setAlpha(255-int(min(200,10.*detuning/get_uv_scaled(cavity['Energy']))))
                    draw_arc(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,90*16,16*180,cavity_strokewidth,cavity_color)
                    draw_arc(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_width, cavity_height,270*16,16*180,cavity_strokewidth,cavity_color)
                    #draw_line(cavity_x1 - c*cavity_x_delta, cavity_y1, cavity_x1 - c*cavity_x_delta, cavity_y1 + cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x1 - c*cavity_x_delta - cavity_width/4, cavity_y1, cavity_x1 - c*cavity_x_delta + cavity_width/4, cavity_y1, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x1 - c*cavity_x_delta - cavity_width/4, cavity_y1+cavity_height, cavity_x1 - c*cavity_x_delta + cavity_width/4, cavity_y1+cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta, cavity_y1, cavity_x2 + c*cavity_x_delta, cavity_y1 + cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta - cavity_width/4, cavity_y1, cavity_x2 + c*cavity_x_delta + cavity_width/4, cavity_y1, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
                    #draw_line(cavity_x2 + c*cavity_x_delta - cavity_width/4, cavity_y1+cavity_height, cavity_x2 + c*cavity_x_delta + cavity_width/4, cavity_y1+cavity_height, _color = cavity_color, _style = Qt.PenStyle.SolidLine)
        
        # Draw Indicator for Pulses
        for i,el in enumerate(list(self.system_components["Pulse"].values())): #+ list(self.system_components["Shift"].values())):
            text = "Pulse: " if el["Name"] in self.system_components["Pulse"] else "Shift: "
            lowest_level = 0.9*h
            highest_level = 0.2*h
            level_height = 0.05
            level_width = 0.1
            #xpos = 0.01 * w
            xpos = 0.01 * w + i*(lowest_level-highest_level)*0.9*level_width*2
            #ypos = lowest_level - i*(lowest_level-highest_level)*0.9*level_height
            ypos = lowest_level
            width = level_width*w
            height = level_height*h
            name = el["Name"]
            transitions = [t.split("=") if "=" in t else t for t in el["CoupledTo"]]
            for transition in transitions:
                if isinstance(transition, list) and len(transition) > 1 and transition[0] in self.system_components["EnergyLevels"] and transition[1] in self.system_components["EnergyLevels"]: # electronic transition
                    e0 = self.system_components["EnergyLevels"][transition[0]]["Coords"]
                    e1 = self.system_components["EnergyLevels"][transition[1]]["Coords"]
                    x1 = e0[0] + e0[2]/2.
                    y1 = e0[1] + e0[3]/2
                    x2 = e1[0] + e1[2]/2.
                    y2 = e1[1] + e1[3]/2
                    x = (x1+x2)/2
                    y = (y1+y2)/2
                    draw_exp(x,y, 100, 50)
        qp.end()

        self.label_output_system.setPixmap(self.output_system_canvas)
        self.update()

    def qdlc_generate_start_command(self, escape_symbol = "'"):
        escaped = self.input_escape_output_command.isChecked()
        # Generate Commands
        commands = [component_parser(component,escaped,self.system_components,escape_symbol=escape_symbol,callback=self.sendHintMessage) for component in self.system_components.keys()]

        final_command = f"[QDLC] {' '.join(commands)} [FILEPATH]"
        return final_command
        #self.output_start_command.setText(final_command)

    def qdlc_start_command_to_real(self, commands = None, escape_symbol = "'") -> str:
        if commands is None:
            commands = self.qdlc_generate_start_command(escape_symbol=escape_symbol)
        executable = self.textinput_file_qdlc.text() or "./QDLC.exe"
        filepath = f"{escape_symbol}{self.textinput_file_destination.text() or self.filepath}{escape_symbol}"
        settingfilepath = f"{escape_symbol}{self.textinput_path_to_settingfile.text() or self.filepath}{escape_symbol}"
        commands = commands.replace("[QDLC]",executable).replace("[FILEPATH]",filepath).replace("[SETTINGFILE]",settingfilepath)
        return commands
        

    def resizeEvent(self, event):
        self.drawSystem()
        QMainWindow.resizeEvent(self, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())