# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import connection
import credential
import edit_upload
import sync_s3
import update_db
import hyve_A
import app_data
import upload_method


class Ui_MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 500)
		MainWindow.setMinimumSize(QtCore.QSize(800, 500))
		MainWindow.setMaximumSize(QtCore.QSize(800, 500))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 456))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")
		self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
		self.progressBar.setProperty("value", 0)
		self.progressBar.setObjectName("progressBar")
		self.gridLayout.addWidget(self.progressBar, 2, 0, 1, 1)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.sync_od_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.sync_od_1.setMinimumSize(QtCore.QSize(0, 50))
		self.icon = QtGui.QIcon()
		self.icon.addPixmap(QtGui.QPixmap("icons/1_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.sync_od_1.setIcon(self.icon)
		self.sync_od_1.setObjectName("sync_od_1")
		self.horizontalLayout.addWidget(self.sync_od_1)
		self.upload_od_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.upload_od_2.setMinimumSize(QtCore.QSize(0, 50))
		self.icon1 = QtGui.QIcon()
		self.icon1.addPixmap(QtGui.QPixmap("icons/2_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.upload_od_2.setIcon(self.icon1)
		self.upload_od_2.setObjectName("upload_od_2")
		self.horizontalLayout.addWidget(self.upload_od_2)
		self.update_od_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.update_od_3.setMinimumSize(QtCore.QSize(0, 50))
		self.icon2 = QtGui.QIcon()
		self.icon2.addPixmap(QtGui.QPixmap("icons/3_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.update_od_3.setIcon(self.icon2)
		self.update_od_3.setObjectName("update_od_3")
		self.horizontalLayout.addWidget(self.update_od_3)
		self.line = QtWidgets.QFrame(self.gridLayoutWidget)
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.horizontalLayout.addWidget(self.line)
		self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton.setMinimumSize(QtCore.QSize(0, 50))
		self.pushButton.setObjectName("pushButton")
		self.horizontalLayout.addWidget(self.pushButton)
		self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_5.setMinimumSize(QtCore.QSize(0, 50))
		self.pushButton_5.setObjectName("pushButton_5")
		self.horizontalLayout.addWidget(self.pushButton_5)
		self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.horizontalLayout.addWidget(self.line_2)
		self.success_count = QtWidgets.QLCDNumber(self.gridLayoutWidget)
		self.success_count.setObjectName("success_count")
		self.horizontalLayout.addWidget(self.success_count)
		self.error_count = QtWidgets.QLCDNumber(self.gridLayoutWidget)
		self.error_count.setObjectName("error_count")
		self.horizontalLayout.addWidget(self.error_count)
		self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
		self.console = QtWidgets.QTextBrowser(self.gridLayoutWidget)
		self.console.setMinimumSize(QtCore.QSize(0, 250))
		self.console.setObjectName("console")
		self.gridLayout.addWidget(self.console, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
		self.menubar.setObjectName("menubar")
		self.menuFile = QtWidgets.QMenu(self.menubar)
		self.menuFile.setObjectName("menuFile")
		self.menuOptions = QtWidgets.QMenu(self.menubar)
		self.menuOptions.setObjectName("menuOptions")
		self.menuHelp = QtWidgets.QMenu(self.menubar)
		self.menuHelp.setObjectName("menuHelp")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.actionNew_Connection = QtWidgets.QAction(MainWindow)
		self.actionNew_Connection.setObjectName("actionNew_Connection")
		self.actionNew_Credentials = QtWidgets.QAction(MainWindow)
		self.actionNew_Credentials.setObjectName("actionNew_Credentials")
		self.actionExit = QtWidgets.QAction(MainWindow)
		self.actionExit.setObjectName("actionExit")
		self.actionSync_with_S3 = QtWidgets.QAction(MainWindow)
		self.actionSync_with_S3.setObjectName("actionSync_with_S3")
		self.actionEdit_and_Upload = QtWidgets.QAction(MainWindow)
		self.actionEdit_and_Upload.setObjectName("actionEdit_and_Upload")
		self.actionUpdate_DB = QtWidgets.QAction(MainWindow)
		self.actionUpdate_DB.setObjectName("actionUpdate_DB")
		self.actionCopy_Fields = QtWidgets.QAction(MainWindow)
		self.actionCopy_Fields.setObjectName("actionCopy_Fields")
		self.actionScan_Storage = QtWidgets.QAction(MainWindow)
		self.actionScan_Storage.setObjectName("actionScan_Storage")
		self.actionDocs = QtWidgets.QAction(MainWindow)
		self.actionDocs.setObjectName("actionDocs")
		self.actionAbout = QtWidgets.QAction(MainWindow)
		self.actionAbout.setObjectName("actionAbout")
		self.menuFile.addAction(self.actionNew_Connection)
		self.menuFile.addAction(self.actionNew_Credentials)
		self.menuFile.addSeparator()
		self.menuFile.addAction(self.actionExit)
		self.menuOptions.addAction(self.actionSync_with_S3)
		self.menuOptions.addAction(self.actionEdit_and_Upload)
		self.menuOptions.addAction(self.actionUpdate_DB)
		self.menuOptions.addSeparator()
		self.menuOptions.addAction(self.actionCopy_Fields)
		self.menuOptions.addAction(self.actionScan_Storage)
		self.menuHelp.addAction(self.actionDocs)
		self.menuHelp.addAction(self.actionAbout)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuOptions.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(MainWindow)
		self.actionNew_Connection.triggered.connect(self.open_connection_widget)
		self.actionNew_Credentials.triggered.connect(self.open_credential_widget)
		self.actionEdit_and_Upload.triggered.connect(self.open_edit_upload_widget)
		self.actionSync_with_S3.triggered.connect(self.open_sync_s3_widget)
		self.actionUpdate_DB.triggered.connect(self.open_update_db_widget)
		self.sync_od_1.clicked.connect(self.od1)
		self.upload_od_2.clicked.connect(self.od2)
		self.update_od_3.clicked.connect(self.od3)
		self.actionExit.triggered.connect(self.exit_app)
		self.sync_od_1.clicked.connect(self.console.clear)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.sync_od_1.setText(_translate("MainWindow", "Sync with S3"))
		self.upload_od_2.setText(_translate("MainWindow", "Edit and Upload"))
		self.update_od_3.setText(_translate("MainWindow", "Update DB"))
		self.pushButton.setText(_translate("MainWindow", "Copy Fields"))
		self.pushButton_5.setText(_translate("MainWindow", "Scan Storage"))
		self.menuFile.setTitle(_translate("MainWindow", "File"))
		self.menuOptions.setTitle(_translate("MainWindow", "Options"))
		self.menuHelp.setTitle(_translate("MainWindow", "Help"))
		self.actionNew_Connection.setText(_translate("MainWindow", "New Connection"))
		self.actionNew_Credentials.setText(_translate("MainWindow", "New Credentials"))
		self.actionExit.setText(_translate("MainWindow", "Exit"))
		self.actionSync_with_S3.setText(_translate("MainWindow", "Sync with S3"))
		self.actionEdit_and_Upload.setText(_translate("MainWindow", "Edit and Upload"))
		self.actionUpdate_DB.setText(_translate("MainWindow", "Update DB"))
		self.actionCopy_Fields.setText(_translate("MainWindow", "Copy Fields"))
		self.actionScan_Storage.setText(_translate("MainWindow", "Scan Storage"))
		self.actionDocs.setText(_translate("MainWindow", "Docs"))
		self.actionAbout.setText(_translate("MainWindow", "About"))

	def exit_app(self):
		import sys
		sys.exit()

	def open_connection_widget(self):
		con_widget = connection.Ui_connection_settings()
		con_widget.exec_()

	def open_credential_widget(self):
		cred_widget = credential.Ui_credentials()
		cred_widget.exec_()

	def open_edit_upload_widget(self):
		edit_upload_widget = edit_upload.Ui_edit_upload()
		edit_upload_widget.exec_()

	def open_sync_s3_widget(self):
		sync_s3_widget = sync_s3.Ui_SyncwithS3()
		sync_s3_widget.exec_()

	def open_update_db_widget(self):
		update_db_widget = update_db.Ui_Dialog()
		update_db_widget.exec_()

	def od1(self):
		self.sync_od_1.setDisabled(1)
		self.upload_od_2.setDisabled(1)
		self.update_od_3.setDisabled(1)
		hyve_A.sync_s3_method_1(app_data.get_credentials(), self.progressBar, self.console, self.success_count, self.error_count)
		self.sync_od_1.setDisabled(0)
		self.upload_od_2.setDisabled(0)
		self.update_od_3.setDisabled(0)

	def od2(self):
		self.sync_od_1.setDisabled(1)
		self.upload_od_2.setDisabled(1)
		self.update_od_3.setDisabled(1)
		hyve_A.upload_method_0(app_data.get_credentials(), self.progressBar, self.console, self.success_count, self.error_count)
		# method_dialog = upload_method.Ui_upload_method(self.progressBar, self.console, self.success_count, self.error_count)
		# method_dialog.exec_()
		self.sync_od_1.setDisabled(0)
		self.upload_od_2.setDisabled(0)
		self.update_od_3.setDisabled(0)

	def od3(self):
		self.sync_od_1.setDisabled(1)
		self.upload_od_2.setDisabled(1)
		self.update_od_3.setDisabled(1)
		hyve_A.update_db_method_3(app_data.get_credentials(), self.progressBar, self.console, self.success_count, self.error_count)
		self.sync_od_1.setDisabled(0)
		self.upload_od_2.setDisabled(0)
		self.update_od_3.setDisabled(0)
