# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowcSRsCQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextBrowser,
    QWidget)

from plotwidget import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1455, 946)
        MainWindow.setStyleSheet(u"QWidget {background-color: #F3F4F8;}\n"
"\n"
"QListView{border-radius: 3px; background-color: #D2D4DA; }\n"
"\n"
"QPushButton {background-color: #88282A3A;  color: #FFFFFF; border-radius: 3px;  font-weight: bold; font-size: 16px; }\n"
"QPushButton::hover {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #D2D4DA, stop:0.91 #88282A3A);}\n"
"QPushButton[objectName^=\"button_next_tab\"] {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4501e, stop:0.91 #8d2f13);  color: #FFFFFF; border-radius: 3px; }\n"
"QPushButton[objectName^=\"button_next_tab\"]::hover {background-color: #aaf4501e;}\n"
"\n"
"QTextEdit {background-color: #D2D4DA;}\n"
"QTextEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QLabel {background-color: #282A3A; border-radius: 3px; color: #FFFFFF;}\n"
"QLabel[objectName^=\"label_title\"] {background-color: #44282A3A; border-radius: 3px; color: #000000; border-bottom-right-radius: 0; border-bottom-left-radius: 0; border-bottom-width: 2px; border-bottom-color: #000000;"
                        "}\n"
"QLabel[objectName^=\"label_output\"] {background-color: #44282A3A; border-radius: 3px; color: #000000; border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"QLabel[objectName^=\"label_plot\"] {background-color: #44282A3A; border-radius: 3px; color: #000000;  border-top-right-radius: 0; border-top-left-radius: 0; }\n"
"\n"
"QLineEdit {border-radius: 3px;background-color: #D2D4DA; }\n"
"QLineEdit::hover {background-color: #D2D4DA}\n"
"\n"
"QComboBox {border-radius: 3px; background-color: #D2D4DA;  padding-left: 10% }\n"
"QComboBox::hover {background-color: #D2D4DA}\n"
"\n"
"QCheckBox {background-color: #D2D4DA;border-radius: 3px; padding-left:10% }\n"
"QCheckBox::hover {background-color: #D2D4DA}\n"
"\n"
"QTextBrowser {background-color: #D2D4DA; }\n"
"QTextBrowser[objectName^=\"text_output\"] {background-color: #44282A3A; border-radius: 3px; color: #000000; }\n"
"\n"
"QTabWidget::tab-bar {   border: 0px solid #282A3A;}\n"
"QTabBar::tab {  background-color: #88282A3A;  color: white;  padding-left: 10"
                        "px; padding-right:10px; padding-bottom: 10px; padding-top: 5px; font-weight: bold;}\n"
"QTabBar::tab:selected { background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #282A3A, stop:0.91 #88282A3A); padding-right:50px; padding-left:50px; border-width: 2px; border-color: black}\n"
"\n"
"QListView::item {background:#D2D4DA; border-right-width:3px; border-color: #282A3A; padding: 5%;}\n"
"QListView::item:selected:!active {background:#D2D4DA; border-right-width:3px; border-color: #aaf4501e;}\n"
"QListView::item:selected:active {background: #88282A3A; border-right-width:3px; border-color: #aaf4501e;}\n"
"QListView::item:hover {background: #D2D4DA; }\n"
"QComboBox::down-arrow {background-color: #88282A3A; min-height: 40px; border-top-right-radius: 3px; border-bottom-right-radius: 3px;}\n"
"QComboBox::drop-down {border: 0px;}\n"
"\n"
"QScrollBar::handle:vertical {background-color: #282A3A; min-height: 30px;max-height: 20%;border-radius: 7px; margin: 0}\n"
"QScrollBar::handle:vertical:hover{background-color:"
                        " #88282A3A;}\n"
"QScrollBar::handle:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::sub-line:vertical {border: none;background-color: #f4501e;height: 15px;border-top-left-radius: 7px;border-top-right-radius: 7px;subcontrol-position: top;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::sub-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::sub-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::add-line:vertical {border: none;background-color: #f4501e;height: 15px;border-bottom-left-radius: 7px;border-bottom-right-radius: 7px;subcontrol-position: bottom;subcontrol-origin: 0;max-height: 20%;}\n"
"QScrollBar::add-line:vertical:hover {background-color: #88282A3A;}\n"
"QScrollBar::add-line:vertical:pressed {background-color: #f4501e;}\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {background: none;}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {background: none;}")
        self.actionLoad_QDLC_Command = QAction(MainWindow)
        self.actionLoad_QDLC_Command.setObjectName(u"actionLoad_QDLC_Command")
        self.actionExport_QDLC_Command = QAction(MainWindow)
        self.actionExport_QDLC_Command.setObjectName(u"actionExport_QDLC_Command")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_11 = QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab_system = QWidget()
        self.tab_system.setObjectName(u"tab_system")
        self.gridLayout_2 = QGridLayout(self.tab_system)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_add_cavity = QPushButton(self.tab_system)
        self.button_add_cavity.setObjectName(u"button_add_cavity")
        self.button_add_cavity.setMinimumSize(QSize(200, 40))
        self.button_add_cavity.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_cavity, 4, 2, 1, 1)

        self.button_input_system_redraw = QPushButton(self.tab_system)
        self.button_input_system_redraw.setObjectName(u"button_input_system_redraw")
        self.button_input_system_redraw.setMinimumSize(QSize(200, 40))
        self.button_input_system_redraw.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setBold(True)
        self.button_input_system_redraw.setFont(font)

        self.gridLayout_2.addWidget(self.button_input_system_redraw, 12, 2, 1, 1)

        self.button_modify_edit = QPushButton(self.tab_system)
        self.button_modify_edit.setObjectName(u"button_modify_edit")
        self.button_modify_edit.setMinimumSize(QSize(200, 40))
        self.button_modify_edit.setMaximumSize(QSize(200, 40))
        self.button_modify_edit.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_edit, 9, 2, 1, 1)

        self.button_modify_delete = QPushButton(self.tab_system)
        self.button_modify_delete.setObjectName(u"button_modify_delete")
        self.button_modify_delete.setMinimumSize(QSize(200, 40))
        self.button_modify_delete.setMaximumSize(QSize(200, 40))
        self.button_modify_delete.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_delete, 10, 2, 1, 1)

        self.button_modify_clear = QPushButton(self.tab_system)
        self.button_modify_clear.setObjectName(u"button_modify_clear")
        self.button_modify_clear.setMinimumSize(QSize(200, 40))
        self.button_modify_clear.setMaximumSize(QSize(200, 40))
        self.button_modify_clear.setFlat(False)

        self.gridLayout_2.addWidget(self.button_modify_clear, 11, 2, 1, 1)

        self.button_add_electronic_shift = QPushButton(self.tab_system)
        self.button_add_electronic_shift.setObjectName(u"button_add_electronic_shift")
        self.button_add_electronic_shift.setMinimumSize(QSize(200, 40))
        self.button_add_electronic_shift.setMaximumSize(QSize(200, 40))
        self.button_add_electronic_shift.setMouseTracking(True)

        self.gridLayout_2.addWidget(self.button_add_electronic_shift, 6, 2, 1, 1)

        self.input_draw_details = QCheckBox(self.tab_system)
        self.input_draw_details.setObjectName(u"input_draw_details")
        self.input_draw_details.setMinimumSize(QSize(200, 40))
        self.input_draw_details.setMaximumSize(QSize(200, 40))
        self.input_draw_details.setChecked(False)

        self.gridLayout_2.addWidget(self.input_draw_details, 13, 2, 1, 1)

        self.label_5 = QLabel(self.tab_system)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(200, 40))
        self.label_5.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)

        self.label_6 = QLabel(self.tab_system)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(200, 40))
        self.label_6.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.label_6, 8, 2, 1, 1)

        self.label_output_system = QLabel(self.tab_system)
        self.label_output_system.setObjectName(u"label_output_system")
        self.label_output_system.setMinimumSize(QSize(1000, 800))
        self.label_output_system.setAcceptDrops(True)
        self.label_output_system.setFrameShape(QFrame.NoFrame)
        self.label_output_system.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_output_system, 1, 0, 14, 1)

        self.button_add_optical_pulse = QPushButton(self.tab_system)
        self.button_add_optical_pulse.setObjectName(u"button_add_optical_pulse")
        self.button_add_optical_pulse.setMinimumSize(QSize(200, 40))
        self.button_add_optical_pulse.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_optical_pulse, 5, 2, 1, 1)

        self.label_title_qdsystem = QLabel(self.tab_system)
        self.label_title_qdsystem.setObjectName(u"label_title_qdsystem")
        self.label_title_qdsystem.setMinimumSize(QSize(200, 40))
        self.label_title_qdsystem.setMaximumSize(QSize(16777215, 40))
        self.label_title_qdsystem.setFrameShape(QFrame.NoFrame)
        self.label_title_qdsystem.setFrameShadow(QFrame.Plain)

        self.gridLayout_2.addWidget(self.label_title_qdsystem, 1, 2, 1, 1)

        self.button_next_tab_system_to_config = QPushButton(self.tab_system)
        self.button_next_tab_system_to_config.setObjectName(u"button_next_tab_system_to_config")
        self.button_next_tab_system_to_config.setMinimumSize(QSize(200, 40))
        self.button_next_tab_system_to_config.setMaximumSize(QSize(200, 40))
        self.button_next_tab_system_to_config.setCheckable(False)

        self.gridLayout_2.addWidget(self.button_next_tab_system_to_config, 14, 2, 1, 1)

        self.button_add_electronic_state = QPushButton(self.tab_system)
        self.button_add_electronic_state.setObjectName(u"button_add_electronic_state")
        self.button_add_electronic_state.setMinimumSize(QSize(200, 40))
        self.button_add_electronic_state.setMaximumSize(QSize(200, 40))

        self.gridLayout_2.addWidget(self.button_add_electronic_state, 3, 2, 1, 1)

        self.list_components = QListView(self.tab_system)
        self.list_components.setObjectName(u"list_components")
        self.list_components.setMinimumSize(QSize(200, 200))
        self.list_components.setMaximumSize(QSize(200, 16777215))
        self.list_components.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_components.setDefaultDropAction(Qt.IgnoreAction)

        self.gridLayout_2.addWidget(self.list_components, 7, 2, 1, 1)

        self.tabWidget.addTab(self.tab_system, "")
        self.tab_environment = QWidget()
        self.tab_environment.setObjectName(u"tab_environment")
        self.gridLayout_3 = QGridLayout(self.tab_environment)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.button_reset_phonon_sd = QPushButton(self.tab_environment)
        self.button_reset_phonon_sd.setObjectName(u"button_reset_phonon_sd")
        self.button_reset_phonon_sd.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonon_sd, 9, 10, 1, 1)

        self.label_title_adjust_rates = QLabel(self.tab_environment)
        self.label_title_adjust_rates.setObjectName(u"label_title_adjust_rates")
        self.label_title_adjust_rates.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_title_adjust_rates, 2, 10, 1, 1)

        self.input_phonons_adjust_radiativeloss = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_radiativeloss.setObjectName(u"input_phonons_adjust_radiativeloss")
        self.input_phonons_adjust_radiativeloss.setMinimumSize(QSize(150, 40))
        self.input_phonons_adjust_radiativeloss.setFont(font)
        self.input_phonons_adjust_radiativeloss.setChecked(True)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_radiativeloss, 3, 10, 1, 1)

        self.textinput_phonons_sd_qd_dh = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_dh.setObjectName(u"textinput_phonons_sd_qd_dh")
        self.textinput_phonons_sd_qd_dh.setEnabled(False)
        self.textinput_phonons_sd_qd_dh.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setPointSize(11)
        self.textinput_phonons_sd_qd_dh.setFont(font1)
        self.textinput_phonons_sd_qd_dh.setFrame(True)
        self.textinput_phonons_sd_qd_dh.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_dh, 17, 3, 1, 1)

        self.label_title_rates = QLabel(self.tab_environment)
        self.label_title_rates.setObjectName(u"label_title_rates")
        self.label_title_rates.setMaximumSize(QSize(16777215, 40))
        self.label_title_rates.setFrameShape(QFrame.NoFrame)
        self.label_title_rates.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_rates, 2, 0, 1, 2)

        self.label_26 = QLabel(self.tab_environment)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_26, 3, 8, 1, 1)

        self.label_19 = QLabel(self.tab_environment)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_19, 4, 0, 1, 1)

        self.label_25 = QLabel(self.tab_environment)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_25, 16, 0, 1, 1)

        self.label_28 = QLabel(self.tab_environment)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_28, 5, 5, 1, 1)

        self.button_reset_phonon_qd = QPushButton(self.tab_environment)
        self.button_reset_phonon_qd.setObjectName(u"button_reset_phonon_qd")
        self.button_reset_phonon_qd.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonon_qd, 20, 9, 1, 1)

        self.textinput_phonons_sd_alpha = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_alpha.setObjectName(u"textinput_phonons_sd_alpha")
        self.textinput_phonons_sd_alpha.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_alpha.setFont(font1)
        self.textinput_phonons_sd_alpha.setFrame(True)
        self.textinput_phonons_sd_alpha.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_alpha, 3, 9, 1, 1)

        self.label_39 = QLabel(self.tab_environment)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 15, 5, 1, 3)

        self.line_2 = QFrame(self.tab_environment)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 14, 0, 1, 11)

        self.label_title_phonons_3 = QLabel(self.tab_environment)
        self.label_title_phonons_3.setObjectName(u"label_title_phonons_3")
        self.label_title_phonons_3.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_3.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_3.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_3, 2, 8, 1, 2)

        self.label_plot_lindblad_rates = QLabel(self.tab_environment)
        self.label_plot_lindblad_rates.setObjectName(u"label_plot_lindblad_rates")

        self.gridLayout_3.addWidget(self.label_plot_lindblad_rates, 16, 8, 4, 3)

        self.textinput_phonons_sd_wcutoff = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_wcutoff.setObjectName(u"textinput_phonons_sd_wcutoff")
        self.textinput_phonons_sd_wcutoff.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_wcutoff.setFont(font1)
        self.textinput_phonons_sd_wcutoff.setFrame(True)
        self.textinput_phonons_sd_wcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_wcutoff, 4, 7, 1, 1)

        self.textinput_phonons_sd_qd_aeah_ratio = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_aeah_ratio.setObjectName(u"textinput_phonons_sd_qd_aeah_ratio")
        self.textinput_phonons_sd_qd_aeah_ratio.setEnabled(False)
        self.textinput_phonons_sd_qd_aeah_ratio.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_qd_aeah_ratio.setFont(font1)
        self.textinput_phonons_sd_qd_aeah_ratio.setFrame(True)
        self.textinput_phonons_sd_qd_aeah_ratio.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_aeah_ratio, 19, 1, 1, 1)

        self.label_27 = QLabel(self.tab_environment)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_27, 4, 5, 1, 1)

        self.textinput_phonons_sd_ohmamp = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_ohmamp.setObjectName(u"textinput_phonons_sd_ohmamp")
        self.textinput_phonons_sd_ohmamp.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_ohmamp.setFont(font1)
        self.textinput_phonons_sd_ohmamp.setFrame(True)
        self.textinput_phonons_sd_ohmamp.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_ohmamp, 4, 3, 1, 1)

        self.label_32 = QLabel(self.tab_environment)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_32, 17, 2, 1, 1)

        self.label_34 = QLabel(self.tab_environment)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_34, 18, 2, 1, 1)

        self.input_phonons_adjust_renormalization = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_renormalization.setObjectName(u"input_phonons_adjust_renormalization")
        self.input_phonons_adjust_renormalization.setMinimumSize(QSize(150, 40))
        self.input_phonons_adjust_renormalization.setFont(font)
        self.input_phonons_adjust_renormalization.setChecked(True)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_renormalization, 5, 10, 1, 1)

        self.label_18 = QLabel(self.tab_environment)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 1)

        self.textinput_rates_radiative_decay = QLineEdit(self.tab_environment)
        self.textinput_rates_radiative_decay.setObjectName(u"textinput_rates_radiative_decay")
        self.textinput_rates_radiative_decay.setMinimumSize(QSize(150, 40))
        self.textinput_rates_radiative_decay.setFont(font1)
        self.textinput_rates_radiative_decay.setFrame(True)
        self.textinput_rates_radiative_decay.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_radiative_decay, 5, 1, 1, 1)

        self.textinput_rates_pure_dephasing = QLineEdit(self.tab_environment)
        self.textinput_rates_pure_dephasing.setObjectName(u"textinput_rates_pure_dephasing")
        self.textinput_rates_pure_dephasing.setMinimumSize(QSize(150, 40))
        self.textinput_rates_pure_dephasing.setFont(font1)
        self.textinput_rates_pure_dephasing.setFrame(True)
        self.textinput_rates_pure_dephasing.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_pure_dephasing, 6, 1, 1, 1)

        self.line_3 = QFrame(self.tab_environment)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 16, 4, 4, 1)

        self.textinput_phonons_sd_qd_rho = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_rho.setObjectName(u"textinput_phonons_sd_qd_rho")
        self.textinput_phonons_sd_qd_rho.setEnabled(False)
        self.textinput_phonons_sd_qd_rho.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_qd_rho.setFont(font1)
        self.textinput_phonons_sd_qd_rho.setFrame(True)
        self.textinput_phonons_sd_qd_rho.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_rho, 18, 1, 1, 1)

        self.input_phonons_approximation = QComboBox(self.tab_environment)
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.addItem("")
        self.input_phonons_approximation.setObjectName(u"input_phonons_approximation")
        self.input_phonons_approximation.setMinimumSize(QSize(150, 40))
        self.input_phonons_approximation.setFont(font1)
        self.input_phonons_approximation.setFocusPolicy(Qt.WheelFocus)
        self.input_phonons_approximation.setFrame(True)

        self.gridLayout_3.addWidget(self.input_phonons_approximation, 5, 3, 1, 1)

        self.input_phonons_use_qd = QCheckBox(self.tab_environment)
        self.input_phonons_use_qd.setObjectName(u"input_phonons_use_qd")
        self.input_phonons_use_qd.setMinimumSize(QSize(150, 40))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.input_phonons_use_qd.setFont(font2)

        self.gridLayout_3.addWidget(self.input_phonons_use_qd, 16, 1, 1, 3)

        self.label_35 = QLabel(self.tab_environment)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_35, 19, 0, 1, 1)

        self.label_37 = QLabel(self.tab_environment)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_37, 3, 5, 1, 1)

        self.label_36 = QLabel(self.tab_environment)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_36, 19, 2, 1, 1)

        self.label_30 = QLabel(self.tab_environment)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_30, 4, 2, 1, 1)

        self.label_31 = QLabel(self.tab_environment)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_31, 17, 0, 1, 1)

        self.textinput_phonons_sd_tcutoff = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_tcutoff.setObjectName(u"textinput_phonons_sd_tcutoff")
        self.textinput_phonons_sd_tcutoff.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_tcutoff.setFont(font1)
        self.textinput_phonons_sd_tcutoff.setFrame(True)
        self.textinput_phonons_sd_tcutoff.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_tcutoff, 6, 7, 1, 1)

        self.label_20 = QLabel(self.tab_environment)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_20, 5, 0, 1, 1)

        self.label_22 = QLabel(self.tab_environment)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_22, 3, 2, 1, 1)

        self.textinput_phonons_sd_wdelta = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_wdelta.setObjectName(u"textinput_phonons_sd_wdelta")
        self.textinput_phonons_sd_wdelta.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_wdelta.setFont(font1)
        self.textinput_phonons_sd_wdelta.setFrame(True)
        self.textinput_phonons_sd_wdelta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_wdelta, 5, 7, 1, 1)

        self.label_title_phonons = QLabel(self.tab_environment)
        self.label_title_phonons.setObjectName(u"label_title_phonons")
        self.label_title_phonons.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons, 2, 2, 1, 2)

        self.textinput_phonons_sd_qd_size = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_size.setObjectName(u"textinput_phonons_sd_qd_size")
        self.textinput_phonons_sd_qd_size.setEnabled(False)
        self.textinput_phonons_sd_qd_size.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_qd_size.setFont(font1)
        self.textinput_phonons_sd_qd_size.setFrame(True)
        self.textinput_phonons_sd_qd_size.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_size, 19, 3, 1, 1)

        self.label_title_phonons_2 = QLabel(self.tab_environment)
        self.label_title_phonons_2.setObjectName(u"label_title_phonons_2")
        self.label_title_phonons_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_2.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_2, 2, 5, 1, 3)

        self.label_33 = QLabel(self.tab_environment)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_33, 18, 0, 1, 1)

        self.button_reset_rates = QPushButton(self.tab_environment)
        self.button_reset_rates.setObjectName(u"button_reset_rates")
        self.button_reset_rates.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_rates, 9, 0, 1, 2)

        self.label_23 = QLabel(self.tab_environment)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_23, 5, 2, 1, 1)

        self.button_reset_phonons_3 = QPushButton(self.tab_environment)
        self.button_reset_phonons_3.setObjectName(u"button_reset_phonons_3")
        self.button_reset_phonons_3.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonons_3, 9, 8, 1, 2)

        self.button_reset_phonons_2 = QPushButton(self.tab_environment)
        self.button_reset_phonons_2.setObjectName(u"button_reset_phonons_2")
        self.button_reset_phonons_2.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonons_2, 9, 5, 1, 3)

        self.label_21 = QLabel(self.tab_environment)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_21, 6, 0, 1, 1)

        self.label_title_phonons_4 = QLabel(self.tab_environment)
        self.label_title_phonons_4.setObjectName(u"label_title_phonons_4")
        self.label_title_phonons_4.setMaximumSize(QSize(16777215, 40))
        self.label_title_phonons_4.setFrameShape(QFrame.NoFrame)
        self.label_title_phonons_4.setFrameShadow(QFrame.Plain)

        self.gridLayout_3.addWidget(self.label_title_phonons_4, 15, 0, 1, 4)

        self.label_29 = QLabel(self.tab_environment)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.label_29, 6, 5, 1, 1)

        self.textinput_phonons_temperature = QLineEdit(self.tab_environment)
        self.textinput_phonons_temperature.setObjectName(u"textinput_phonons_temperature")
        self.textinput_phonons_temperature.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_temperature.setFont(font1)
        self.textinput_phonons_temperature.setFrame(True)
        self.textinput_phonons_temperature.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_temperature, 3, 3, 1, 1)

        self.textinput_rates_cavity_coupling = QLineEdit(self.tab_environment)
        self.textinput_rates_cavity_coupling.setObjectName(u"textinput_rates_cavity_coupling")
        self.textinput_rates_cavity_coupling.setMinimumSize(QSize(150, 40))
        self.textinput_rates_cavity_coupling.setFont(font1)
        self.textinput_rates_cavity_coupling.setFrame(True)
        self.textinput_rates_cavity_coupling.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_coupling, 3, 1, 1, 1)

        self.textinput_rates_cavity_loss = QLineEdit(self.tab_environment)
        self.textinput_rates_cavity_loss.setObjectName(u"textinput_rates_cavity_loss")
        self.textinput_rates_cavity_loss.setMinimumSize(QSize(150, 40))
        self.textinput_rates_cavity_loss.setFont(font1)
        self.textinput_rates_cavity_loss.setFrame(True)
        self.textinput_rates_cavity_loss.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_rates_cavity_loss, 4, 1, 1, 1)

        self.textinput_phonons_iterator_stepsize = QLineEdit(self.tab_environment)
        self.textinput_phonons_iterator_stepsize.setObjectName(u"textinput_phonons_iterator_stepsize")
        self.textinput_phonons_iterator_stepsize.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_iterator_stepsize.setFont(font1)
        self.textinput_phonons_iterator_stepsize.setFrame(True)
        self.textinput_phonons_iterator_stepsize.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_iterator_stepsize, 3, 7, 1, 1)

        self.textinput_phonons_sd_qd_cs = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_cs.setObjectName(u"textinput_phonons_sd_qd_cs")
        self.textinput_phonons_sd_qd_cs.setEnabled(False)
        self.textinput_phonons_sd_qd_cs.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_qd_cs.setFont(font1)
        self.textinput_phonons_sd_qd_cs.setFrame(True)
        self.textinput_phonons_sd_qd_cs.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_cs, 18, 3, 1, 1)

        self.input_phonons_adjust_pure_dephasing = QCheckBox(self.tab_environment)
        self.input_phonons_adjust_pure_dephasing.setObjectName(u"input_phonons_adjust_pure_dephasing")
        self.input_phonons_adjust_pure_dephasing.setMinimumSize(QSize(150, 40))
        self.input_phonons_adjust_pure_dephasing.setFont(font)

        self.gridLayout_3.addWidget(self.input_phonons_adjust_pure_dephasing, 4, 10, 1, 1)

        self.label_40 = QLabel(self.tab_environment)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 15, 8, 1, 3)

        self.label_plot_spectral_density = QLabel(self.tab_environment)
        self.label_plot_spectral_density.setObjectName(u"label_plot_spectral_density")

        self.gridLayout_3.addWidget(self.label_plot_spectral_density, 16, 5, 4, 3)

        self.button_reset_phonons = QPushButton(self.tab_environment)
        self.button_reset_phonons.setObjectName(u"button_reset_phonons")
        self.button_reset_phonons.setMinimumSize(QSize(150, 40))

        self.gridLayout_3.addWidget(self.button_reset_phonons, 9, 2, 1, 2)

        self.textinput_phonons_sd_qd_de = QLineEdit(self.tab_environment)
        self.textinput_phonons_sd_qd_de.setObjectName(u"textinput_phonons_sd_qd_de")
        self.textinput_phonons_sd_qd_de.setEnabled(False)
        self.textinput_phonons_sd_qd_de.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_sd_qd_de.setFont(font1)
        self.textinput_phonons_sd_qd_de.setFrame(True)
        self.textinput_phonons_sd_qd_de.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.textinput_phonons_sd_qd_de, 17, 1, 1, 1)

        self.button_next_tab_config_to_timeline = QPushButton(self.tab_environment)
        self.button_next_tab_config_to_timeline.setObjectName(u"button_next_tab_config_to_timeline")
        self.button_next_tab_config_to_timeline.setMinimumSize(QSize(150, 40))
        self.button_next_tab_config_to_timeline.setMaximumSize(QSize(150, 16777215))
        self.button_next_tab_config_to_timeline.setCheckable(False)

        self.gridLayout_3.addWidget(self.button_next_tab_config_to_timeline, 20, 10, 1, 1)

        self.tabWidget.addTab(self.tab_environment, "")
        self.tab_timeline = QWidget()
        self.tab_timeline.setObjectName(u"tab_timeline")
        self.gridLayout_4 = QGridLayout(self.tab_timeline)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_15 = QLabel(self.tab_timeline)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_15, 4, 5, 1, 1)

        self.label_title_time = QLabel(self.tab_timeline)
        self.label_title_time.setObjectName(u"label_title_time")
        self.label_title_time.setMaximumSize(QSize(16777215, 40))
        self.label_title_time.setFrameShape(QFrame.NoFrame)
        self.label_title_time.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_time, 0, 0, 1, 2)

        self.textinput_phonons_tsteppath = QLineEdit(self.tab_timeline)
        self.textinput_phonons_tsteppath.setObjectName(u"textinput_phonons_tsteppath")
        self.textinput_phonons_tsteppath.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_tsteppath.setFont(font1)
        self.textinput_phonons_tsteppath.setFrame(True)
        self.textinput_phonons_tsteppath.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_phonons_tsteppath, 6, 6, 1, 1)

        self.button_time_config_grid = QPushButton(self.tab_timeline)
        self.button_time_config_grid.setObjectName(u"button_time_config_grid")
        self.button_time_config_grid.setMinimumSize(QSize(150, 40))
        self.button_time_config_grid.setFont(font)

        self.gridLayout_4.addWidget(self.button_time_config_grid, 5, 0, 1, 1)

        self.input_rungekutta_order = QComboBox(self.tab_timeline)
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.addItem("")
        self.input_rungekutta_order.setObjectName(u"input_rungekutta_order")
        self.input_rungekutta_order.setMinimumSize(QSize(150, 40))
        self.input_rungekutta_order.setFont(font1)
        self.input_rungekutta_order.setFocusPolicy(Qt.WheelFocus)

        self.gridLayout_4.addWidget(self.input_rungekutta_order, 2, 6, 1, 1)

        self.textinput_phonons_nc = QLineEdit(self.tab_timeline)
        self.textinput_phonons_nc.setObjectName(u"textinput_phonons_nc")
        self.textinput_phonons_nc.setMinimumSize(QSize(150, 40))
        self.textinput_phonons_nc.setFont(font1)
        self.textinput_phonons_nc.setFrame(True)
        self.textinput_phonons_nc.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_phonons_nc, 5, 6, 1, 1)

        self.button_time_config_tol = QPushButton(self.tab_timeline)
        self.button_time_config_tol.setObjectName(u"button_time_config_tol")
        self.button_time_config_tol.setMinimumSize(QSize(150, 40))
        self.button_time_config_tol.setFont(font)

        self.gridLayout_4.addWidget(self.button_time_config_tol, 6, 0, 1, 1)

        self.label_12 = QLabel(self.tab_timeline)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_12, 2, 5, 1, 1)

        self.label_11 = QLabel(self.tab_timeline)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 1)

        self.button_timeline_force_calculate = QPushButton(self.tab_timeline)
        self.button_timeline_force_calculate.setObjectName(u"button_timeline_force_calculate")
        self.button_timeline_force_calculate.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.button_timeline_force_calculate, 16, 1, 1, 1)

        self.label_38 = QLabel(self.tab_timeline)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_38, 5, 5, 1, 1)

        self.label_41 = QLabel(self.tab_timeline)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_41, 6, 5, 1, 1)

        self.input_timeline_enable_phonons = QCheckBox(self.tab_timeline)
        self.input_timeline_enable_phonons.setObjectName(u"input_timeline_enable_phonons")
        self.input_timeline_enable_phonons.setMinimumSize(QSize(150, 40))
        self.input_timeline_enable_phonons.setChecked(True)

        self.gridLayout_4.addWidget(self.input_timeline_enable_phonons, 16, 0, 1, 1)

        self.label_plot_time_prediction = PlotWidget(self.tab_timeline)
        self.label_plot_time_prediction.setObjectName(u"label_plot_time_prediction")

        self.gridLayout_4.addWidget(self.label_plot_time_prediction, 14, 0, 1, 7)

        self.label_10 = QLabel(self.tab_timeline)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_10, 3, 0, 1, 1)

        self.textinput_time_endtime = QLineEdit(self.tab_timeline)
        self.textinput_time_endtime.setObjectName(u"textinput_time_endtime")
        self.textinput_time_endtime.setMinimumSize(QSize(150, 40))
        self.textinput_time_endtime.setFont(font1)
        self.textinput_time_endtime.setFrame(True)
        self.textinput_time_endtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_endtime, 3, 1, 1, 1)

        self.label_title_solver = QLabel(self.tab_timeline)
        self.label_title_solver.setObjectName(u"label_title_solver")
        self.label_title_solver.setMaximumSize(QSize(16777215, 40))
        self.label_title_solver.setFrameShape(QFrame.NoFrame)
        self.label_title_solver.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_solver, 0, 5, 1, 2)

        self.input_interpolator_t = QComboBox(self.tab_timeline)
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.addItem("")
        self.input_interpolator_t.setObjectName(u"input_interpolator_t")
        self.input_interpolator_t.setMinimumSize(QSize(150, 40))
        self.input_interpolator_t.setFont(font1)
        self.input_interpolator_t.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_t.setFrame(True)

        self.gridLayout_4.addWidget(self.input_interpolator_t, 3, 6, 1, 1)

        self.label_9 = QLabel(self.tab_timeline)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_9, 2, 0, 1, 1)

        self.textinput_time_gridresolution = QLineEdit(self.tab_timeline)
        self.textinput_time_gridresolution.setObjectName(u"textinput_time_gridresolution")
        self.textinput_time_gridresolution.setMinimumSize(QSize(150, 40))
        self.textinput_time_gridresolution.setFont(font1)
        self.textinput_time_gridresolution.setFrame(True)
        self.textinput_time_gridresolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_gridresolution, 5, 1, 1, 1)

        self.input_interpolator_tau = QComboBox(self.tab_timeline)
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.addItem("")
        self.input_interpolator_tau.setObjectName(u"input_interpolator_tau")
        self.input_interpolator_tau.setMinimumSize(QSize(150, 40))
        self.input_interpolator_tau.setFont(font1)
        self.input_interpolator_tau.setFocusPolicy(Qt.WheelFocus)
        self.input_interpolator_tau.setFrame(True)

        self.gridLayout_4.addWidget(self.input_interpolator_tau, 4, 6, 1, 1)

        self.label_14 = QLabel(self.tab_timeline)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.label_14, 3, 5, 1, 1)

        self.textinput_time_startingtime = QLineEdit(self.tab_timeline)
        self.textinput_time_startingtime.setObjectName(u"textinput_time_startingtime")
        self.textinput_time_startingtime.setMinimumSize(QSize(150, 40))
        self.textinput_time_startingtime.setFont(font1)
        self.textinput_time_startingtime.setFrame(True)
        self.textinput_time_startingtime.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_startingtime, 2, 1, 1, 1)

        self.textinput_time_tolerance = QLineEdit(self.tab_timeline)
        self.textinput_time_tolerance.setObjectName(u"textinput_time_tolerance")
        self.textinput_time_tolerance.setMinimumSize(QSize(150, 40))
        self.textinput_time_tolerance.setFont(font1)
        self.textinput_time_tolerance.setFrame(True)
        self.textinput_time_tolerance.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_tolerance, 6, 1, 1, 1)

        self.textinput_time_timestep = QLineEdit(self.tab_timeline)
        self.textinput_time_timestep.setObjectName(u"textinput_time_timestep")
        self.textinput_time_timestep.setMinimumSize(QSize(150, 40))
        self.textinput_time_timestep.setFont(font1)
        self.textinput_time_timestep.setFrame(True)
        self.textinput_time_timestep.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.textinput_time_timestep, 4, 1, 1, 1)

        self.label_title_predicted_timeline = QLabel(self.tab_timeline)
        self.label_title_predicted_timeline.setObjectName(u"label_title_predicted_timeline")
        self.label_title_predicted_timeline.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_timeline.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_timeline.setFrameShadow(QFrame.Plain)

        self.gridLayout_4.addWidget(self.label_title_predicted_timeline, 13, 0, 1, 7)

        self.button_next_tab_timeline_to_spectrum = QPushButton(self.tab_timeline)
        self.button_next_tab_timeline_to_spectrum.setObjectName(u"button_next_tab_timeline_to_spectrum")
        self.button_next_tab_timeline_to_spectrum.setMinimumSize(QSize(150, 40))

        self.gridLayout_4.addWidget(self.button_next_tab_timeline_to_spectrum, 16, 6, 1, 1)

        self.tabWidget.addTab(self.tab_timeline, "")
        self.tab_spectrum = QWidget()
        self.tab_spectrum.setObjectName(u"tab_spectrum")
        self.gridLayout_5 = QGridLayout(self.tab_spectrum)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textinput_spectrum_range = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_range.setObjectName(u"textinput_spectrum_range")
        self.textinput_spectrum_range.setMinimumSize(QSize(150, 40))
        self.textinput_spectrum_range.setFont(font1)
        self.textinput_spectrum_range.setFrame(True)
        self.textinput_spectrum_range.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_range, 2, 1, 1, 3)

        self.input_spectrum_order = QComboBox(self.tab_spectrum)
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.addItem("")
        self.input_spectrum_order.setObjectName(u"input_spectrum_order")
        self.input_spectrum_order.setMinimumSize(QSize(150, 40))
        self.input_spectrum_order.setFont(font1)

        self.gridLayout_5.addWidget(self.input_spectrum_order, 5, 1, 1, 3)

        self.button_add_spectrum_to_output = QPushButton(self.tab_spectrum)
        self.button_add_spectrum_to_output.setObjectName(u"button_add_spectrum_to_output")
        self.button_add_spectrum_to_output.setMinimumSize(QSize(150, 40))
        self.button_add_spectrum_to_output.setFont(font)

        self.gridLayout_5.addWidget(self.button_add_spectrum_to_output, 7, 0, 1, 2)

        self.label_49 = QLabel(self.tab_spectrum)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_49, 4, 0, 1, 1)

        self.textinput_spectrum_modes = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_modes.setObjectName(u"textinput_spectrum_modes")
        self.textinput_spectrum_modes.setMinimumSize(QSize(150, 40))
        self.textinput_spectrum_modes.setFont(font1)
        self.textinput_spectrum_modes.setFrame(True)
        self.textinput_spectrum_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_modes, 1, 1, 1, 3)

        self.label_51 = QLabel(self.tab_spectrum)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_51, 6, 0, 1, 1)

        self.label_title_predicted_spectral = QLabel(self.tab_spectrum)
        self.label_title_predicted_spectral.setObjectName(u"label_title_predicted_spectral")
        self.label_title_predicted_spectral.setMaximumSize(QSize(16777215, 40))
        self.label_title_predicted_spectral.setFrameShape(QFrame.NoFrame)
        self.label_title_predicted_spectral.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_title_predicted_spectral, 9, 0, 1, 13)

        self.label_title_set_spectrum = QLabel(self.tab_spectrum)
        self.label_title_set_spectrum.setObjectName(u"label_title_set_spectrum")
        self.label_title_set_spectrum.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_spectrum.setFrameShape(QFrame.NoFrame)
        self.label_title_set_spectrum.setFrameShadow(QFrame.Plain)

        self.gridLayout_5.addWidget(self.label_title_set_spectrum, 0, 0, 1, 13)

        self.label_46 = QLabel(self.tab_spectrum)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_46, 1, 0, 1, 1)

        self.button_next_tab_spectrum_to_indist = QPushButton(self.tab_spectrum)
        self.button_next_tab_spectrum_to_indist.setObjectName(u"button_next_tab_spectrum_to_indist")
        self.button_next_tab_spectrum_to_indist.setMinimumSize(QSize(150, 40))
        self.button_next_tab_spectrum_to_indist.setCheckable(False)

        self.gridLayout_5.addWidget(self.button_next_tab_spectrum_to_indist, 13, 12, 1, 1)

        self.input_spectrum_normalize = QCheckBox(self.tab_spectrum)
        self.input_spectrum_normalize.setObjectName(u"input_spectrum_normalize")
        self.input_spectrum_normalize.setMinimumSize(QSize(150, 40))
        self.input_spectrum_normalize.setFont(font1)
        self.input_spectrum_normalize.setChecked(False)

        self.gridLayout_5.addWidget(self.input_spectrum_normalize, 6, 1, 1, 3)

        self.textinput_spectrum_range_2 = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_range_2.setObjectName(u"textinput_spectrum_range_2")
        self.textinput_spectrum_range_2.setMinimumSize(QSize(150, 40))
        self.textinput_spectrum_range_2.setFont(font1)
        self.textinput_spectrum_range_2.setFrame(True)
        self.textinput_spectrum_range_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_range_2, 4, 1, 1, 3)

        self.button_add_spectrum_to_output_3 = QPushButton(self.tab_spectrum)
        self.button_add_spectrum_to_output_3.setObjectName(u"button_add_spectrum_to_output_3")
        self.button_add_spectrum_to_output_3.setMinimumSize(QSize(150, 40))
        self.button_add_spectrum_to_output_3.setFont(font)

        self.gridLayout_5.addWidget(self.button_add_spectrum_to_output_3, 7, 2, 1, 2)

        self.input_timeline_enable_phonons_2 = QCheckBox(self.tab_spectrum)
        self.input_timeline_enable_phonons_2.setObjectName(u"input_timeline_enable_phonons_2")
        self.input_timeline_enable_phonons_2.setMinimumSize(QSize(150, 40))
        self.input_timeline_enable_phonons_2.setChecked(True)

        self.gridLayout_5.addWidget(self.input_timeline_enable_phonons_2, 13, 0, 1, 1)

        self.label_47 = QLabel(self.tab_spectrum)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_47, 3, 0, 1, 1)

        self.textinput_spectrum_center = QLineEdit(self.tab_spectrum)
        self.textinput_spectrum_center.setObjectName(u"textinput_spectrum_center")
        self.textinput_spectrum_center.setMinimumSize(QSize(150, 40))
        self.textinput_spectrum_center.setFont(font1)
        self.textinput_spectrum_center.setFrame(True)
        self.textinput_spectrum_center.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.textinput_spectrum_center, 3, 1, 1, 3)

        self.text_output_list_of_spectra = QListView(self.tab_spectrum)
        self.text_output_list_of_spectra.setObjectName(u"text_output_list_of_spectra")
        self.text_output_list_of_spectra.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.text_output_list_of_spectra, 1, 4, 7, 9)

        self.label_48 = QLabel(self.tab_spectrum)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_48, 2, 0, 1, 1)

        self.label_50 = QLabel(self.tab_spectrum)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.label_50, 5, 0, 1, 1)

        self.label_plot_spectral_prediction = PlotWidget(self.tab_spectrum)
        self.label_plot_spectral_prediction.setObjectName(u"label_plot_spectral_prediction")

        self.gridLayout_5.addWidget(self.label_plot_spectral_prediction, 10, 0, 1, 13)

        self.button_time_config_grid_3 = QPushButton(self.tab_spectrum)
        self.button_time_config_grid_3.setObjectName(u"button_time_config_grid_3")
        self.button_time_config_grid_3.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.button_time_config_grid_3, 13, 11, 1, 1)

        self.button_timeline_force_calculate_2 = QPushButton(self.tab_spectrum)
        self.button_timeline_force_calculate_2.setObjectName(u"button_timeline_force_calculate_2")
        self.button_timeline_force_calculate_2.setMinimumSize(QSize(150, 40))

        self.gridLayout_5.addWidget(self.button_timeline_force_calculate_2, 13, 10, 1, 1)

        self.tabWidget.addTab(self.tab_spectrum, "")
        self.tab_indist = QWidget()
        self.tab_indist.setObjectName(u"tab_indist")
        self.gridLayout_7 = QGridLayout(self.tab_indist)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_52 = QLabel(self.tab_indist)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(150, 40))
        self.label_52.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_7.addWidget(self.label_52, 1, 1, 1, 1)

        self.label_title_set_indists_2 = QLabel(self.tab_indist)
        self.label_title_set_indists_2.setObjectName(u"label_title_set_indists_2")
        self.label_title_set_indists_2.setMinimumSize(QSize(150, 40))
        self.label_title_set_indists_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_indists_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_7.addWidget(self.label_title_set_indists_2, 2, 1, 1, 4)

        self.textinput_indist_modes = QLineEdit(self.tab_indist)
        self.textinput_indist_modes.setObjectName(u"textinput_indist_modes")
        self.textinput_indist_modes.setMinimumSize(QSize(150, 40))
        self.textinput_indist_modes.setFont(font1)
        self.textinput_indist_modes.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_indist_modes.setFrame(True)
        self.textinput_indist_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.textinput_indist_modes, 1, 2, 1, 1)

        self.text_output_list_of_indists = QListView(self.tab_indist)
        self.text_output_list_of_indists.setObjectName(u"text_output_list_of_indists")

        self.gridLayout_7.addWidget(self.text_output_list_of_indists, 3, 1, 1, 4)

        self.button_next_tab_indist_to_conc = QPushButton(self.tab_indist)
        self.button_next_tab_indist_to_conc.setObjectName(u"button_next_tab_indist_to_conc")
        self.button_next_tab_indist_to_conc.setMinimumSize(QSize(150, 40))
        self.button_next_tab_indist_to_conc.setCheckable(False)

        self.gridLayout_7.addWidget(self.button_next_tab_indist_to_conc, 4, 4, 1, 1)

        self.label_title_set_indists = QLabel(self.tab_indist)
        self.label_title_set_indists.setObjectName(u"label_title_set_indists")
        self.label_title_set_indists.setMinimumSize(QSize(150, 40))
        self.label_title_set_indists.setFrameShape(QFrame.NoFrame)
        self.label_title_set_indists.setFrameShadow(QFrame.Plain)

        self.gridLayout_7.addWidget(self.label_title_set_indists, 0, 0, 1, 5)

        self.button_remove_indist_from_output = QPushButton(self.tab_indist)
        self.button_remove_indist_from_output.setObjectName(u"button_remove_indist_from_output")
        self.button_remove_indist_from_output.setMinimumSize(QSize(150, 40))
        self.button_remove_indist_from_output.setFont(font)

        self.gridLayout_7.addWidget(self.button_remove_indist_from_output, 4, 1, 1, 1)

        self.button_add_indist_to_output = QPushButton(self.tab_indist)
        self.button_add_indist_to_output.setObjectName(u"button_add_indist_to_output")
        self.button_add_indist_to_output.setMinimumSize(QSize(150, 40))
        self.button_add_indist_to_output.setFont(font)

        self.gridLayout_7.addWidget(self.button_add_indist_to_output, 1, 3, 1, 2)

        self.tabWidget.addTab(self.tab_indist, "")
        self.tab_concurrence = QWidget()
        self.tab_concurrence.setObjectName(u"tab_concurrence")
        self.gridLayout = QGridLayout(self.tab_concurrence)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_114 = QLabel(self.tab_concurrence)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(140, 40))
        self.label_114.setMaximumSize(QSize(200, 16777215))
        self.label_114.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_114, 11, 0, 1, 1)

        self.label_115 = QLabel(self.tab_concurrence)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(140, 40))
        self.label_115.setMaximumSize(QSize(200, 16777215))
        self.label_115.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_115, 12, 0, 1, 1)

        self.label_55 = QLabel(self.tab_concurrence)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(140, 40))
        self.label_55.setMaximumSize(QSize(200, 16777215))
        self.label_55.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_55, 9, 0, 1, 1)

        self.button_next_tab_sconc_to_stats = QPushButton(self.tab_concurrence)
        self.button_next_tab_sconc_to_stats.setObjectName(u"button_next_tab_sconc_to_stats")
        self.button_next_tab_sconc_to_stats.setMinimumSize(QSize(140, 40))
        self.button_next_tab_sconc_to_stats.setMaximumSize(QSize(200, 16777215))
        self.button_next_tab_sconc_to_stats.setCheckable(False)

        self.gridLayout.addWidget(self.button_next_tab_sconc_to_stats, 15, 7, 1, 1)

        self.label_54 = QLabel(self.tab_concurrence)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(140, 40))
        self.label_54.setMaximumSize(QSize(200, 16777215))
        self.label_54.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_54, 4, 0, 1, 1)

        self.label_113 = QLabel(self.tab_concurrence)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(140, 40))
        self.label_113.setMaximumSize(QSize(200, 16777215))
        self.label_113.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_113, 10, 0, 1, 1)

        self.label_53 = QLabel(self.tab_concurrence)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(140, 40))
        self.label_53.setMaximumSize(QSize(200, 16777215))
        self.label_53.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout.addWidget(self.label_53, 3, 0, 1, 1)

        self.button_add_concurrence_to_output = QPushButton(self.tab_concurrence)
        self.button_add_concurrence_to_output.setObjectName(u"button_add_concurrence_to_output")
        self.button_add_concurrence_to_output.setMinimumSize(QSize(140, 40))
        self.button_add_concurrence_to_output.setFont(font)

        self.gridLayout.addWidget(self.button_add_concurrence_to_output, 5, 0, 1, 2)

        self.button_add_concurrence_to_output_2 = QPushButton(self.tab_concurrence)
        self.button_add_concurrence_to_output_2.setObjectName(u"button_add_concurrence_to_output_2")
        self.button_add_concurrence_to_output_2.setMinimumSize(QSize(140, 40))
        self.button_add_concurrence_to_output_2.setFont(font)

        self.gridLayout.addWidget(self.button_add_concurrence_to_output_2, 5, 2, 1, 1)

        self.label_title_set_concurrences = QLabel(self.tab_concurrence)
        self.label_title_set_concurrences.setObjectName(u"label_title_set_concurrences")
        self.label_title_set_concurrences.setMinimumSize(QSize(0, 40))
        self.label_title_set_concurrences.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_title_set_concurrences, 2, 0, 1, 3)

        self.textinput_concurrence_first = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_first.setObjectName(u"textinput_concurrence_first")
        self.textinput_concurrence_first.setMinimumSize(QSize(140, 40))
        self.textinput_concurrence_first.setFont(font1)
        self.textinput_concurrence_first.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_concurrence_first.setFrame(True)
        self.textinput_concurrence_first.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_first, 3, 1, 1, 2)

        self.textinput_concurrence_second = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_second.setObjectName(u"textinput_concurrence_second")
        self.textinput_concurrence_second.setMinimumSize(QSize(140, 40))
        self.textinput_concurrence_second.setFont(font1)
        self.textinput_concurrence_second.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_concurrence_second.setFrame(True)
        self.textinput_concurrence_second.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_second, 4, 1, 1, 2)

        self.text_output_list_of_concurrences = QListView(self.tab_concurrence)
        self.text_output_list_of_concurrences.setObjectName(u"text_output_list_of_concurrences")

        self.gridLayout.addWidget(self.text_output_list_of_concurrences, 6, 0, 1, 3)

        self.label_title_set_concurrences_2 = QLabel(self.tab_concurrence)
        self.label_title_set_concurrences_2.setObjectName(u"label_title_set_concurrences_2")
        self.label_title_set_concurrences_2.setMinimumSize(QSize(0, 40))
        self.label_title_set_concurrences_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_concurrences_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_concurrences_2.setFrameShadow(QFrame.Plain)

        self.gridLayout.addWidget(self.label_title_set_concurrences_2, 8, 0, 1, 3)

        self.input_concurrence_add_spectra = QCheckBox(self.tab_concurrence)
        self.input_concurrence_add_spectra.setObjectName(u"input_concurrence_add_spectra")
        self.input_concurrence_add_spectra.setMinimumSize(QSize(140, 40))
        self.input_concurrence_add_spectra.setFont(font1)
        self.input_concurrence_add_spectra.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.input_concurrence_add_spectra.setChecked(False)

        self.gridLayout.addWidget(self.input_concurrence_add_spectra, 9, 1, 1, 2)

        self.textinput_concurrence_spec_freq = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_freq.setObjectName(u"textinput_concurrence_spec_freq")
        self.textinput_concurrence_spec_freq.setEnabled(False)
        self.textinput_concurrence_spec_freq.setMinimumSize(QSize(140, 40))
        self.textinput_concurrence_spec_freq.setFont(font1)
        self.textinput_concurrence_spec_freq.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_concurrence_spec_freq.setFrame(True)
        self.textinput_concurrence_spec_freq.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_freq, 10, 1, 1, 2)

        self.textinput_concurrence_spec_range = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_range.setObjectName(u"textinput_concurrence_spec_range")
        self.textinput_concurrence_spec_range.setEnabled(False)
        self.textinput_concurrence_spec_range.setMinimumSize(QSize(140, 40))
        self.textinput_concurrence_spec_range.setFont(font1)
        self.textinput_concurrence_spec_range.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_concurrence_spec_range.setFrame(True)
        self.textinput_concurrence_spec_range.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_range, 11, 1, 1, 2)

        self.textinput_concurrence_spec_res = QLineEdit(self.tab_concurrence)
        self.textinput_concurrence_spec_res.setObjectName(u"textinput_concurrence_spec_res")
        self.textinput_concurrence_spec_res.setEnabled(False)
        self.textinput_concurrence_spec_res.setMinimumSize(QSize(140, 40))
        self.textinput_concurrence_spec_res.setFont(font1)
        self.textinput_concurrence_spec_res.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_concurrence_spec_res.setFrame(True)
        self.textinput_concurrence_spec_res.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.textinput_concurrence_spec_res, 12, 1, 1, 2)

        self.tabWidget.addTab(self.tab_concurrence, "")
        self.tab_additional_stats = QWidget()
        self.tab_additional_stats.setObjectName(u"tab_additional_stats")
        self.gridLayout_8 = QGridLayout(self.tab_additional_stats)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_126 = QLabel(self.tab_additional_stats)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(150, 40))
        self.label_126.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_126, 12, 0, 1, 1)

        self.textinput_wigner_modes_y = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_modes_y.setObjectName(u"textinput_wigner_modes_y")
        self.textinput_wigner_modes_y.setMinimumSize(QSize(150, 40))
        self.textinput_wigner_modes_y.setFont(font1)
        self.textinput_wigner_modes_y.setFrame(True)
        self.textinput_wigner_modes_y.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_modes_y, 10, 2, 1, 1)

        self.label_123 = QLabel(self.tab_additional_stats)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setMinimumSize(QSize(150, 40))
        self.label_123.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_123, 9, 0, 1, 1)

        self.textinput_correlation_modes = QLineEdit(self.tab_additional_stats)
        self.textinput_correlation_modes.setObjectName(u"textinput_correlation_modes")
        self.textinput_correlation_modes.setMinimumSize(QSize(150, 40))
        self.textinput_correlation_modes.setFont(font1)
        self.textinput_correlation_modes.setFrame(True)
        self.textinput_correlation_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_correlation_modes, 1, 0, 1, 1)

        self.label_116 = QLabel(self.tab_additional_stats)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setMinimumSize(QSize(150, 40))
        self.label_116.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_116, 4, 0, 1, 1)

        self.label_122 = QLabel(self.tab_additional_stats)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setMinimumSize(QSize(150, 40))
        self.label_122.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_122, 8, 0, 1, 1)

        self.button_add_wigner = QPushButton(self.tab_additional_stats)
        self.button_add_wigner.setObjectName(u"button_add_wigner")
        self.button_add_wigner.setMinimumSize(QSize(150, 40))
        self.button_add_wigner.setFont(font)

        self.gridLayout_8.addWidget(self.button_add_wigner, 13, 0, 1, 3)

        self.label_124 = QLabel(self.tab_additional_stats)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setMinimumSize(QSize(150, 40))
        self.label_124.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_124, 10, 0, 1, 1)

        self.textinput_wigner_skip = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_skip.setObjectName(u"textinput_wigner_skip")
        self.textinput_wigner_skip.setMinimumSize(QSize(150, 40))
        self.textinput_wigner_skip.setFont(font1)
        self.textinput_wigner_skip.setFrame(True)
        self.textinput_wigner_skip.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_skip, 12, 2, 1, 1)

        self.text_output_list_of_gfuncs = QListView(self.tab_additional_stats)
        self.text_output_list_of_gfuncs.setObjectName(u"text_output_list_of_gfuncs")

        self.gridLayout_8.addWidget(self.text_output_list_of_gfuncs, 0, 2, 6, 8)

        self.label_57 = QLabel(self.tab_additional_stats)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(150, 40))
        self.label_57.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_57, 2, 0, 1, 1)

        self.input_gfunc_integration = QComboBox(self.tab_additional_stats)
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.addItem("")
        self.input_gfunc_integration.setObjectName(u"input_gfunc_integration")
        self.input_gfunc_integration.setMinimumSize(QSize(150, 40))
        self.input_gfunc_integration.setFont(font1)

        self.gridLayout_8.addWidget(self.input_gfunc_integration, 5, 0, 1, 1)

        self.label_56 = QLabel(self.tab_additional_stats)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(150, 40))
        self.label_56.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_56, 0, 0, 1, 1)

        self.label_125 = QLabel(self.tab_additional_stats)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(150, 40))
        self.label_125.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_8.addWidget(self.label_125, 11, 0, 1, 1)

        self.textinput_wigner_x = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_x.setObjectName(u"textinput_wigner_x")
        self.textinput_wigner_x.setMinimumSize(QSize(150, 40))
        self.textinput_wigner_x.setFont(font1)
        self.textinput_wigner_x.setFrame(True)
        self.textinput_wigner_x.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_x, 9, 2, 1, 1)

        self.input_gfunc_order = QComboBox(self.tab_additional_stats)
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.addItem("")
        self.input_gfunc_order.setObjectName(u"input_gfunc_order")
        self.input_gfunc_order.setMinimumSize(QSize(150, 40))
        self.input_gfunc_order.setFont(font1)

        self.gridLayout_8.addWidget(self.input_gfunc_order, 3, 0, 1, 1)

        self.textinput_wigner_modes = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_modes.setObjectName(u"textinput_wigner_modes")
        self.textinput_wigner_modes.setMinimumSize(QSize(150, 40))
        self.textinput_wigner_modes.setFont(font1)
        self.textinput_wigner_modes.setFrame(True)
        self.textinput_wigner_modes.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_modes, 8, 2, 1, 1)

        self.label_title_set_wigner = QLabel(self.tab_additional_stats)
        self.label_title_set_wigner.setObjectName(u"label_title_set_wigner")
        self.label_title_set_wigner.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_wigner.setFrameShape(QFrame.NoFrame)
        self.label_title_set_wigner.setFrameShadow(QFrame.Plain)

        self.gridLayout_8.addWidget(self.label_title_set_wigner, 7, 0, 1, 10)

        self.textinput_wigner_resolution = QLineEdit(self.tab_additional_stats)
        self.textinput_wigner_resolution.setObjectName(u"textinput_wigner_resolution")
        self.textinput_wigner_resolution.setMinimumSize(QSize(150, 40))
        self.textinput_wigner_resolution.setFont(font1)
        self.textinput_wigner_resolution.setFrame(True)
        self.textinput_wigner_resolution.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.textinput_wigner_resolution, 11, 2, 1, 1)

        self.button_next_tab_stats_to_detector = QPushButton(self.tab_additional_stats)
        self.button_next_tab_stats_to_detector.setObjectName(u"button_next_tab_stats_to_detector")
        self.button_next_tab_stats_to_detector.setMinimumSize(QSize(150, 40))
        self.button_next_tab_stats_to_detector.setCheckable(False)

        self.gridLayout_8.addWidget(self.button_next_tab_stats_to_detector, 14, 8, 1, 1)

        self.text_output_list_of_wigner_funcs = QListView(self.tab_additional_stats)
        self.text_output_list_of_wigner_funcs.setObjectName(u"text_output_list_of_wigner_funcs")

        self.gridLayout_8.addWidget(self.text_output_list_of_wigner_funcs, 8, 8, 6, 1)

        self.button_add_gfunc_to_output = QPushButton(self.tab_additional_stats)
        self.button_add_gfunc_to_output.setObjectName(u"button_add_gfunc_to_output")
        self.button_add_gfunc_to_output.setMinimumSize(QSize(150, 40))
        self.button_add_gfunc_to_output.setFont(font)

        self.gridLayout_8.addWidget(self.button_add_gfunc_to_output, 6, 0, 1, 5)

        self.tabWidget.addTab(self.tab_additional_stats, "")
        self.tab_detector = QWidget()
        self.tab_detector.setObjectName(u"tab_detector")
        self.gridLayout_9 = QGridLayout(self.tab_detector)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.button_next_tab_detector_to_generate = QPushButton(self.tab_detector)
        self.button_next_tab_detector_to_generate.setObjectName(u"button_next_tab_detector_to_generate")
        self.button_next_tab_detector_to_generate.setMinimumSize(QSize(150, 40))
        self.button_next_tab_detector_to_generate.setCheckable(False)

        self.gridLayout_9.addWidget(self.button_next_tab_detector_to_generate, 11, 9, 1, 1)

        self.label_121 = QLabel(self.tab_detector)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setMinimumSize(QSize(150, 40))
        self.label_121.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_121, 8, 0, 1, 1)

        self.textinput_detector_wnum = QLineEdit(self.tab_detector)
        self.textinput_detector_wnum.setObjectName(u"textinput_detector_wnum")
        self.textinput_detector_wnum.setMinimumSize(QSize(150, 40))
        self.textinput_detector_wnum.setFont(font1)
        self.textinput_detector_wnum.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_detector_wnum.setFrame(True)
        self.textinput_detector_wnum.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wnum, 9, 1, 1, 1)

        self.textinput_detector_t0 = QLineEdit(self.tab_detector)
        self.textinput_detector_t0.setObjectName(u"textinput_detector_t0")
        self.textinput_detector_t0.setMinimumSize(QSize(150, 40))
        self.textinput_detector_t0.setFont(font1)
        self.textinput_detector_t0.setStyleSheet(u"border-radius: 0px;")
        self.textinput_detector_t0.setFrame(True)
        self.textinput_detector_t0.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_t0, 1, 1, 1, 1)

        self.label_118 = QLabel(self.tab_detector)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setMinimumSize(QSize(150, 40))
        self.label_118.setMaximumSize(QSize(16777215, 40))
        self.label_118.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_118, 3, 0, 1, 1)

        self.button_add_detector_spectral = QPushButton(self.tab_detector)
        self.button_add_detector_spectral.setObjectName(u"button_add_detector_spectral")
        self.button_add_detector_spectral.setMinimumSize(QSize(150, 40))
        self.button_add_detector_spectral.setFont(font)

        self.gridLayout_9.addWidget(self.button_add_detector_spectral, 11, 0, 1, 1)

        self.label_120 = QLabel(self.tab_detector)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setMinimumSize(QSize(150, 40))
        self.label_120.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_120, 10, 0, 1, 1)

        self.label_117 = QLabel(self.tab_detector)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setMinimumSize(QSize(150, 40))
        self.label_117.setMaximumSize(QSize(16777215, 40))
        self.label_117.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_117, 1, 0, 1, 1)

        self.label_title_set_detector_2 = QLabel(self.tab_detector)
        self.label_title_set_detector_2.setObjectName(u"label_title_set_detector_2")
        self.label_title_set_detector_2.setMinimumSize(QSize(0, 40))
        self.label_title_set_detector_2.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector_2.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector_2.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_set_detector_2, 6, 0, 1, 10)

        self.textinput_detector_wcenter = QLineEdit(self.tab_detector)
        self.textinput_detector_wcenter.setObjectName(u"textinput_detector_wcenter")
        self.textinput_detector_wcenter.setMinimumSize(QSize(150, 40))
        self.textinput_detector_wcenter.setFont(font1)
        self.textinput_detector_wcenter.setStyleSheet(u"border-radius: 0px;")
        self.textinput_detector_wcenter.setFrame(True)
        self.textinput_detector_wcenter.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wcenter, 8, 1, 1, 1)

        self.label_119 = QLabel(self.tab_detector)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setMinimumSize(QSize(150, 40))
        self.label_119.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_119, 7, 0, 1, 1)

        self.label_127 = QLabel(self.tab_detector)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(150, 40))
        self.label_127.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_127, 9, 0, 1, 1)

        self.textinput_detector_wpower = QLineEdit(self.tab_detector)
        self.textinput_detector_wpower.setObjectName(u"textinput_detector_wpower")
        self.textinput_detector_wpower.setMinimumSize(QSize(150, 40))
        self.textinput_detector_wpower.setFont(font1)
        self.textinput_detector_wpower.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_detector_wpower.setFrame(True)
        self.textinput_detector_wpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wpower, 10, 1, 1, 1)

        self.text_output_list_of_detector_spec = QListView(self.tab_detector)
        self.text_output_list_of_detector_spec.setObjectName(u"text_output_list_of_detector_spec")

        self.gridLayout_9.addWidget(self.text_output_list_of_detector_spec, 7, 2, 4, 8)

        self.label_title_set_detector = QLabel(self.tab_detector)
        self.label_title_set_detector.setObjectName(u"label_title_set_detector")
        self.label_title_set_detector.setMinimumSize(QSize(0, 40))
        self.label_title_set_detector.setMaximumSize(QSize(16777215, 40))
        self.label_title_set_detector.setFrameShape(QFrame.NoFrame)
        self.label_title_set_detector.setFrameShadow(QFrame.Plain)

        self.gridLayout_9.addWidget(self.label_title_set_detector, 0, 0, 1, 10)

        self.textinput_detector_tpower = QLineEdit(self.tab_detector)
        self.textinput_detector_tpower.setObjectName(u"textinput_detector_tpower")
        self.textinput_detector_tpower.setMinimumSize(QSize(150, 40))
        self.textinput_detector_tpower.setFont(font1)
        self.textinput_detector_tpower.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_detector_tpower.setFrame(True)
        self.textinput_detector_tpower.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_tpower, 3, 1, 1, 1)

        self.textinput_detector_wrange = QLineEdit(self.tab_detector)
        self.textinput_detector_wrange.setObjectName(u"textinput_detector_wrange")
        self.textinput_detector_wrange.setMinimumSize(QSize(150, 40))
        self.textinput_detector_wrange.setFont(font1)
        self.textinput_detector_wrange.setStyleSheet(u"border-radius: 0px;")
        self.textinput_detector_wrange.setFrame(True)
        self.textinput_detector_wrange.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_wrange, 7, 1, 1, 1)

        self.textinput_detector_t1 = QLineEdit(self.tab_detector)
        self.textinput_detector_t1.setObjectName(u"textinput_detector_t1")
        self.textinput_detector_t1.setMinimumSize(QSize(150, 40))
        self.textinput_detector_t1.setFont(font1)
        self.textinput_detector_t1.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_detector_t1.setFrame(True)
        self.textinput_detector_t1.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.textinput_detector_t1, 2, 1, 1, 1)

        self.label_128 = QLabel(self.tab_detector)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(150, 40))
        self.label_128.setMaximumSize(QSize(16777215, 40))
        self.label_128.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_9.addWidget(self.label_128, 2, 0, 1, 1)

        self.button_add_detector_time = QPushButton(self.tab_detector)
        self.button_add_detector_time.setObjectName(u"button_add_detector_time")
        self.button_add_detector_time.setMinimumSize(QSize(150, 40))
        self.button_add_detector_time.setFont(font)

        self.gridLayout_9.addWidget(self.button_add_detector_time, 4, 0, 1, 1)

        self.text_output_list_of_detector_time = QListView(self.tab_detector)
        self.text_output_list_of_detector_time.setObjectName(u"text_output_list_of_detector_time")

        self.gridLayout_9.addWidget(self.text_output_list_of_detector_time, 1, 3, 3, 7)

        self.tabWidget.addTab(self.tab_detector, "")
        self.tab_generate = QWidget()
        self.tab_generate.setObjectName(u"tab_generate")
        self.gridLayout_10 = QGridLayout(self.tab_generate)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.input_add_output_detecotrtrafo = QCheckBox(self.tab_generate)
        self.input_add_output_detecotrtrafo.setObjectName(u"input_add_output_detecotrtrafo")
        self.input_add_output_detecotrtrafo.setMinimumSize(QSize(150, 40))
        self.input_add_output_detecotrtrafo.setFont(font)
        self.input_add_output_detecotrtrafo.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_detecotrtrafo, 12, 7, 1, 1)

        self.button_run_program = QPushButton(self.tab_generate)
        self.button_run_program.setObjectName(u"button_run_program")
        self.button_run_program.setEnabled(True)
        self.button_run_program.setMinimumSize(QSize(150, 40))
        self.button_run_program.setFont(font)
        self.button_run_program.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4501e, stop:0.91 #8d2f13)}")
        self.button_run_program.setCheckable(False)
        self.button_run_program.setChecked(False)

        self.gridLayout_10.addWidget(self.button_run_program, 3, 2, 1, 1)

        self.button_next_tab_statistics_to_run = QPushButton(self.tab_generate)
        self.button_next_tab_statistics_to_run.setObjectName(u"button_next_tab_statistics_to_run")
        self.button_next_tab_statistics_to_run.setMinimumSize(QSize(150, 40))
        self.button_next_tab_statistics_to_run.setCheckable(False)

        self.gridLayout_10.addWidget(self.button_next_tab_statistics_to_run, 16, 7, 1, 1)

        self.text_output_program_qdlc_command = QTextBrowser(self.tab_generate)
        self.text_output_program_qdlc_command.setObjectName(u"text_output_program_qdlc_command")
        self.text_output_program_qdlc_command.setFrameShape(QFrame.NoFrame)
        self.text_output_program_qdlc_command.setReadOnly(False)

        self.gridLayout_10.addWidget(self.text_output_program_qdlc_command, 1, 2, 1, 6)

        self.input_add_output_phononcoeffs = QCheckBox(self.tab_generate)
        self.input_add_output_phononcoeffs.setObjectName(u"input_add_output_phononcoeffs")
        self.input_add_output_phononcoeffs.setMinimumSize(QSize(150, 40))
        self.input_add_output_phononcoeffs.setFont(font)
        self.input_add_output_phononcoeffs.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_phononcoeffs, 15, 7, 1, 1)

        self.text_output_program_main = QTextBrowser(self.tab_generate)
        self.text_output_program_main.setObjectName(u"text_output_program_main")
        self.text_output_program_main.setMinimumSize(QSize(700, 0))
        self.text_output_program_main.setFrameShape(QFrame.NoFrame)

        self.gridLayout_10.addWidget(self.text_output_program_main, 1, 0, 16, 1)

        self.input_add_output_vonneumannpath = QCheckBox(self.tab_generate)
        self.input_add_output_vonneumannpath.setObjectName(u"input_add_output_vonneumannpath")
        self.input_add_output_vonneumannpath.setMinimumSize(QSize(150, 40))
        self.input_add_output_vonneumannpath.setFont(font)
        self.input_add_output_vonneumannpath.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_vonneumannpath, 11, 7, 1, 1)

        self.label_58 = QLabel(self.tab_generate)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(150, 40))
        self.label_58.setFrameShape(QFrame.NoFrame)
        self.label_58.setFrameShadow(QFrame.Plain)

        self.gridLayout_10.addWidget(self.label_58, 0, 0, 1, 8)

        self.label_60 = QLabel(self.tab_generate)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(150, 40))

        self.gridLayout_10.addWidget(self.label_60, 2, 7, 1, 1)

        self.button_generate_run = QPushButton(self.tab_generate)
        self.button_generate_run.setObjectName(u"button_generate_run")
        self.button_generate_run.setEnabled(True)
        self.button_generate_run.setMinimumSize(QSize(150, 40))
        self.button_generate_run.setFont(font)
        self.button_generate_run.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #f4771e, stop:0.91 #4f2609)}")
        self.button_generate_run.setCheckable(False)
        self.button_generate_run.setChecked(False)

        self.gridLayout_10.addWidget(self.button_generate_run, 2, 2, 1, 1)

        self.input_add_output_phononj = QCheckBox(self.tab_generate)
        self.input_add_output_phononj.setObjectName(u"input_add_output_phononj")
        self.input_add_output_phononj.setMinimumSize(QSize(150, 40))
        self.input_add_output_phononj.setFont(font)
        self.input_add_output_phononj.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_phononj, 14, 7, 1, 1)

        self.input_logginglevel = QComboBox(self.tab_generate)
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.addItem("")
        self.input_logginglevel.setObjectName(u"input_logginglevel")
        self.input_logginglevel.setMinimumSize(QSize(150, 40))
        self.input_logginglevel.setFont(font1)
        self.input_logginglevel.setFocusPolicy(Qt.WheelFocus)
        self.input_logginglevel.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")

        self.gridLayout_10.addWidget(self.input_logginglevel, 2, 4, 1, 1)

        self.label_62 = QLabel(self.tab_generate)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(150, 40))
        self.label_62.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_62, 2, 3, 1, 1)

        self.input_add_output_greenf = QCheckBox(self.tab_generate)
        self.input_add_output_greenf.setObjectName(u"input_add_output_greenf")
        self.input_add_output_greenf.setMinimumSize(QSize(150, 40))
        self.input_add_output_greenf.setFont(font)
        self.input_add_output_greenf.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_greenf, 13, 7, 1, 1)

        self.line_4 = QFrame(self.tab_generate)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_4, 1, 1, 16, 1)

        self.button_run_external = QPushButton(self.tab_generate)
        self.button_run_external.setObjectName(u"button_run_external")
        self.button_run_external.setEnabled(True)
        self.button_run_external.setMinimumSize(QSize(150, 40))
        self.button_run_external.setFont(font)
        self.button_run_external.setStyleSheet(u"QPushButton {background-color: qlineargradient( x1:0 y1:0, x2:0 y2:1, stop:0.9 #1e6cf4, stop:0.91 #133e8d)}")
        self.button_run_external.setCheckable(False)
        self.button_run_external.setChecked(False)

        self.gridLayout_10.addWidget(self.button_run_external, 4, 2, 1, 1)

        self.input_escape_output_command = QCheckBox(self.tab_generate)
        self.input_escape_output_command.setObjectName(u"input_escape_output_command")
        self.input_escape_output_command.setMinimumSize(QSize(150, 40))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.input_escape_output_command.setFont(font3)
        self.input_escape_output_command.setChecked(False)

        self.gridLayout_10.addWidget(self.input_escape_output_command, 5, 2, 1, 1)

        self.label_63 = QLabel(self.tab_generate)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(150, 40))
        self.label_63.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_63, 3, 3, 1, 1)

        self.input_dm_mode = QComboBox(self.tab_generate)
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.addItem("")
        self.input_dm_mode.setObjectName(u"input_dm_mode")
        self.input_dm_mode.setMinimumSize(QSize(150, 40))
        self.input_dm_mode.setFont(font1)
        self.input_dm_mode.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_mode.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-right-radius: 0px; border-bottom-left-radius: 0px;")
        self.input_dm_mode.setFrame(True)

        self.gridLayout_10.addWidget(self.input_dm_mode, 3, 4, 1, 1)

        self.label_61 = QLabel(self.tab_generate)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(150, 40))
        self.label_61.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_61, 5, 3, 1, 1)

        self.label_64 = QLabel(self.tab_generate)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(150, 40))
        self.label_64.setStyleSheet(u"border-top-right-radius: 0px; border-bottom-right-radius: 0px; border-right-width: 0px")

        self.gridLayout_10.addWidget(self.label_64, 4, 3, 1, 1)

        self.input_dm_frame = QComboBox(self.tab_generate)
        self.input_dm_frame.addItem("")
        self.input_dm_frame.addItem("")
        self.input_dm_frame.setObjectName(u"input_dm_frame")
        self.input_dm_frame.setMinimumSize(QSize(150, 40))
        self.input_dm_frame.setFont(font1)
        self.input_dm_frame.setFocusPolicy(Qt.WheelFocus)
        self.input_dm_frame.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-top-right-radius: 0px; border-bottom-left-radius: 0px; border-top-width: 0px;")
        self.input_dm_frame.setFrame(True)

        self.gridLayout_10.addWidget(self.input_dm_frame, 4, 4, 1, 1)

        self.textinput_cpucores = QLineEdit(self.tab_generate)
        self.textinput_cpucores.setObjectName(u"textinput_cpucores")
        self.textinput_cpucores.setMinimumSize(QSize(150, 40))
        self.textinput_cpucores.setFont(font1)
        self.textinput_cpucores.setStyleSheet(u"border-left-width: 0px; border-top-left-radius: 0px; border-bottom-left-radius: 0px;")
        self.textinput_cpucores.setFrame(True)
        self.textinput_cpucores.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.textinput_cpucores, 5, 4, 1, 1)

        self.input_add_output_eigenvalues = QCheckBox(self.tab_generate)
        self.input_add_output_eigenvalues.setObjectName(u"input_add_output_eigenvalues")
        self.input_add_output_eigenvalues.setMinimumSize(QSize(150, 40))
        self.input_add_output_eigenvalues.setFont(font)
        self.input_add_output_eigenvalues.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_eigenvalues, 3, 7, 1, 1)

        self.input_add_output_operators = QCheckBox(self.tab_generate)
        self.input_add_output_operators.setObjectName(u"input_add_output_operators")
        self.input_add_output_operators.setMinimumSize(QSize(150, 40))
        self.input_add_output_operators.setFont(font)
        self.input_add_output_operators.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_operators, 4, 7, 1, 1)

        self.input_add_output_rkerror = QCheckBox(self.tab_generate)
        self.input_add_output_rkerror.setObjectName(u"input_add_output_rkerror")
        self.input_add_output_rkerror.setMinimumSize(QSize(150, 40))
        self.input_add_output_rkerror.setFont(font)
        self.input_add_output_rkerror.setChecked(False)

        self.gridLayout_10.addWidget(self.input_add_output_rkerror, 5, 7, 1, 1)

        self.tabWidget.addTab(self.tab_generate, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.label_3 = QLabel(self.tab_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(380, 275, 751, 241))
        font4 = QFont()
        font4.setPointSize(26)
        font4.setBold(True)
        self.label_3.setFont(font4)
        self.label_3.setWordWrap(True)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.label_4 = QLabel(self.tab_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(400, 220, 751, 241))
        self.label_4.setFont(font4)
        self.label_4.setWordWrap(True)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.label_8 = QLabel(self.tab_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(425, 270, 751, 241))
        self.label_8.setFont(font4)
        self.label_8.setWordWrap(True)
        self.tabWidget.addTab(self.tab_8, "")

        self.gridLayout_11.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1455, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        self.menuMenu.setGeometry(QRect(471, 217, 190, 94))
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionLoad_QDLC_Command)
        self.menuMenu.addAction(self.actionExport_QDLC_Command)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.input_phonons_approximation.setCurrentIndex(1)
        self.input_rungekutta_order.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"QDLC Generator", None))
        self.actionLoad_QDLC_Command.setText(QCoreApplication.translate("MainWindow", u"Import QDLC Command", None))
        self.actionExport_QDLC_Command.setText(QCoreApplication.translate("MainWindow", u"Export QDLC Command", None))
        self.button_add_cavity.setText(QCoreApplication.translate("MainWindow", u"Cavity", None))
        self.button_input_system_redraw.setText(QCoreApplication.translate("MainWindow", u"Redraw", None))
        self.button_modify_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.button_modify_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_modify_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.button_add_electronic_shift.setText(QCoreApplication.translate("MainWindow", u"Chirp", None))
