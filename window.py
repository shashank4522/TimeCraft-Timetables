

from PyQt5 import QtCore, QtGui, QtWidgets
import lightstyle

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(799, 460)
        window.setStyleSheet(lightstyle.css)
        window.setWindowIcon(QtGui.QIcon('icons/logo.ico'))
        self.centralWidget = QtWidgets.QWidget(window)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 11, 3, 0)
        self.gridLayout.setHorizontalSpacing(9)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 12, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.centralWidget)
        self.addBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.addBtn.setFont(font)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.electiveBtn = QtWidgets.QPushButton(self.centralWidget)
        self.electiveBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.electiveBtn.setFont(font)
        self.electiveBtn.setObjectName("electiveBtn")
        self.horizontalLayout.addWidget(self.electiveBtn)
        self.removeBtn = QtWidgets.QPushButton(self.centralWidget)
        self.removeBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.removeBtn.setFont(font)
        self.removeBtn.setObjectName("removeBtn")
        self.horizontalLayout.addWidget(self.removeBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.nextBtn = QtWidgets.QPushButton(self.centralWidget)
        self.nextBtn.setMinimumSize(QtCore.QSize(120, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 13, 0, 1, 7)
        self.label = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 7, QtCore.Qt.AlignHCenter)
        self.title_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_combobox.sizePolicy().hasHeightForWidth())
        self.title_combobox.setSizePolicy(sizePolicy)
        self.title_combobox.setMinimumSize(QtCore.QSize(70, 40))
        self.title_combobox.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title_combobox.setFont(font)
        self.title_combobox.setObjectName("title_combobox")
        self.gridLayout.addWidget(self.title_combobox, 9, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 10, 1, 1, 1)
        self.subject_code_input = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_code_input.sizePolicy().hasHeightForWidth())
        self.subject_code_input.setSizePolicy(sizePolicy)
        self.subject_code_input.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_code_input.setFont(font)
        self.subject_code_input.setObjectName("subject_code_input")
        self.gridLayout.addWidget(self.subject_code_input, 11, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 3, 1, 1)
        self.credits_spinbox = QtWidgets.QSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.credits_spinbox.sizePolicy().hasHeightForWidth())
        self.credits_spinbox.setSizePolicy(sizePolicy)
        self.credits_spinbox.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.credits_spinbox.setFont(font)
        self.credits_spinbox.setProperty("value", 1)
        self.credits_spinbox.setObjectName("credits_spinbox")
        self.gridLayout.addWidget(self.credits_spinbox, 11, 3, 1, 1)
        self.lab_checkbox = QtWidgets.QCheckBox(self.centralWidget)
        self.lab_checkbox.setMinimumSize(QtCore.QSize(45, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        self.lab_checkbox.setFont(font)
        self.lab_checkbox.setObjectName("lab_checkbox")
        self.gridLayout.addWidget(self.lab_checkbox, 11, 4, 1, 1)
        self.sections_spinbox = QtWidgets.QSpinBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sections_spinbox.sizePolicy().hasHeightForWidth())
        self.sections_spinbox.setSizePolicy(sizePolicy)
        self.sections_spinbox.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sections_spinbox.setFont(font)
        self.sections_spinbox.setProperty("value", 1)
        self.sections_spinbox.setObjectName("sections_spinbox")
        self.gridLayout.addWidget(self.sections_spinbox, 6, 2, 1, 1)
        self.semester_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semester_combobox.sizePolicy().hasHeightForWidth())
        self.semester_combobox.setSizePolicy(sizePolicy)
        self.semester_combobox.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.semester_combobox.setFont(font)
        self.semester_combobox.setObjectName("semester_combobox")
        self.gridLayout.addWidget(self.semester_combobox, 6, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setMinimumSize(QtCore.QSize(0, 0))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 7, 0, 1, 5)
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setMinimumSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 5)
        self.input_list = QtWidgets.QListWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_list.sizePolicy().hasHeightForWidth())
        self.input_list.setSizePolicy(sizePolicy)
        self.input_list.setMinimumSize(QtCore.QSize(260, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_list.setFont(font)
        self.input_list.setAlternatingRowColors(True)
        self.input_list.setObjectName("input_list")
        self.gridLayout.addWidget(self.input_list, 1, 5, 12, 2)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 2)
        self.subject_short_input = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subject_short_input.sizePolicy().hasHeightForWidth())
        self.subject_short_input.setSizePolicy(sizePolicy)
        self.subject_short_input.setMinimumSize(QtCore.QSize(125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_short_input.setFont(font)
        self.subject_short_input.setObjectName("subject_short_input")
        self.gridLayout.addWidget(self.subject_short_input, 11, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 10, 2, 1, 1)
        self.inputType_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputType_combobox.sizePolicy().hasHeightForWidth())
        self.inputType_combobox.setSizePolicy(sizePolicy)
        self.inputType_combobox.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.inputType_combobox.setFont(font)
        self.inputType_combobox.setObjectName("inputType_combobox")
        self.gridLayout.addWidget(self.inputType_combobox, 3, 1, 1, 2)
        self.input_textbox = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_textbox.sizePolicy().hasHeightForWidth())
        self.input_textbox.setSizePolicy(sizePolicy)
        self.input_textbox.setMinimumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.input_textbox.setFont(font)
        self.input_textbox.setObjectName("input_textbox")
        self.gridLayout.addWidget(self.input_textbox, 9, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 3, 1, 2)
        self.desig_combobox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.desig_combobox.sizePolicy().hasHeightForWidth())
        self.desig_combobox.setSizePolicy(sizePolicy)
        self.desig_combobox.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.desig_combobox.setFont(font)
        self.desig_combobox.setObjectName("desig_combobox")
        self.gridLayout.addWidget(self.desig_combobox, 9, 3, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        window.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setGeometry(QtCore.QRect(226, 100, 169, 156))
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        window.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(window)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSaveAs = QtWidgets.QAction(window)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSaveAs.setShortcut("Ctrl+Shift+S")
        self.actionLoad = QtWidgets.QAction(window)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut("Ctrl+L")
        self.actionExit = QtWidgets.QAction(window)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(window)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(window)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionClear_All = QtWidgets.QAction(window)
        self.actionClear_All.setObjectName("actionClear_All")
        self.actionClear_All.setShortcut("Ctrl+R")
        self.aboutMenu = QtWidgets.QAction(window)
        self.aboutMenu.setObjectName("aboutMenu")
        self.LicenseMenu = QtWidgets.QAction(window)
        self.LicenseMenu.setObjectName("LicenseMenu")
        self.actionSet_Year_Dept = QtWidgets.QAction(window)
        self.actionSet_Year_Dept.setObjectName("actionSet_Year_Dept")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSet_Year_Dept)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClear_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.aboutMenu)
        self.menuHelp.addAction(self.LicenseMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        window.setTabOrder(self.inputType_combobox, self.semester_combobox)
        window.setTabOrder(self.semester_combobox, self.sections_spinbox)
        window.setTabOrder(self.sections_spinbox, self.title_combobox)
        window.setTabOrder(self.title_combobox, self.input_textbox)
        window.setTabOrder(self.input_textbox, self.desig_combobox)
        window.setTabOrder(self.desig_combobox, self.subject_code_input)
        window.setTabOrder(self.subject_code_input, self.subject_short_input)
        window.setTabOrder(self.subject_short_input, self.credits_spinbox)
        window.setTabOrder(self.credits_spinbox, self.lab_checkbox)
        window.setTabOrder(self.lab_checkbox, self.addBtn)
        window.setTabOrder(self.addBtn, self.input_list)
        window.setTabOrder(self.input_list, self.electiveBtn)
        window.setTabOrder(self.electiveBtn, self.removeBtn)
        window.setTabOrder(self.removeBtn, self.nextBtn)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "TIMECRAFT"))
        self.addBtn.setText(_translate("window", "Add"))
        self.electiveBtn.setText(_translate("window", "Add Elective"))
        self.removeBtn.setText(_translate("window", "Remove"))
        self.nextBtn.setText(_translate("window", "Next"))
        self.label.setText(_translate("window", "List Entry"))
        self.label_8.setText(_translate("window", "Subject code:"))
        self.label_7.setText(_translate("window", "Credits:"))
        self.lab_checkbox.setText(_translate("window", "Lab"))
        self.label_3.setText(_translate("window", "Semester:"))
        self.label_4.setText(_translate("window", "Section:"))
        self.label_2.setText(_translate("window", "Input Type:"))
        self.label_5.setText(_translate("window", "Name:"))
        self.label_6.setText(_translate("window", "Subject short form:"))
        self.label_9.setText(_translate("window", "Designation:"))
        self.menuFile.setTitle(_translate("window", "File"))
        self.menuHelp.setTitle(_translate("window", "Help"))
        self.actionSave.setText(_translate("window", "Save"))
        self.actionSaveAs.setText(_translate("window", "Save As"))
        self.actionLoad.setText(_translate("window", "Load"))
        self.actionExit.setText(_translate("window", "Exit"))
        self.actionAbout.setText(_translate("window", "About"))
        self.actionAbout_2.setText(_translate("window", "About"))
        self.actionClear_All.setText(_translate("window", "Clear All"))
        self.aboutMenu.setText(_translate("window", "About"))
        self.LicenseMenu.setText(_translate("window", "License"))
        self.actionSet_Year_Dept.setText(_translate("window", "Set Year/Department"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
