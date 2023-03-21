from ui_add_pulse_wplot import Ui_AddPulse
from PySide6.QtWidgets import QDialog
import numpy as np
from unit_seperator import get_uv_scaled

class DialogAddPulse(QDialog, Ui_AddPulse):
    def __init__(self, *args, main_window=None, **kwargs):
        super(DialogAddPulse, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        def finished():
            name = self.textinput_name.text()
            transitions = tuple(self.textinput_transitions.text().split(","))
            amp = tuple(self.textinput_amp.text().split(","))
            freq = tuple(self.textinput_energy.text().split(","))
            t0 = tuple(self.textinput_center.text().split(","))
            width = tuple(self.textinput_width.text().split(","))
            pulse_type = tuple(self.textinput_type.text().split(","))
            main_window.addPulse({"Name": name, "CoupledTo": transitions, "Amplitudes" : amp, "Frequencies" : freq, "Centers": t0, "Widths": width, "Type" : pulse_type})
            main_window.drawSystem()
        def reset():
            for t in [self.textinput_name, self.textinput_energy, self.textinput_transitions, self.textinput_amp, self.textinput_center, self.textinput_width]:
                t.setText("")
            for t,u in zip([self.textinput_energy_unit, self.textinput_amp_unit, self.textinput_center_unit, self.textinput_width_unit],["eV","pi","ps","ps"]):
                t.setText(u)
            self.textinput_type.setText("")
        def load():
            name = self.textinput_name.text()
            if name not in main_window.system_components["Pulse"]:
                main_window.sendErrorMessage("No Exist Error","A Pulse with this name does not exist!")
                return
            pulse = main_window.system_components["Pulse"][name]
            self.textinput_transitions.setText( ",".join(pulse["CoupledTo"]) )
            self.textinput_amp.setText( ",".join(pulse["Amplitudes"] )) 
            self.textinput_center.setText( ",".join(pulse["Centers"] )) 
            self.textinput_energy.setText( ",".join(pulse["Frequencies"] )) 
            self.textinput_name.setText( pulse["Name"] ) 
            self.textinput_type.setText( ",".join(pulse["Type"]) ) 
            self.textinput_width.setText( ",".join(pulse["Widths"] )) 

        def plot():
            # Get Time From timeconfig if checkbox is checked, else use bare minimum
            widths = [get_uv_scaled(t) for t in self.textinput_width.text().split(",")]
            centers = [get_uv_scaled(t) for t in self.textinput_center.text().split(",")]
            amps = [get_uv_scaled(t) for t in self.textinput_amp.text().split(",")]
            freqs = [get_uv_scaled(t) for t in self.textinput_energy.text().split(",")]
            if self.input_use_timeconfig.isChecked() and main_window.textinput_time_endtime.text() != "auto":
                t0,t1 = get_uv_scaled(main_window.textinput_time_startingtime.text()), get_uv_scaled(main_window.textinput_time_endtime.text())
            else:
                margin = max( widths )
                t0 = min( centers ) - 5*margin
                t1 = max( centers ) + 5*margin
            t = np.linspace(t0,t1,200)
            self.plot_pulse.canvas.axes.clear()
            for (a,f,c,w) in zip( amps, freqs, centers, widths ):
                y = a*np.exp( -(t-c)**2 / w**2 / 2 )
                self.plot_pulse.canvas.axes.plot(t,y)
            #self.plot_pulse.canvas.axes.legend(('cosinus', 'sinus'),loc='upper right')
            #self.plot_pulse.canvas.axes.set_title('Cosinus - Sinus Signals')
            self.plot_pulse.canvas.draw()
        def remove():
            name = self.textinput_name.text()
            if name in main_window.system_components["Pulse"]:
                main_window.system_components["Pulse"].pop(name)
            else:
                main_window.sendErrorMessage("No Exist Error","A Pulse with this name does not exist!")
            main_window.drawSystem()
        self.button_remove.clicked.connect(remove)
        self.button_plot.clicked.connect(plot)
        self.button_confirm.clicked.connect(finished)
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDLC GUI and should be imported, not executed.")