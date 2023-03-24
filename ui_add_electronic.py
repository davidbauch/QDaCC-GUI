# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_electronicRZPGIE.ui'
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

class Ui_AddElectronic(object):
    def setupUi(self, AddElectronic):
        if not AddElectronic.objectName():
            AddElectronic.setObjectName(u"AddElectronic")
        AddElectronic.resize(648, 412)
        AddElectronic.setStyleSheet(u"QWidget {background-color: #F3F4F8;}\n"
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
        self.gridLayout = QGridLayout(AddElectronic)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_11 = QLabel(AddElectronic)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 2)

        self.textinput_decay = QLineEdit(AddElectronic)
        self.textinput_decay.setObjectName(u"textinput_decay")
        self.textinput_decay.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_decay.setFont(font)
        self.textinput_decay.setFrame(True)
        self.textinput_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_decay, 5, 0, 1, 1)

        self.title = QLabel(AddElectronic)
        self.title.setObjectName(u"title")
        self.title.setMaximumSize(QSize(16777215, 40))
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 6)

        self.label_12 = QLabel(AddElectronic)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 2)

        self.button_confirm = QPushButton(AddElectronic)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 8, 0, 1, 2)

        self.label_10 = QLabel(AddElectronic)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 2)

        self.label_9 = QLabel(AddElectronic)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 2)

        self.button_setzero = QPushButton(AddElectronic)
        self.button_setzero.setObjectName(u"button_setzero")
        self.button_setzero.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setzero, 4, 2, 1, 2)

        self.button_confirm_replace = QPushButton(AddElectronic)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 8, 2, 1, 1)

        self.textinput_dephasing = QLineEdit(AddElectronic)
        self.textinput_dephasing.setObjectName(u"textinput_dephasing")
        self.textinput_dephasing.setMinimumSize(QSize(150, 40))
        self.textinput_dephasing.setFont(font)
        self.textinput_dephasing.setFrame(True)
        self.textinput_dephasing.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_dephasing, 5, 2, 1, 1)

        self.textinput_phonons = QLineEdit(AddElectronic)
        self.textinput_phonons.setObjectName(u"textinput_phonons")
        self.textinput_phonons.setMinimumSize(QSize(150, 40))
        self.textinput_phonons.setFont(font)
        self.textinput_phonons.setFrame(True)
        self.textinput_phonons.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_phonons, 5, 4, 1, 1)

        self.button_setone = QPushButton(AddElectronic)
        self.button_setone.setObjectName(u"button_setone")
        self.button_setone.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setone, 4, 4, 1, 1)

        self.button_reset = QPushButton(AddElectronic)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 8, 4, 1, 1)

        self.textinput_transitions = QLineEdit(AddElectronic)
        self.textinput_transitions.setObjectName(u"textinput_transitions")
        self.textinput_transitions.setMinimumSize(QSize(150, 40))
        self.textinput_transitions.setFont(font)
        self.textinput_transitions.setFrame(True)
        self.textinput_transitions.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_transitions, 3, 2, 1, 3)

        self.textinput_name = QLineEdit(AddElectronic)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 2, 1, 2)

        self.textinput_energy = QLineEdit(AddElectronic)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 2, 2, 1, 3)

        self.button_load = QPushButton(AddElectronic)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 4, 1, 1)

        self.label_12.raise_()
        self.title.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.textinput_transitions.raise_()
        self.textinput_decay.raise_()
        self.button_setone.raise_()
        self.button_setzero.raise_()
        self.button_reset.raise_()
        self.button_confirm.raise_()
        self.button_confirm_replace.raise_()
        self.textinput_dephasing.raise_()
        self.textinput_phonons.raise_()
        self.button_load.raise_()

        self.retranslateUi(AddElectronic)

        QMetaObject.connectSlotsByName(AddElectronic)
    # setupUi

    def retranslateUi(self, AddElectronic):
        AddElectronic.setWindowTitle(QCoreApplication.translate("AddElectronic", u"Dialog", None))
        self.label_11.setText(QCoreApplication.translate("AddElectronic", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupled To</span></p></body></html>", None))
        self.textinput_decay.setText("")
        self.textinput_decay.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"Decay", None))
        self.title.setText(QCoreApplication.translate("AddElectronic", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Electronic State</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("AddElectronic", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Scalings</span></p></body></html>", None))
        self.button_confirm.setText(QCoreApplication.translate("AddElectronic", u"Save", None))
        self.label_10.setText(QCoreApplication.translate("AddElectronic", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Energy</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AddElectronic", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.button_setzero.setText(QCoreApplication.translate("AddElectronic", u"Set Zero", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddElectronic", u"Overwrite Original", None))
        self.textinput_dephasing.setText("")
        self.textinput_dephasing.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"Dephasing", None))
        self.textinput_phonons.setText("")
        self.textinput_phonons.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"Phonons", None))
        self.button_setone.setText(QCoreApplication.translate("AddElectronic", u"Set One", None))
        self.button_reset.setText(QCoreApplication.translate("AddElectronic", u"Reset", None))
        self.textinput_transitions.setText("")
        self.textinput_transitions.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"List of Transitions", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"Name", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddElectronic", u"0", None))
#if QT_CONFIG(tooltip)
        self.button_load.setToolTip(QCoreApplication.translate("AddElectronic", u"Load an existing Level and overwrite it's properties.", None))
#endif // QT_CONFIG(tooltip)
        self.button_load.setText(QCoreApplication.translate("AddElectronic", u"Load", None))
    # retranslateUi

