# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_cavityhxnXIR.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddCavity(object):
    def setupUi(self, AddCavity):
        if not AddCavity.objectName():
            AddCavity.setObjectName(u"AddCavity")
        AddCavity.resize(480, 416)
        AddCavity.setStyleSheet(u"QWidget {background-color: #F3F4F8;}\n"
"\n"
"QPushButton {background-color: #88282A3A;  color: #FFFFFF; border-radius: 8px;  font-weight: bold; font-size: 16px; }\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #D2D4DA, stop:0.91 #88282A3A);}\n"
"QPushButton[objectName^=\"button_next_tab\"] {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4501e, stop:0.91 #8d2f13);  color: #FFFFFF; border-radius: 8px; }\n"
"QPushButton[objectName^=\"button_next_tab\"]::hover {background-color: #aaf4501e; transition: 2.5s;}\n"
"\n"
"QTextEdit {background-color: #D2D4DA;}\n"
"QTextEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QLabel {background-color: #282A3A; border-radius: 8px; color: #FFFFFF;}\n"
"QLabel[objectName^=\"label_title\"] {background-color: #44282A3A; border-radius: 8px; color: #000000; border-bottom-right-radius: 0; border-bottom-left-radius: 0; border-bottom-width: 2px; border-bottom-color: #000000;}\n"
"QLabel[objectName^=\"label_output\"] {backgr"
                        "ound-color: #44282A3A; border-radius: 8px; color: #000000; border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"QLabel[objectName^=\"label_plot\"] {background-color: #44282A3A; border-radius: 8px; color: #000000;  border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"\n"
"QLineEdit {border-radius: 8px;background-color: #D2D4DA; }\n"
"QLineEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QComboBox {border-radius: 8px; background-color: #D2D4DA;  padding-left: 10% }\n"
"QComboBox::hover {background-color: #D2D4DA}\n"
"\n"
"QCheckBox {background-color: #D2D4DA;border-radius: 8px; padding-left:10% }\n"
"QCheckBox::hover {background-color: #D2D4DA}\n"
"\n"
"QTextBrowser {background-color: #D2D4DA; }\n"
"QTextBrowser[objectName^=\"text_output\"] {background-color: #44282A3A; border-radius: 8px; color: #000000; }\n"
"\n"
"QTabWidget::tab-bar {   border: 0px solid #282A3A;}\n"
"QTabBar::tab {  background-color: #88282A3A;  color: white;  padding-left: 10px; padding-right:10px; padding-bottom: 10px; padd"
                        "ing-top: 5px; font-weight: bold;}\n"
"QTabBar::tab:selected { background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #282A3A, stop:0.91 #88282A3A); padding-right:50px; padding-left:50px; border-width: 2px; border-color: black}\n"
"\n"
"QScrollBar::handle:vertical {background-color: #282A3A; min-height: 30px;max-height: 20%;border-radius: 7px; margin: 0}\n"
"QScrollBar::handle:vertical:hover{background-color: #88282A3A;}\n"
"QScrollBar::handle:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::sub-line:vertical {border: none;background-color: #f4501e;height: 15px;border-top-left-radius: 7px;border-top-right-radius: 7px;subcontrol-position: top;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::sub-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::sub-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::add-line:vertical {border: none;background-color: #f4501e;height: 15px;border-bottom-left-radius: 7px;border-bottom-right-radius: 7px;subcontrol-position: "
                        "bottom;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::add-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::add-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {background: none;}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}")
        self.gridLayout = QGridLayout(AddCavity)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddCavity)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.label_9 = QLabel(AddCavity)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.textinput_name = QLineEdit(AddCavity)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 1, 1, 1)

        self.button_load = QPushButton(AddCavity)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 2, 1, 1)

        self.label_10 = QLabel(AddCavity)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.textinput_energy = QLineEdit(AddCavity)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 2, 1, 1, 2)

        self.label_11 = QLabel(AddCavity)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.textinput_transitions = QLineEdit(AddCavity)
        self.textinput_transitions.setObjectName(u"textinput_transitions")
        self.textinput_transitions.setMinimumSize(QSize(150, 40))
        self.textinput_transitions.setFont(font)
        self.textinput_transitions.setFrame(True)
        self.textinput_transitions.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transitions, 3, 1, 1, 2)

        self.label_12 = QLabel(AddCavity)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.textinput_transition_scalings = QLineEdit(AddCavity)
        self.textinput_transition_scalings.setObjectName(u"textinput_transition_scalings")
        self.textinput_transition_scalings.setMinimumSize(QSize(150, 40))
        self.textinput_transition_scalings.setFont(font)
        self.textinput_transition_scalings.setFrame(True)
        self.textinput_transition_scalings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transition_scalings, 4, 1, 1, 1)

        self.button_setone = QPushButton(AddCavity)
        self.button_setone.setObjectName(u"button_setone")
        self.button_setone.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setone, 4, 2, 1, 1)

        self.label_13 = QLabel(AddCavity)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)

        self.textinput_decay = QLineEdit(AddCavity)
        self.textinput_decay.setObjectName(u"textinput_decay")
        self.textinput_decay.setMinimumSize(QSize(150, 40))
        self.textinput_decay.setFont(font)
        self.textinput_decay.setFrame(True)
        self.textinput_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_decay, 5, 1, 1, 2)

        self.label_14 = QLabel(AddCavity)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_14, 6, 0, 1, 1)

        self.textinput_photonnumber = QLineEdit(AddCavity)
        self.textinput_photonnumber.setObjectName(u"textinput_photonnumber")
        self.textinput_photonnumber.setMinimumSize(QSize(150, 40))
        self.textinput_photonnumber.setFont(font)
        self.textinput_photonnumber.setFrame(True)
        self.textinput_photonnumber.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_photonnumber, 6, 1, 1, 2)

        self.button_confirm = QPushButton(AddCavity)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 7, 0, 1, 1)

        self.button_reset = QPushButton(AddCavity)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 7, 2, 1, 1)

        self.button_confirm_replace = QPushButton(AddCavity)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 7, 1, 1, 1)

        self.label_11.raise_()
        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_transitions.raise_()
        self.button_confirm.raise_()
        self.button_reset.raise_()
        self.textinput_transition_scalings.raise_()
        self.label_13.raise_()
        self.textinput_decay.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.textinput_photonnumber.raise_()
        self.button_setone.raise_()
        self.button_load.raise_()
        self.button_confirm_replace.raise_()

        self.retranslateUi(AddCavity)

        QMetaObject.connectSlotsByName(AddCavity)
    # setupUi

    def retranslateUi(self, AddCavity):
        AddCavity.setWindowTitle(QCoreApplication.translate("AddCavity", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Optical Cavity</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddCavity", u"Name", None))
        self.button_load.setText(QCoreApplication.translate("AddCavity", u"Load", None))
        self.label_10.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Energy</span></p></body></html>", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddCavity", u"0", None))
        self.label_11.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupled To</span></p></body></html>", None))
        self.textinput_transitions.setText("")
        self.textinput_transitions.setPlaceholderText(QCoreApplication.translate("AddCavity", u"List of Transitions", None))
        self.label_12.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Scaling</span></p></body></html>", None))
        self.textinput_transition_scalings.setText("")
        self.textinput_transition_scalings.setPlaceholderText(QCoreApplication.translate("AddCavity", u"List of Scalings", None))
        self.button_setone.setText(QCoreApplication.translate("AddCavity", u"Set 1", None))
        self.label_13.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Decay Scaling</span></p></body></html>", None))
        self.textinput_decay.setText(QCoreApplication.translate("AddCavity", u"1", None))
        self.textinput_decay.setPlaceholderText(QCoreApplication.translate("AddCavity", u"1", None))
        self.label_14.setText(QCoreApplication.translate("AddCavity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Photon Number</span></p></body></html>", None))
        self.textinput_photonnumber.setText("")
        self.textinput_photonnumber.setPlaceholderText(QCoreApplication.translate("AddCavity", u"Maximum Photons", None))
        self.button_confirm.setText(QCoreApplication.translate("AddCavity", u"Save", None))
        self.button_reset.setText(QCoreApplication.translate("AddCavity", u"Reset", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddCavity", u"Overwrite Original", None))
    # retranslateUi

