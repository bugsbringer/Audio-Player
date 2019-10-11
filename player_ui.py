# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(405, 391)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.minimizeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeButton.sizePolicy().hasHeightForWidth())
        self.minimizeButton.setSizePolicy(sizePolicy)
        self.minimizeButton.setMinimumSize(QtCore.QSize(32, 25))
        self.minimizeButton.setMaximumSize(QtCore.QSize(32, 25))
        self.minimizeButton.setMouseTracking(True)
        self.minimizeButton.setAutoFillBackground(False)
        self.minimizeButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.minimizeButton.setText("")
        self.minimizeButton.setIconSize(QtCore.QSize(12, 12))
        self.minimizeButton.setFlat(False)
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout.addWidget(self.minimizeButton)
        self.maximizeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximizeButton.sizePolicy().hasHeightForWidth())
        self.maximizeButton.setSizePolicy(sizePolicy)
        self.maximizeButton.setMinimumSize(QtCore.QSize(32, 25))
        self.maximizeButton.setMaximumSize(QtCore.QSize(32, 25))
        self.maximizeButton.setMouseTracking(True)
        self.maximizeButton.setAutoFillBackground(False)
        self.maximizeButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.maximizeButton.setText("")
        self.maximizeButton.setIconSize(QtCore.QSize(14, 14))
        self.maximizeButton.setFlat(False)
        self.maximizeButton.setObjectName("maximizeButton")
        self.horizontalLayout.addWidget(self.maximizeButton)
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setMinimumSize(QtCore.QSize(32, 25))
        self.closeButton.setMaximumSize(QtCore.QSize(32, 25))
        self.closeButton.setMouseTracking(True)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.closeButton.setText("")
        self.closeButton.setIconSize(QtCore.QSize(12, 12))
        self.closeButton.setFlat(False)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 5, 5, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clearListButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearListButton.sizePolicy().hasHeightForWidth())
        self.clearListButton.setSizePolicy(sizePolicy)
        self.clearListButton.setMinimumSize(QtCore.QSize(32, 24))
        self.clearListButton.setMaximumSize(QtCore.QSize(100, 24))
        self.clearListButton.setMouseTracking(True)
        self.clearListButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.clearListButton.setText("")
        self.clearListButton.setFlat(False)
        self.clearListButton.setObjectName("clearListButton")
        self.horizontalLayout_6.addWidget(self.clearListButton)
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(32, 24, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.searchInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchInput.sizePolicy().hasHeightForWidth())
        self.searchInput.setSizePolicy(sizePolicy)
        self.searchInput.setMinimumSize(QtCore.QSize(180, 22))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setItalic(False)
        font.setKerning(True)
        self.searchInput.setFont(font)
        self.searchInput.setMaxLength(32)
        self.searchInput.setFrame(True)
        self.searchInput.setAlignment(QtCore.Qt.AlignCenter)
        self.searchInput.setClearButtonEnabled(False)
        self.searchInput.setObjectName("searchInput")
        self.horizontalLayout_8.addWidget(self.searchInput)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(32, 24))
        self.searchButton.setMaximumSize(QtCore.QSize(32, 24))
        self.searchButton.setMouseTracking(True)
        self.searchButton.setStyleSheet("*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.searchButton.setText("")
        self.searchButton.setFlat(False)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout_8.addWidget(self.searchButton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setMinimumSize(QtCore.QSize(32, 24))
        self.downloadButton.setMaximumSize(QtCore.QSize(32, 24))
        self.downloadButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.downloadButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.downloadButton.setText("")
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_6.addWidget(self.downloadButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.playlistView = QtWidgets.QListView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playlistView.sizePolicy().hasHeightForWidth())
        self.playlistView.setSizePolicy(sizePolicy)
        self.playlistView.setAutoFillBackground(False)
        self.playlistView.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playlistView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.playlistView.setLineWidth(0)
        self.playlistView.setAutoScrollMargin(16)
        self.playlistView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.playlistView.setDragEnabled(False)
        self.playlistView.setDragDropOverwriteMode(False)
        self.playlistView.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.playlistView.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.playlistView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.playlistView.setIconSize(QtCore.QSize(16, 16))
        self.playlistView.setViewMode(QtWidgets.QListView.ListMode)
        self.playlistView.setObjectName("playlistView")
        self.verticalLayout_3.addWidget(self.playlistView)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mediaName = QtWidgets.QLabel(self.centralwidget)
        self.mediaName.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.mediaName.setFont(font)
        self.mediaName.setText("")
        self.mediaName.setObjectName("mediaName")
        self.horizontalLayout_9.addWidget(self.mediaName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.currentTime = QtWidgets.QLabel(self.centralwidget)
        self.currentTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentTime.setObjectName("currentTime")
        self.horizontalLayout_2.addWidget(self.currentTime)
        self.timeSlider = QtWidgets.QSlider(self.centralwidget)
        self.timeSlider.setMaximum(600)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setObjectName("timeSlider")
        self.horizontalLayout_2.addWidget(self.timeSlider)
        self.totalTime = QtWidgets.QLabel(self.centralwidget)
        self.totalTime.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.totalTime.setObjectName("totalTime")
        self.horizontalLayout_2.addWidget(self.totalTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prevButton.sizePolicy().hasHeightForWidth())
        self.prevButton.setSizePolicy(sizePolicy)
        self.prevButton.setMinimumSize(QtCore.QSize(32, 0))
        self.prevButton.setMouseTracking(True)
        self.prevButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.prevButton.setText("")
        self.prevButton.setIconSize(QtCore.QSize(20, 20))
        self.prevButton.setFlat(False)
        self.prevButton.setObjectName("prevButton")
        self.horizontalLayout_7.addWidget(self.prevButton)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(32, 0))
        self.playButton.setMouseTracking(True)
        self.playButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.playButton.setText("")
        self.playButton.setIconSize(QtCore.QSize(20, 20))
        self.playButton.setCheckable(False)
        self.playButton.setAutoDefault(False)
        self.playButton.setDefault(False)
        self.playButton.setFlat(False)
        self.playButton.setObjectName("playButton")
        self.horizontalLayout_7.addWidget(self.playButton)
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setMinimumSize(QtCore.QSize(32, 0))
        self.nextButton.setMouseTracking(True)
        self.nextButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.nextButton.setText("")
        self.nextButton.setIconSize(QtCore.QSize(20, 20))
        self.nextButton.setFlat(False)
        self.nextButton.setObjectName("nextButton")
        self.horizontalLayout_7.addWidget(self.nextButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_7)
        spacerItem5 = QtWidgets.QSpacerItem(13, 23, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.repeatButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeatButton.sizePolicy().hasHeightForWidth())
        self.repeatButton.setSizePolicy(sizePolicy)
        self.repeatButton.setMinimumSize(QtCore.QSize(32, 0))
        self.repeatButton.setMouseTracking(True)
        self.repeatButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}\n"
"*:checked{\n"
"    border: 2px solid rgb(100,100,100) ;\n"
"}")
        self.repeatButton.setText("")
        self.repeatButton.setIconSize(QtCore.QSize(16, 16))
        self.repeatButton.setCheckable(True)
        self.repeatButton.setChecked(False)
        self.repeatButton.setFlat(False)
        self.repeatButton.setObjectName("repeatButton")
        self.horizontalLayout_4.addWidget(self.repeatButton)
        self.shuffleButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shuffleButton.sizePolicy().hasHeightForWidth())
        self.shuffleButton.setSizePolicy(sizePolicy)
        self.shuffleButton.setMinimumSize(QtCore.QSize(32, 0))
        self.shuffleButton.setMouseTracking(True)
        self.shuffleButton.setAutoFillBackground(False)
        self.shuffleButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}\n"
