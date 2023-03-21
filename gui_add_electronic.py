from ui_add_electronic import Ui_AddElectronic
from PySide6.QtWidgets import QDialog

class DialogAddElectronic(QDialog, Ui_AddElectronic):
    def __init__(self, *args, main_window=None, **kwargs):
        super(DialogAddElectronic, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.retranslateUi(self)
        def add():
            name = self.textinput_name.text()
            energy = self.textinput_energy.text()
            transitions = tuple(a for a in self.textinput_transitions.text().split(",") if len(a) > 0)
            decay = self.textinput_decay.text()
            dephasing = self.textinput_dephasing.text()
            phonons = self.textinput_phonons.text()
            main_window.addEnergyLevel({"Name": name, "Energy": energy, "CoupledTo": transitions, "DephasingScaling": dephasing, "DecayScaling": decay, "PhononScaling": phonons})
            main_window.drawSystem()
        def set_scalings(a: str, b: str, c: str):
            for t,m in zip([self.textinput_dephasing ,self.textinput_phonons, self.textinput_decay],[a,b,c]):
                t.setText(m)
        def reset():
            for t in [self.textinput_name, self.textinput_energy, self.textinput_transitions, self.textinput_decay, self.textinput_dephasing, self.textinput_phonons]:
                t.setText("")
            self.textinput_energy_unit.setText("eV")
        def load():
            level = self.textinput_name.text()
            if level not in main_window.system_components["EnergyLevels"]:
                main_window.sendErrorMessage("No Exist Error","An Electronic State with this name does not exist!")
                return
            level = main_window.system_components["EnergyLevels"][level]
            self.textinput_energy.setText( level["Energy"] )
            self.textinput_transitions.setText( ",".join(level["CoupledTo"]) )
            self.textinput_dephasing.setText( level["DephasingScaling"] )
            self.textinput_decay.setText( level["DecayScaling"] )
            self.textinput_phonons.setText( level["PhononScaling"] )
        def remove():
            name = self.textinput_name.text()
            if name in main_window.system_components["EnergyLevels"]:
                main_window.system_components["EnergyLevels"].pop(name)
            else:
                main_window.sendErrorMessage("No Exist Error","An Electronic State with this name does not exist!")
            main_window.drawSystem()
        self.button_remove.clicked.connect(remove)
        self.button_confirm.clicked.connect(add)
        self.button_setzero.clicked.connect(lambda: set_scalings("1","0","0"))
        self.button_setone.clicked.connect(lambda: set_scalings("1","1","1"))
        self.button_reset.clicked.connect(reset)
        self.button_load.clicked.connect(load)
        self.exec()

if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDLC GUI and should be imported, not executed.")