#if QT_CONFIG(statustip)
        self.input_draw_details.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_draw_details.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Add...</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Editing</span></p></body></html>", None))
        self.label_output_system.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.button_add_optical_pulse.setText(QCoreApplication.translate("MainWindow", u"Pulse", None))
        self.label_title_qdsystem.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">QD System</span></p></body></html>", None))
        self.button_next_tab_system_to_config.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_add_electronic_state.setText(QCoreApplication.translate("MainWindow", u"State", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_system), QCoreApplication.translate("MainWindow", u"System", None))
        self.button_reset_phonon_sd.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_title_adjust_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Adjust Rates</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the radiative decay loss using the formula gamma_rad = gamma_rad*<B>", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_radiativeloss.setText(QCoreApplication.translate("MainWindow", u"Radiative Loss", None))
        self.textinput_phonons_sd_qd_dh.setText(QCoreApplication.translate("MainWindow", u"-3.5eV", None))
        self.label_title_rates.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Rates</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Phonon Coupling</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Loss</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Quantum Dot</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Delta</span></p></body></html>", None))
        self.button_reset_phonon_qd.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.textinput_phonons_sd_alpha.setText(QCoreApplication.translate("MainWindow", u"0.03E-24", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Density Plot</span></p></body></html>", None))
        self.label_title_phonons_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">PME Settings</span></p></body></html>", None))
        self.label_plot_lindblad_rates.setText("")
        self.textinput_phonons_sd_wcutoff.setText(QCoreApplication.translate("MainWindow", u"1meV", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setStatusTip(QCoreApplication.translate("MainWindow", u"a_e/a_h ratio", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_aeah_ratio.setText(QCoreApplication.translate("MainWindow", u"1.15", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Cutoff</span></p></body></html>", None))
        self.textinput_phonons_sd_ohmamp.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Hole Energy</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Speed of Sound</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.input_phonons_adjust_renormalization.setToolTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setStatusTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_renormalization.setText(QCoreApplication.translate("MainWindow", u"Renormalization", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Cavity Coupling</span></p></body></html>", None))
        self.textinput_rates_radiative_decay.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_rates_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is kg/m^3", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_rho.setText(QCoreApplication.translate("MainWindow", u"5370", None))
        self.input_phonons_approximation.setItemText(0, QCoreApplication.translate("MainWindow", u"Full", None))
        self.input_phonons_approximation.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrixexponential", None))
        self.input_phonons_approximation.setItemText(2, QCoreApplication.translate("MainWindow", u"Omit Transformation", None))
        self.input_phonons_approximation.setItemText(3, QCoreApplication.translate("MainWindow", u"Analytical Rates", None))
        self.input_phonons_approximation.setItemText(4, QCoreApplication.translate("MainWindow", u"Hybrid", None))

        self.input_phonons_use_qd.setText(QCoreApplication.translate("MainWindow", u"Use QD Parameters Instead of PME Settings", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">E-H Ratio</span></p></body></html>", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Integral Stepsize</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">QD Size</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Ohm</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Electron Energy</span></p></body></html>", None))
        self.textinput_phonons_sd_tcutoff.setText(QCoreApplication.translate("MainWindow", u"4ps", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Radiative Loss</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Temperature</span></p></body></html>", None))
        self.textinput_phonons_sd_wdelta.setText(QCoreApplication.translate("MainWindow", u"0.01meV", None))
        self.label_title_phonons.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Environment (Phonons)</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setStatusTip(QCoreApplication.translate("MainWindow", u"Typical Values lie around 3nm to 6nm", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_size.setText(QCoreApplication.translate("MainWindow", u"3nm", None))
        self.label_title_phonons_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Phonon Integral</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Material Density</span></p></body></html>", None))
        self.button_reset_rates.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Approximation</span></p></body></html>", None))
        self.button_reset_phonons_3.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.button_reset_phonons_2.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Pure Dephasing</span></p></body></html>", None))
        self.label_title_phonons_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">QD Settings</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Cutoff</span></p></body></html>", None))
        self.textinput_phonons_temperature.setText(QCoreApplication.translate("MainWindow", u"No Phonons", None))
        self.textinput_rates_cavity_coupling.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_rates_cavity_loss.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_phonons_iterator_stepsize.setText(QCoreApplication.translate("MainWindow", u"auto", None))
#if QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setStatusTip(QCoreApplication.translate("MainWindow", u"Unit is m/s", None))
#endif // QT_CONFIG(statustip)
        self.textinput_phonons_sd_qd_cs.setText(QCoreApplication.translate("MainWindow", u"5110", None))
#if QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setStatusTip(QCoreApplication.translate("MainWindow", u"Adjusts the pure dephasing rate using the formula pure_dephasing = 1mueV/K * temperature. This effect is quite strong and should probably not be used.", None))
#endif // QT_CONFIG(statustip)
        self.input_phonons_adjust_pure_dephasing.setText(QCoreApplication.translate("MainWindow", u"Pure Dephasing", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">QD Rates</span></p></body></html>", None))
        self.label_plot_spectral_density.setText("")
        self.button_reset_phonons.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.textinput_phonons_sd_qd_de.setText(QCoreApplication.translate("MainWindow", u"7eV", None))
        self.button_next_tab_config_to_timeline.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_environment), QCoreApplication.translate("MainWindow", u"Environment", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Grid Expander</span></p></body></html>", None))
        self.label_title_time.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Time</span></p></body></html>", None))
        self.textinput_phonons_tsteppath.setText(QCoreApplication.translate("MainWindow", u"auto", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_grid.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_grid.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_grid.setText(QCoreApplication.translate("MainWindow", u"Gridresolution", None))
        self.input_rungekutta_order.setItemText(0, QCoreApplication.translate("MainWindow", u"Variable Timestep Runge Kutta Dormand Prince", None))
        self.input_rungekutta_order.setItemText(1, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 4", None))
        self.input_rungekutta_order.setItemText(2, QCoreApplication.translate("MainWindow", u"Fixed Timestep Runge-Kutta Order 5", None))
        self.input_rungekutta_order.setItemText(3, QCoreApplication.translate("MainWindow", u"Path Integral (PSADM IQUAPI)", None))

        self.textinput_phonons_nc.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(tooltip)
        self.button_time_config_tol.setToolTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_time_config_tol.setStatusTip(QCoreApplication.translate("MainWindow", u"Configure a grid instead", None))
#endif // QT_CONFIG(statustip)
        self.button_time_config_tol.setText(QCoreApplication.translate("MainWindow", u"Tolerance", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Main Solver</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Time Step</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the actual temporal evolution. This disables the phonon interactions, such that calculations are fast.", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate Time", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI NC</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">PI Stepsize</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_timeline_enable_phonons.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_timeline_enable_phonons.setText(QCoreApplication.translate("MainWindow", u"Disable Phonons", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">End Time</span></p></body></html>", None))
        self.textinput_time_endtime.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_title_solver.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Solver</span></p></body></html>", None))
        self.input_interpolator_t.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.input_interpolator_t.setItemText(1, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_t.setItemText(2, QCoreApplication.translate("MainWindow", u"Bicubic", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_t.setStatusTip(QCoreApplication.translate("MainWindow", u"Main Direction Interpolator. If None, no interpolation will be used, meaning the main time output has non-equidistant elements", None))
#endif // QT_CONFIG(statustip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Starting Time</span></p></body></html>", None))
        self.textinput_time_gridresolution.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.textinput_time_gridresolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.input_interpolator_tau.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.input_interpolator_tau.setItemText(1, QCoreApplication.translate("MainWindow", u"Bicubic", None))

#if QT_CONFIG(statustip)
        self.input_interpolator_tau.setStatusTip(QCoreApplication.translate("MainWindow", u"Tau-Direction Interpolator which expands the time calculations onto an equidistant grid. Usually linear is sufficient.", None))
#endif // QT_CONFIG(statustip)
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Interpolator</span></p></body></html>", None))
        self.textinput_time_startingtime.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.textinput_time_tolerance.setText(QCoreApplication.translate("MainWindow", u"1E-6", None))
        self.textinput_time_tolerance.setPlaceholderText(QCoreApplication.translate("MainWindow", u"None", None))
        self.textinput_time_timestep.setText(QCoreApplication.translate("MainWindow", u"auto", None))
        self.label_title_predicted_timeline.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Timeline</span></p></body></html>", None))
        self.button_next_tab_timeline_to_spectrum.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_timeline), QCoreApplication.translate("MainWindow", u"Timeline", None))
        self.textinput_spectrum_range.setText("")
        self.textinput_spectrum_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"2meV", None))
        self.input_spectrum_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_spectrum_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.button_add_spectrum_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.textinput_spectrum_modes.setText("")
        self.textinput_spectrum_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B,c", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Normalize</span></p></body></html>", None))
        self.label_title_predicted_spectral.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Predicted Spectral Properties</span></p></body></html>", None))
        self.label_title_set_spectrum.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectrum</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">List of Modes</span></p></body></html>", None))
        self.button_next_tab_spectrum_to_indist.setText(QCoreApplication.translate("MainWindow", u"Next", None))
#if QT_CONFIG(tooltip)
        self.input_spectrum_normalize.setToolTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_spectrum_normalize.setStatusTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(statustip)
        self.input_spectrum_normalize.setText(QCoreApplication.translate("MainWindow", u"To 1", None))
        self.textinput_spectrum_range_2.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.textinput_spectrum_range_2.setPlaceholderText("")
        self.button_add_spectrum_to_output_3.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
#if QT_CONFIG(statustip)
        self.input_timeline_enable_phonons_2.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_timeline_enable_phonons_2.setText(QCoreApplication.translate("MainWindow", u"Disable Phonons", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.textinput_spectrum_center.setText("")
        self.textinput_spectrum_center.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1eV", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Correlation</span></p></body></html>", None))
        self.button_time_config_grid_3.setText(QCoreApplication.translate("MainWindow", u"Time Grid", None))
#if QT_CONFIG(statustip)
        self.button_timeline_force_calculate_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the actual spectral properties using a small spectral window. This disables the phonon interactions, such that calculations are fast.", None))
#endif // QT_CONFIG(statustip)
        self.button_timeline_force_calculate_2.setText(QCoreApplication.translate("MainWindow", u"Calculate Spectra", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_spectrum), QCoreApplication.translate("MainWindow", u"Spectrum", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Mode</span></p></body></html>", None))
        self.label_title_set_indists_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">List of Indistinguishabilities to calculate</span></p></body></html>", None))
        self.textinput_indist_modes.setText("")
        self.textinput_indist_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.button_next_tab_indist_to_conc.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_title_set_indists.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Indistinguishabilities</span></p></body></html>", None))
        self.button_remove_indist_from_output.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.button_add_indist_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_indist), QCoreApplication.translate("MainWindow", u"Indistinguishability", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Range</span></p></body></html>", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">G2 Spectra</span></p></body></html>", None))
        self.button_next_tab_sconc_to_stats.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Second Mode</span></p></body></html>", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Center</span></p></body></html>", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">First Mode</span></p></body></html>", None))
        self.button_add_concurrence_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.button_add_concurrence_to_output_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_title_set_concurrences.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Concurrences</span></p></body></html>", None))
        self.textinput_concurrence_first.setText("")
        self.textinput_concurrence_first.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B+B=D", None))
        self.textinput_concurrence_second.setText("")
        self.textinput_concurrence_second.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=C+C=D", None))
        self.label_title_set_concurrences_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectral Properties</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.input_concurrence_add_spectra.setToolTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.input_concurrence_add_spectra.setStatusTip(QCoreApplication.translate("MainWindow", u"Enables the renomalization of the polaron shifted energies and rates, e.g. using the <B> and <B>^2 scalings", None))
#endif // QT_CONFIG(statustip)
        self.input_concurrence_add_spectra.setText(QCoreApplication.translate("MainWindow", u"All", None))
#if QT_CONFIG(statustip)
        self.textinput_concurrence_spec_freq.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the spectrum for all of the used G2 functions. Check the Box to edit these values", None))
#endif // QT_CONFIG(statustip)
        self.textinput_concurrence_spec_freq.setText("")
        self.textinput_concurrence_spec_freq.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.textinput_concurrence_spec_range.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the spectrum for all of the used G2 functions. Check the Box to edit these values", None))
#endif // QT_CONFIG(statustip)
        self.textinput_concurrence_spec_range.setText("")
        self.textinput_concurrence_spec_range.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(statustip)
        self.textinput_concurrence_spec_res.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate the spectrum for all of the used G2 functions. Check the Box to edit these values", None))
#endif // QT_CONFIG(statustip)
        self.textinput_concurrence_spec_res.setText("")
        self.textinput_concurrence_spec_res.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_concurrence), QCoreApplication.translate("MainWindow", u"Concurrence", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Skip</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_wigner_modes_y.setStatusTip(QCoreApplication.translate("MainWindow", u"Alpha in -Y:Y range", None))
#endif // QT_CONFIG(statustip)
        self.textinput_wigner_modes_y.setText("")
        self.textinput_wigner_modes_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">X</span></p></body></html>", None))
        self.textinput_correlation_modes.setText("")
        self.textinput_correlation_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B, c", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Outputmethod</span></p></body></html>", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Modes</span></p></body></html>", None))
        self.button_add_wigner.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Y</span></p></body></html>", None))
        self.textinput_wigner_skip.setText("")
        self.textinput_wigner_skip.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Order</span></p></body></html>", None))
        self.input_gfunc_integration.setItemText(0, QCoreApplication.translate("MainWindow", u"Integrated", None))
        self.input_gfunc_integration.setItemText(1, QCoreApplication.translate("MainWindow", u"Matrix", None))
        self.input_gfunc_integration.setItemText(2, QCoreApplication.translate("MainWindow", u"Both", None))

        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">List of Modes</span></p></body></html>", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Resolution</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.textinput_wigner_x.setStatusTip(QCoreApplication.translate("MainWindow", u"Alpha in -X:X range", None))
#endif // QT_CONFIG(statustip)
        self.textinput_wigner_x.setText("")
        self.textinput_wigner_x.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.input_gfunc_order.setItemText(0, QCoreApplication.translate("MainWindow", u"G1", None))
        self.input_gfunc_order.setItemText(1, QCoreApplication.translate("MainWindow", u"G2", None))

        self.textinput_wigner_modes.setText("")
        self.textinput_wigner_modes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A=B,c", None))
        self.label_title_set_wigner.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Wigner Function</span></p></body></html>", None))
        self.textinput_wigner_resolution.setText("")
        self.textinput_wigner_resolution.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button_next_tab_stats_to_detector.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.button_add_gfunc_to_output.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_additional_stats), QCoreApplication.translate("MainWindow", u"Additional Statistics", None))
        self.button_next_tab_detector_to_generate.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Center</span></p></body></html>", None))
        self.textinput_detector_wnum.setText("")
        self.textinput_detector_wnum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"fourier points", None))
        self.textinput_detector_t0.setText("")
        self.textinput_detector_t0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.button_add_detector_spectral.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Falloff Power</span></p></body></html>", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Starting Time</span></p></body></html>", None))
        self.label_title_set_detector_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Spectral Measurement Window</span></p></body></html>", None))
        self.textinput_detector_wcenter.setText("")
        self.textinput_detector_wcenter.setPlaceholderText(QCoreApplication.translate("MainWindow", u"center", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Spectral Range</span></p></body></html>", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Fourier Points</span></p></body></html>", None))
        self.textinput_detector_wpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_wpower.setPlaceholderText("")
        self.label_title_set_detector.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Temporal Measurement Window</span></p></body></html>", None))
        self.textinput_detector_tpower.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.textinput_detector_tpower.setPlaceholderText("")
        self.textinput_detector_wrange.setText("")
        self.textinput_detector_wrange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"range", None))
        self.textinput_detector_t1.setText("")
        self.textinput_detector_t1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"end", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">End Time</span></p></body></html>", None))
        self.button_add_detector_time.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_detector), QCoreApplication.translate("MainWindow", u"Detector", None))
