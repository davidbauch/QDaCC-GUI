import sys, os
from PySide6.QtWidgets import QWidget,QMainWindow, QApplication,QLabel, QLineEdit,QTextEdit, QGridLayout, QTextBrowser, QTabWidget, QBoxLayout, QPushButton, QDialog, QFormLayout, QMessageBox
from PySide6.QtGui import QIcon, QAction, QPainter, QColor, QPixmap,QFont, QPen, QPainterPath
from PySide6.QtCore import Qt,QRect,QPropertyAnimation

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

from collections import defaultdict

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
        self.plot_system_details = False
        # System Components that contribute to the execution string
        self.system_components = defaultdict(lambda: {})
        # Hoverable Widgets
        self.system_widgets = {}
        ## Test:
        self.addEnergyLevel({"Name": "G","Energy": "0","CoupledTo": ( "H","V" ),"DecayScaling" : "0","DephasingScaling": "1","PhononScaling": "0"} )
        self.addEnergyLevel({"Name": "H","Energy": f"{1-2E-6}eV","CoupledTo": ( "Z", ),"DecayScaling" : "1","DephasingScaling": "1","PhononScaling": "1"} )
        self.addEnergyLevel({"Name": "V","Energy": f"{1+2E-6}eV","CoupledTo": ( "Z", ),"DecayScaling" : "1","DephasingScaling": "1","PhononScaling": "1"} )
        self.addEnergyLevel({"Name": "Z","Energy": f"{2-3E-3}eV","CoupledTo": tuple( ),"DecayScaling" : "1","DephasingScaling": "1","PhononScaling": "2"} )
        self.addCavity({"Name": "h","Energy": f"{1+1E-3}eV","CoupledTo": ("G=H","H=Z"),"CoupledToScalings": ("1","1"), "PhotonNumber": "2", "DecayScaling": "1"})
        self.addCavity({"Name": "v","Energy": "1eV","CoupledTo": ("G=V","V=Z"),"CoupledToScalings": ("1","1"), "PhotonNumber": "2", "DecayScaling": "1"})
        self.addPulse({"Name": "p", "CoupledTo": ("G=H","H=Z"),"Frequencies": ("1eV","1eV"), "Amplitudes" : ("1pi","1pi"), "Centers" : ("15ps","30ps"), "Widths": ("5ps","5ps"), "Type": ("gauss","gauss")})

        # Cache sizes:
        self.fixed_energy_w, self.fixed_energy_h = None, None

        # Add functionality to buttons
        self.connect_functionality()

        self.show()
        self.drawSystem()

    def connect_functionality(self):
        # "Next" Buttons
        for button in [self.button_next_tab_system_to_config, self.button_next_tab_config_to_timeline, self.button_next_tab_timeline_to_statistics, self.button_next_tab_statistics_to_run, self.button_next_tab_statistics_generate]:
            button.clicked.connect( lambda: self.tabWidget.setCurrentIndex( self.tabWidget.currentIndex() + 1 ) )
        # Add Stuff Dialog
        self.button_add_electronic_state.clicked.connect(lambda: DialogAddElectronic(main_window=self))
        self.button_add_cavity.clicked.connect(lambda: DialogAddCavity(main_window=self))
        self.button_add_optical_pulse.clicked.connect(lambda: DialogAddPulse(main_window=self))
        self.button_add_electronic_shift.clicked.connect(lambda: DialogAddChirp(main_window=self))
        # Modify Stuff
        self.button_modify_clear.clicked.connect(self.clearSystem)
        self.button_input_system_redraw.clicked.connect(self.drawSystem)
        def modify():
            self.plot_system_details = self.input_draw_details.isChecked()
            self.drawSystem()
        self.input_draw_details.clicked.connect(modify)
        def delete_input():
            dialog = InputDialogSmall(main_window=self)
            result = dialog.input.text()
            if len(result) > 0:
                # Find everything that matches the input. ask to delete.
                pass
        self.button_modify_delete.clicked.connect(delete_input)

        # Config Inputs
        self.button_time_config_tol.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Tolerances"))
        self.button_time_config_grid.clicked.connect(lambda: DialogAddGridOrTolerance(main_window=self,name="Grid"))

        # Reset Buttons
        # Reset time parameters
        self.button_reset_timeinput.clicked.connect(lambda: [self.textinput_time_startingtime.setText("0"),self.textinput_time_endtime.setText("auto"),self.textinput_time_timestep.setText("auto"),self.textinput_time_tolerance.setText("1E-6"),self.textinput_time_gridresolution.setText("auto")])
        # Reset solver parameters
        self.button_reset_solver_config.clicked.connect(lambda: [self.input_rungekutta_order.setCurrentIndex(0),self.input_interpolator_t.setCurrentIndex(0),self.input_interpolator_tau.setCurrentIndex(0)])
        # ...

        # Dynamic change stuff
        self.input_phonons_use_qd.stateChanged.connect(lambda: [a.setEnabled(self.input_phonons_use_qd.isChecked()) for a in [self.textinput_phonons_sd_qd_de,self.textinput_phonons_sd_qd_dh,self.textinput_phonons_sd_qd_rho,self.textinput_phonons_sd_qd_cs,self.textinput_phonons_sd_qd_aeah_ratio,self.textinput_phonons_sd_qd_size]])

        # Run
        def generate_command():
            print(self.system_components)
            self.parseConfig()
            command = self.generateQDLCStartCommand()
            self.text_output_program_qdlc_command.setText(command)
            print(command)
        self.button_generate_run.clicked.connect(generate_command)

    def sendMessage(self, bar: str, title: str, message: str):
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Critical)
        msg.setText(title)
        msg.setInformativeText(message)
        msg.setWindowTitle(bar)
        msg.exec()
    def sendErrorMessage(self, error: str, message: str):
        self.sendMessage("Error!",error,message)
    def sendWarningMessage(self, warning: str, message: str):
        self.sendMessage("Warning!",warning,message)
    def sendHintMessage(self, message: str):
        self.sendMessage("Attention!","Attention!",message)

    def clearSystem(self):
        self.system_components["EnergyLevels"] = {}
        self.system_energy_level_groups = list()
        self.system_components["CavityLevels"] = {}
        self.system_cavity_level_groups = list()
        self.system_components["Pulse"] = {}
        self.system_components["Shift"] = {}
        self.drawSystem()

    def sort_energy_levels(self, group_threshold: float = 0.05) -> None:
        levels = [a for a in self.system_components["EnergyLevels"].values()]
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
    def add_generic(self, category: str, struct: dict) -> None:
        name = struct["Name"]
        changed = "Added" if name not in self.system_components[category] else "Replaced"
        self.system_components[category][name] = struct
        print(changed, self.system_components[category][name])

    def addEnergyLevel(self, p: dict ):
        self.add_generic( "EnergyLevels", p )
        
    def addCavity(self, p: dict):
        self.add_generic( "CavityLevels", p )

    def addPulse(self, p: dict):
        # Confirm that Pulse sizes are the same:
        a,f,c,w,t = len(p["Amplitudes"]), len(p["Frequencies"]), len(p["Centers"]), len(p["Widths"]), len(p["Type"])
        if not (a==f and f==c and c==w and w==t):
            self.sendErrorMessage("Wrong Pulse Dimensions", "The arrays you entered for the Pulse parameters must be of equal length!")
            return
        self.add_generic( "Pulse", p )
        
    def addShift(self, p: dict):
        self.add_generic( "Shift", p )
    
    # Parses All configs from always-on entries like time, solver, etc.
    def parseConfig(self):
        # Time
        self.system_components["ConfigTime"] = {
            "Start" : self.textinput_time_startingtime.text(),
            "End" : self.textinput_time_endtime.text(),
            "Step" : self.textinput_time_timestep.text()
        }
        # Grids
        self.system_components["ConfigGrid"]["Resolution"] = self.textinput_time_gridresolution.text()
        self.system_components["ConfigTolerances"]["Resolution"] = self.textinput_time_tolerance.text()
        # Solver and Interpolator
        self.system_components["ConfigSolver"]["Solver"] = self.input_rungekutta_order.currentIndex()
        self.system_components["ConfigSolver"]["Interpolator"] = self.input_interpolator_t.currentText()
        self.system_components["ConfigSolver"]["InterpolatorGrid"] = self.input_interpolator_tau.currentText()
        # System Parameters
        self.system_components["ConfigSystem"]["Coupling"] = self.textinput_rates_cavity_coupling.text()
        self.system_components["ConfigSystem"]["CavityLosses"] = self.textinput_rates_cavity_loss.text()
        self.system_components["ConfigSystem"]["RadiativeLosses"] = self.textinput_rates_radiative_decay.text()
        self.system_components["ConfigSystem"]["DephasingLosses"] = self.textinput_rates_pure_dephasing.text()
        # Phonons
        self.system_components["ConfigPhonons"]["Temperature"] = self.textinput_phonons_temperature.text()
        self.system_components["ConfigPhonons"]["IteratorStep"] = self.textinput_phonons_iterator_stepsize.text()
        self.system_components["ConfigPhonons"]["Approximation"] = self.input_phonons_approximation.currentIndex()
        self.system_components["ConfigPhonons"]["ARRad"] = self.input_phonons_adjust_radiativeloss.isChecked()
        self.system_components["ConfigPhonons"]["ARDep"] = self.input_phonons_adjust_pure_dephasing.isChecked()
        self.system_components["ConfigPhonons"]["Renormalization"] = self.input_phonons_adjust_renormalization.isChecked()
        ## Phonon Parameters
        self.system_components["ConfigPhonons"]["Alpha"] = self.textinput_phonons_sd_alpha.text()
        self.system_components["ConfigPhonons"]["SpectralCutoff"] = self.textinput_phonons_sd_wcutoff.text()
        self.system_components["ConfigPhonons"]["SpectralDelta"] = self.textinput_phonons_sd_wdelta.text()
        self.system_components["ConfigPhonons"]["TimeCutoff"] = self.textinput_phonons_sd_tcutoff.text()
        self.system_components["ConfigPhonons"]["Ohm"] = self.textinput_phonons_sd_ohmamp.text()
        ## Phonon QD
        self.system_components["ConfigPhonons"]["UseQD"] = self.input_phonons_use_qd.isChecked()
        self.system_components["ConfigPhonons"]["QDde"] = self.textinput_phonons_sd_qd_de.text()
        self.system_components["ConfigPhonons"]["QDdh"] = self.textinput_phonons_sd_qd_dh.text()
        self.system_components["ConfigPhonons"]["QDrho"] = self.textinput_phonons_sd_qd_rho.text()
        self.system_components["ConfigPhonons"]["QDcs"] = self.textinput_phonons_sd_qd_cs.text()
        self.system_components["ConfigPhonons"]["QDeh"] = self.textinput_phonons_sd_qd_aeah_ratio.text()
        self.system_components["ConfigPhonons"]["QDs"] = self.textinput_phonons_sd_qd_size.text()

    ###########################################################################################################
    ################################################ Draw #####################################################
    ###########################################################################################################
    def drawSystem(self) -> None:
        self.sort_energy_levels()
        if self.fixed_energy_h is None:
            self.fixed_energy_x,self.fixed_energy_y,self.fixed_energy_w, self.fixed_energy_h = self.label_output_system.geometry().getCoords()
        x0,y0,w,h = self.fixed_energy_x, self.fixed_energy_y, self.fixed_energy_w, self.fixed_energy_h 
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
        # Draw Indicator for Pulse and chirp
        for i,el in enumerate(list(self.system_components["Pulse"].values()) + list(self.system_components["Shift"].values())):
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
            draw_rect(xpos,ypos,width,height,f"{text}{name}",font_size = 0.5,offset_name=(0.25*width,-0.25*height))
        qp.end()

        self.label_output_system.setPixmap(self.output_system_canvas)
        self.update()

    def generateQDLCStartCommand(self):
        self.executable = "./QDLC.exe"
        self.filepath = "data/test/"

        escaped = self.input_escape_output_command.isChecked()

        # Generate Commands
        commands = [component_parser(component,escaped,self.system_components,callback=self.sendHintMessage) for component in self.system_components.keys()]

        final_command = f"{self.executable} {' '.join(commands)} {self.filepath}"
        return final_command
        #self.output_start_command.setText(final_command)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())