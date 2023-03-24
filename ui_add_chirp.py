# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_chirpbXlbLW.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextBrowser, QWidget)

from plotwidget import PlotWidget

class Ui_AddChirp(object):
    def setupUi(self, AddChirp):
        if not AddChirp.objectName():
            AddChirp.setObjectName(u"AddChirp")
        AddChirp.resize(986, 608)
        AddChirp.setStyleSheet(u"QWidget {background-color: #F3F4F8;}\n"
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
        self.gridLayout = QGridLayout(AddChirp)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(AddChirp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setFrameShape(QFrame.NoFrame)
        self.label_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 5)

        self.label_9 = QLabel(AddChirp)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.textinput_name = QLineEdit(AddChirp)
        self.textinput_name.setObjectName(u"textinput_name")
        self.textinput_name.setMinimumSize(QSize(150, 40))
        font = QFont()
        font.setPointSize(11)
        self.textinput_name.setFont(font)
        self.textinput_name.setFrame(True)
        self.textinput_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_name, 1, 1, 1, 1)

        self.button_load = QPushButton(AddChirp)
        self.button_load.setObjectName(u"button_load")
        self.button_load.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_load, 1, 2, 1, 1)

        self.plot_chirp = PlotWidget(AddChirp)
        self.plot_chirp.setObjectName(u"plot_chirp")
        self.plot_chirp.setMinimumSize(QSize(500, 0))

        self.gridLayout.addWidget(self.plot_chirp, 1, 3, 6, 2)

        self.label_11 = QLabel(AddChirp)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)

        self.textinput_states = QLineEdit(AddChirp)
        self.textinput_states.setObjectName(u"textinput_states")
        self.textinput_states.setMinimumSize(QSize(150, 40))
        self.textinput_states.setFont(font)
        self.textinput_states.setFrame(True)
        self.textinput_states.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_states, 2, 1, 1, 2)

        self.label_13 = QLabel(AddChirp)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_13, 3, 0, 1, 1)

        self.textinput_state_couplings = QLineEdit(AddChirp)
        self.textinput_state_couplings.setObjectName(u"textinput_state_couplings")
        self.textinput_state_couplings.setMinimumSize(QSize(150, 40))
        self.textinput_state_couplings.setFont(font)
        self.textinput_state_couplings.setFrame(True)
        self.textinput_state_couplings.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_state_couplings, 3, 1, 1, 1)

        self.button_setone = QPushButton(AddChirp)
        self.button_setone.setObjectName(u"button_setone")
        self.button_setone.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_setone, 3, 2, 1, 1)

        self.label_12 = QLabel(AddChirp)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.textinput_time = QLineEdit(AddChirp)
        self.textinput_time.setObjectName(u"textinput_time")
        self.textinput_time.setMinimumSize(QSize(150, 40))
        self.textinput_time.setFont(font)
        self.textinput_time.setFrame(True)
        self.textinput_time.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_time, 4, 1, 1, 2)

        self.label_10 = QLabel(AddChirp)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_10, 5, 0, 1, 1)

        self.textinput_energy = QLineEdit(AddChirp)
        self.textinput_energy.setObjectName(u"textinput_energy")
        self.textinput_energy.setMinimumSize(QSize(150, 40))
        self.textinput_energy.setFont(font)
        self.textinput_energy.setFrame(True)
        self.textinput_energy.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_energy, 5, 1, 1, 2)

        self.button_add = QPushButton(AddChirp)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_add, 6, 0, 1, 3)

        self.button_remove_points = QPushButton(AddChirp)
        self.button_remove_points.setObjectName(u"button_remove_points")
        self.button_remove_points.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_remove_points, 7, 0, 1, 3)

        self.label = QLabel(AddChirp)
        self.label.setObjectName(u"label")
        self.label.setLineWidth(1)
        self.label.setWordWrap(True)
        self.label.setMargin(17)

        self.gridLayout.addWidget(self.label, 8, 0, 1, 3)

        self.text_output_list_of_points = QTextBrowser(AddChirp)
        self.text_output_list_of_points.setObjectName(u"text_output_list_of_points")

        self.gridLayout.addWidget(self.text_output_list_of_points, 8, 3, 2, 2)

        self.label_15 = QLabel(AddChirp)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)

        self.textinput_type = QLineEdit(AddChirp)
        self.textinput_type.setObjectName(u"textinput_type")
        self.textinput_type.setMinimumSize(QSize(150, 40))
        self.textinput_type.setFont(font)
        self.textinput_type.setFrame(True)
        self.textinput_type.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_type, 9, 1, 1, 2)

        self.button_confirm = QPushButton(AddChirp)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm, 10, 0, 1, 1)

        self.input_use_timeconfig = QCheckBox(AddChirp)
        self.input_use_timeconfig.setObjectName(u"input_use_timeconfig")
        self.input_use_timeconfig.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setBold(True)
        self.input_use_timeconfig.setFont(font1)
        self.input_use_timeconfig.setChecked(True)

        self.gridLayout.addWidget(self.input_use_timeconfig, 10, 3, 1, 1)

        self.button_plot = QPushButton(AddChirp)
        self.button_plot.setObjectName(u"button_plot")
        self.button_plot.setMinimumSize(QSize(150, 40))
        self.button_plot.setFont(font1)

        self.gridLayout.addWidget(self.button_plot, 10, 4, 1, 1)

        self.button_reset = QPushButton(AddChirp)
        self.button_reset.setObjectName(u"button_reset")
        self.button_reset.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_reset, 10, 2, 1, 1)

        self.button_confirm_replace = QPushButton(AddChirp)
        self.button_confirm_replace.setObjectName(u"button_confirm_replace")
        self.button_confirm_replace.setMinimumSize(QSize(150, 40))

        self.gridLayout.addWidget(self.button_confirm_replace, 10, 1, 1, 1)

        self.label_11.raise_()
        self.label_2.raise_()
        self.textinput_name.raise_()
        self.label_9.raise_()
        self.textinput_energy.raise_()
        self.label_10.raise_()
        self.textinput_states.raise_()
        self.label_12.raise_()
        self.textinput_time.raise_()
        self.label_15.raise_()
        self.textinput_type.raise_()
        self.label.raise_()
        self.button_plot.raise_()
        self.plot_chirp.raise_()
        self.input_use_timeconfig.raise_()
        self.button_load.raise_()
        self.button_add.raise_()
        self.button_remove_points.raise_()
        self.text_output_list_of_points.raise_()
        self.label_13.raise_()
        self.textinput_state_couplings.raise_()
        self.button_setone.raise_()
        self.button_reset.raise_()
        self.button_confirm.raise_()
        self.button_confirm_replace.raise_()

        self.retranslateUi(AddChirp)

        QMetaObject.connectSlotsByName(AddChirp)
    # setupUi

    def retranslateUi(self, AddChirp):
        AddChirp.setWindowTitle(QCoreApplication.translate("AddChirp", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Add Shift</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Name</span></p></body></html>", None))
        self.textinput_name.setText("")
        self.textinput_name.setPlaceholderText(QCoreApplication.translate("AddChirp", u"Name", None))
        self.button_load.setText(QCoreApplication.translate("AddChirp", u"Load", None))
        self.label_11.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupled To</span></p></body></html>", None))
        self.textinput_states.setText("")
        self.textinput_states.setPlaceholderText(QCoreApplication.translate("AddChirp", u"List of States or Cavities", None))
        self.label_13.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Coupling Factors</span></p></body></html>", None))
        self.textinput_state_couplings.setText("")
        self.textinput_state_couplings.setPlaceholderText(QCoreApplication.translate("AddChirp", u"List of Scalings", None))
        self.button_setone.setText(QCoreApplication.translate("AddChirp", u"Set 1", None))
        self.label_12.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time</span></p></body></html>", None))
        self.textinput_time.setText("")
        self.textinput_time.setPlaceholderText(QCoreApplication.translate("AddChirp", u"0", None))
        self.label_10.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Energy</span></p></body></html>", None))
        self.textinput_energy.setText("")
        self.textinput_energy.setPlaceholderText(QCoreApplication.translate("AddChirp", u"0", None))
        self.button_add.setText(QCoreApplication.translate("AddChirp", u"Add Point(s)", None))
        self.button_remove_points.setText(QCoreApplication.translate("AddChirp", u"Remove Point(s)", None))
        self.label.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Add or remove any number of points for the shift. Check the preview and confirm.</span></p><p align=\"center\"><span style=\" font-weight:700;\">TODO: use ListView instead of TextField and use remove points button to remove highlighted points.</span></p></body></html>", None))
        self.text_output_list_of_points.setPlaceholderText(QCoreApplication.translate("AddChirp", u"List of Chirp Tuples ", None))
        self.label_15.setText(QCoreApplication.translate("AddChirp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Type</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_type.setStatusTip(QCoreApplication.translate("AddChirp", u"Can be either of: gauss, sine", None))
#endif // QT_CONFIG(statustip)
        self.textinput_type.setText(QCoreApplication.translate("AddChirp", u"monotone", None))
        self.textinput_type.setPlaceholderText(QCoreApplication.translate("AddChirp", u"gauss or sine", None))
        self.button_confirm.setText(QCoreApplication.translate("AddChirp", u"Save", None))
#if QT_CONFIG(statustip)
        self.input_use_timeconfig.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_use_timeconfig.setText(QCoreApplication.translate("AddChirp", u"Use Timeconfig", None))
        self.button_plot.setText(QCoreApplication.translate("AddChirp", u"Plot", None))
        self.button_reset.setText(QCoreApplication.translate("AddChirp", u"Reset", None))
        self.button_confirm_replace.setText(QCoreApplication.translate("AddChirp", u"Overwrite Original", None))
    # retranslateUi

