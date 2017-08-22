# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatedb.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_data


class Ui_Dialog(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(403, 220)
		self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
		self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 371, 179))
		self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
		self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
		self.checkBox.setObjectName("checkBox")
		self.horizontalLayout.addWidget(self.checkBox)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
		self.checkBox_2.setObjectName("checkBox_2")
		self.horizontalLayout_2.addWidget(self.checkBox_2)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.horizontalLayout_3.addWidget(self.label_3)
		self.textEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
		self.textEdit.setObjectName("textEdit")
		self.horizontalLayout_3.addWidget(self.textEdit)
		self.verticalLayout_2.addLayout(self.horizontalLayout_3)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout_2.addWidget(self.buttonBox)
		self.verticalLayoutWidget.raise_()
		self.checkBox_2.raise_()
		self.checkBox.raise_()
		self.checkBox_2.raise_()

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept_val)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.checkBox.setText(_translate("Dialog", "Execute query"))
		self.checkBox_2.setText(_translate("Dialog", "Mail The Script"))
		self.label_3.setText(_translate("Dialog", "Recipient\'s"))

	def accept_val(self):
		if self.textEdit.toPlainText() == '' and self.checkBox_2.isChecked() is True:
			print 'Not possible'
			self.accept()
		else:
			params = {}
			params['mail_recipients'] = self.textEdit.toPlainText()
			if self.checkBox.isChecked() is True:
				params['execute_query'] = '1'
			else:
				params['execute_query'] = '0'
			if self.checkBox_2.isChecked() is True:
				params['send_mail'] = '1'
			else:
				params['send_mail'] = '0'
			app_data.set_credentials_update_db(params)
			self.accept()
