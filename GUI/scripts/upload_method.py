# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'method.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import hyve_A
import app_data


class Ui_upload_method(QtWidgets.QDialog):
	def __init__(self, progressBar, console, success_count, error_count):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)
		self.progressBar = progressBar
		self.console = console
		self.success_count = success_count
		self.error_count = error_count

	def setupUi(self, upload_method):
		upload_method.setObjectName("upload_method")
		upload_method.resize(384, 95)
		self.horizontalLayoutWidget = QtWidgets.QWidget(upload_method)
		self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 321, 71))
		self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.m1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.m1.setMinimumSize(QtCore.QSize(0, 60))
		self.m1.setObjectName("m1")
		self.horizontalLayout.addWidget(self.m1)
		self.m2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
		self.m2.setMinimumSize(QtCore.QSize(0, 60))
		self.m2.setObjectName("m2")
		self.horizontalLayout.addWidget(self.m2)

		self.retranslateUi(upload_method)
		self.m1.clicked.connect(self.method1)
		self.m2.clicked.connect(self.method2)
		QtCore.QMetaObject.connectSlotsByName(upload_method)

	def retranslateUi(self, upload_method):
		_translate = QtCore.QCoreApplication.translate
		upload_method.setWindowTitle(_translate("upload_method", "Choose a method"))
		self.m1.setText(_translate("upload_method", "Upload by Selecting From List"))
		self.m2.setText(_translate("upload_method", "Upload By Comparing Buckets"))

	def method1(self):
		hyve_A.upload_method_cycle()

	def method2(self):
		hyve_A.upload_method_0(app_data.get_credentials(), self.progressBar, self.console, self.success_count, self.error_count)