"*:checked{\n"
"    border: 2px solid rgb(100,100,100) ;\n"
"}")
        self.shuffleButton.setText("")
        self.shuffleButton.setIconSize(QtCore.QSize(16, 16))
        self.shuffleButton.setCheckable(True)
        self.shuffleButton.setChecked(False)
        self.shuffleButton.setFlat(False)
        self.shuffleButton.setObjectName("shuffleButton")
        self.horizontalLayout_4.addWidget(self.shuffleButton)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.volumeButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeButton.sizePolicy().hasHeightForWidth())
        self.volumeButton.setSizePolicy(sizePolicy)
        self.volumeButton.setMinimumSize(QtCore.QSize(32, 0))
        self.volumeButton.setMouseTracking(True)
        self.volumeButton.setStyleSheet("*{\n"
"    background-color: rgba(53, 53, 53, 0);\n"
"    border: none;\n"
"}\n"
"*:hover{\n"
"    background-color: rgb(76,76,76);\n"
"}")
        self.volumeButton.setText("")
        self.volumeButton.setIconSize(QtCore.QSize(20, 20))
        self.volumeButton.setCheckable(False)
        self.volumeButton.setChecked(False)
        self.volumeButton.setDefault(False)
        self.volumeButton.setFlat(False)
        self.volumeButton.setObjectName("volumeButton")
        self.horizontalLayout_5.addWidget(self.volumeButton)
        self.volumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.volumeSlider.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setSingleStep(100)
        self.volumeSlider.setPageStep(100)
        self.volumeSlider.setProperty("value", 50)
        self.volumeSlider.setSliderPosition(50)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setInvertedAppearance(False)
        self.volumeSlider.setInvertedControls(False)
        self.volumeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.volumeSlider.setTickInterval(10)
        self.volumeSlider.setObjectName("volumeSlider")
        self.horizontalLayout_5.addWidget(self.volumeSlider)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        spacerItem7 = QtWidgets.QSpacerItem(13, 26, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusBar.sizePolicy().hasHeightForWidth())
        self.statusBar.setSizePolicy(sizePolicy)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actiondownload_folder = QtWidgets.QAction(MainWindow)
        self.actiondownload_folder.setObjectName("actiondownload_folder")

        self.retranslateUi(MainWindow)
        self.searchInput.returnPressed.connect(self.searchButton.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.playButton, self.searchInput)
        MainWindow.setTabOrder(self.searchInput, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.prevButton)
        MainWindow.setTabOrder(self.prevButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.repeatButton)
        MainWindow.setTabOrder(self.repeatButton, self.shuffleButton)
        MainWindow.setTabOrder(self.shuffleButton, self.volumeButton)
        MainWindow.setTabOrder(self.volumeButton, self.minimizeButton)
        MainWindow.setTabOrder(self.minimizeButton, self.maximizeButton)
        MainWindow.setTabOrder(self.maximizeButton, self.volumeSlider)
        MainWindow.setTabOrder(self.volumeSlider, self.closeButton)
        MainWindow.setTabOrder(self.closeButton, self.timeSlider)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MediaPlayer"))
        self.clearListButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Clear playlist</p></body></html>"))
        self.searchInput.setPlaceholderText(_translate("MainWindow", "Search music online"))
        self.searchButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Search</p></body></html>"))
        self.downloadButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Download selected tracks</p></body></html>"))
        self.currentTime.setText(_translate("MainWindow", "0:00"))
        self.totalTime.setText(_translate("MainWindow", "0:00"))
        self.prevButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Previous</p></body></html>"))
        self.playButton.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Play</p></body></html>"))
        self.nextButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Next</p></body></html>"))
        self.repeatButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Repeat current</p></body></html>"))
        self.shuffleButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Shuffle</p></body></html>"))
        self.volumeButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Mute</p></body></html>"))
        self.actiondownload_folder.setText(_translate("MainWindow", "download folder"))