#if QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_detecotrtrafo.setText(QCoreApplication.translate("MainWindow", u"Detectorfunctions", None))
        self.button_run_program.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.button_next_tab_statistics_to_run.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.text_output_program_qdlc_command.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_qdlc_command.setPlaceholderText(QCoreApplication.translate("MainWindow", u"./QDLC.exe ...", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononcoeffs.setText(QCoreApplication.translate("MainWindow", u"Phononcoefficients", None))
        self.text_output_program_main.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.text_output_program_main.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output", None))
#if QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_vonneumannpath.setText(QCoreApplication.translate("MainWindow", u"von Neumann Path", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Generate QDLC Command and Run</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Output</span></p></body></html>", None))
        self.button_generate_run.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(statustip)
        self.input_add_output_phononj.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_phononj.setText(QCoreApplication.translate("MainWindow", u"Phonon Spectral J", None))
        self.input_logginglevel.setItemText(0, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.input_logginglevel.setItemText(1, QCoreApplication.translate("MainWindow", u"Additional", None))
        self.input_logginglevel.setItemText(2, QCoreApplication.translate("MainWindow", u"Verbose", None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Logging Level</span></p></body></html>", None))
#if QT_CONFIG(statustip)
        self.input_add_output_greenf.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_greenf.setText(QCoreApplication.translate("MainWindow", u"Greenfunctions", None))
        self.button_run_external.setText(QCoreApplication.translate("MainWindow", u"Run on Noctua", None))
#if QT_CONFIG(statustip)
        self.input_escape_output_command.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_escape_output_command.setText(QCoreApplication.translate("MainWindow", u"Escape Output", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Density Matrix</span></p></body></html>", None))
        self.input_dm_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"No Output", None))
        self.input_dm_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Diagonal Elements", None))
        self.input_dm_mode.setItemText(2, QCoreApplication.translate("MainWindow", u"Full Matrix", None))

        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">CPU Cores</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Frame</span></p></body></html>", None))
        self.input_dm_frame.setItemText(0, QCoreApplication.translate("MainWindow", u"Heisenberg", None))
        self.input_dm_frame.setItemText(1, QCoreApplication.translate("MainWindow", u"Schr\u00f6dinger", None))

        self.textinput_cpucores.setText(QCoreApplication.translate("MainWindow", u"all", None))
#if QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_eigenvalues.setText(QCoreApplication.translate("MainWindow", u"Eigenvalues", None))
#if QT_CONFIG(statustip)
        self.input_add_output_operators.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_operators.setText(QCoreApplication.translate("MainWindow", u"Operator Matrices", None))
#if QT_CONFIG(statustip)
        self.input_add_output_rkerror.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.input_add_output_rkerror.setText(QCoreApplication.translate("MainWindow", u"Runge-Kutta Error", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_generate), QCoreApplication.translate("MainWindow", u"Generate and Run", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">add ability to change different parameters using lambda expressions, generate output settings file. add goto run button and run sweep</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Sweep and Scan", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Plot stuff</p><p align=\"center\">matrix plot, evaluation (enpoints, then plot, etc.)</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Plotting", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Parameter optimization.</p><p align=\"center\">print runscript, let user change parameters to {0}, {1}, etc. then set parameter limits</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Optimization", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

