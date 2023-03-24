from ui_add_cavity import Ui_AddCavity
from PySide6.QtWidgets import QDialog

class DialogAddCavity(QDialog, Ui_AddCavity):
    def __init__(self, *args, main_window=None, load_existing = None, **kwargs):
        super(DialogAddCavity, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        def finished(replace=False):
            name = self.textinput_name.text()
            energy = self.textinput_energy.text()
            transitions = tuple(self.textinput_transitions.text().split(","))
            transition_scaling = ([a for a in self.textinput_transition_scalings.text().split(",")])
            decay = self.textinput_decay.text()
            photonnumber = self.textinput_photonnumber.text()
            if replace:
                main_window.system_components["CavityLevels"].pop(self.name_when_loaded)
            main_window.addCavity({"Name": name, "Energy": energy, "CoupledTo": transitions, "CoupledToScalings": transition_scaling, "DecayScaling": decay, "PhotonNumber": photonnumber})
            main_window.drawSystem()
        def set_scalings():
            self.textinput_transition_scalings.setText(",".join(["1" for _ in self.textinput_transitions.text().split(",")]))
        def reset():
            for t in [self.textinput_name, self.textinput_energy, self.textinput_transitions, self.textinput_transition_scalings, self.textinput_decay, self.textinput_photonnumber]:
                t.setText("")
        def load():
            level = self.textinput_name.text()
            self.name_when_loaded = level
            if level not in main_window.system_components["CavityLevels"]:
                main_window.sendErrorMessage("No Exist Error","A Cavity with this name does not exist!")
                return
            level = main_window.system_components["CavityLevels"][level]
            self.textinput_energy.setText( level["Energy"] ) 
            self.textinput_transitions.setText( ",".join(level["CoupledTo"]) ) 
            self.textinput_transition_scalings.setText( ",".join(level["CoupledToScalings"]) )
            self.textinput_decay.setText( level["DecayScaling"] ) 
            self.textinput_photonnumber.setText( level["PhotonNumber"] ) 
        self.button_confirm.clicked.connect(finished)
        self.button_confirm_replace.clicked.connect(lambda: finished(replace=True))
        self.button_setone.clicked.connect(set_scalings)
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        if load_existing is not None:
            self.textinput_name.setText(load_existing)
            load()
        self.exec()
        
if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDLC GUI and should be imported, not executed.")