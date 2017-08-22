# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sync.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_data


class Ui_SyncwithS3(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def setupUi(self, SyncwithS3):
		SyncwithS3.setObjectName("SyncwithS3")
		SyncwithS3.resize(434, 156)
		self.formLayoutWidget = QtWidgets.QWidget(SyncwithS3)
		self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 391, 104))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.dest_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.dest_label.setObjectName("dest_label")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.dest_label)
		self.dest = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.dest.setObjectName("dest")
		self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dest)
		self.source = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.source.setObjectName("source")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.source)
		self.exclude_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.exclude_label.setObjectName("exclude_label")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.exclude_label)
		self.exclude = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.exclude.setObjectName("exclude")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.exclude)
		self.source_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.source_label.setObjectName("source_label")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.source_label)
		self.buttonBox = QtWidgets.QDialogButtonBox(SyncwithS3)
		self.buttonBox.setGeometry(QtCore.QRect(120, 120, 291, 27))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")

		self.retranslateUi(SyncwithS3)
		self.buttonBox.accepted.connect(SyncwithS3.accept_val)
		self.buttonBox.rejected.connect(SyncwithS3.reject)
		QtCore.QMetaObject.connectSlotsByName(SyncwithS3)

	def retranslateUi(self, SyncwithS3):
		_translate = QtCore.QCoreApplication.translate
		SyncwithS3.setWindowTitle(_translate("SyncwithS3", "Sync with S3"))
		self.dest_label.setText(_translate("SyncwithS3", "Destination"))
		self.dest.setPlaceholderText(_translate("SyncwithS3", "destination url Eg: s3://xyz"))
		self.source.setPlaceholderText(_translate("SyncwithS3", "Source url (absolute path)"))
		self.exclude_label.setText(_translate("SyncwithS3", "Exclude"))
		self.exclude.setPlaceholderText(_translate("SyncwithS3", "Separate values by comma"))
		self.source_label.setText(_translate("SyncwithS3", "Source"))

	def accept_val(self):
		if self.dest.text() == '' or self.source.text() == '' or self.exclude.text() == '':
			print 'Not possible'
			self.accept()
		else:
			params = {}
			params['exclude_cards'] = self.exclude.text()
			params['destination'] = self.dest.text()
			params['source'] = self.source.text()
			app_data.set_credentials_sync_s3(params)
			self.accept()
