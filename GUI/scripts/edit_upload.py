# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_upload.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_data


class Ui_edit_upload(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def setupUi(self, edit_upload):
		edit_upload.setObjectName("edit_upload")
		edit_upload.resize(620, 180)
		edit_upload.setMinimumSize(QtCore.QSize(620, 180))
		edit_upload.setMaximumSize(QtCore.QSize(620, 180))
		self.formLayoutWidget = QtWidgets.QWidget(edit_upload)
		self.formLayoutWidget.setGeometry(QtCore.QRect(16, 20, 591, 144))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.label = QtWidgets.QLabel(self.formLayoutWidget)
		self.label.setObjectName("label")
		self.verticalLayout.addWidget(self.label)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
		self.radioButton_2.setChecked(True)
		self.radioButton_2.setObjectName("radioButton_2")
		self.horizontalLayout.addWidget(self.radioButton_2)
		self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
		self.radioButton.setObjectName("radioButton")
		self.horizontalLayout.addWidget(self.radioButton)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.buttonBox)

		self.retranslateUi(edit_upload)
		self.buttonBox.accepted.connect(edit_upload.accept_val)
		self.buttonBox.rejected.connect(edit_upload.reject)
		QtCore.QMetaObject.connectSlotsByName(edit_upload)

	def retranslateUi(self, edit_upload):
		_translate = QtCore.QCoreApplication.translate
		edit_upload.setWindowTitle(_translate("edit_upload", "Edit & Upload"))
		self.label.setText(_translate("edit_upload", "Choose a procedure"))
		self.radioButton_2.setText(_translate("edit_upload", "Upload from Iron IO"))
		self.radioButton.setText(_translate("edit_upload", "Upload from Local"))

	def accept_val(self):
		params = {}
		if self.radioButton_2.isChecked() is True:
			params['use_iron'] = '1'
		else:
			params['use_iron'] = '0'
		app_data.set_credentials_iron(params)
		self.accept()
