# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_data


class Ui_connection_settings(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def setupUi(self, connection_settings):
		connection_settings.setObjectName("connection_settings")
		connection_settings.resize(360, 250)
		connection_settings.setMinimumSize(QtCore.QSize(360, 250))
		connection_settings.setMaximumSize(QtCore.QSize(360, 250))
		self.formLayoutWidget = QtWidgets.QWidget(connection_settings)
		self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 221))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.host_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.host_label.setObjectName("host_label")
		self.verticalLayout_2.addWidget(self.host_label)
		self.user_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.user_label.setObjectName("user_label")
		self.verticalLayout_2.addWidget(self.user_label)
		self.password_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.password_label.setObjectName("password_label")
		self.verticalLayout_2.addWidget(self.password_label)
		self.db_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.db_label.setObjectName("db_label")
		self.verticalLayout_2.addWidget(self.db_label)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.host_name = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.host_name.setText("")
		self.host_name.setObjectName("host_name")
		self.verticalLayout.addWidget(self.host_name)
		self.user_name = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.user_name.setText("")
		self.user_name.setObjectName("user_name")
		self.verticalLayout.addWidget(self.user_name)
		self.password = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.password.setInputMask("")
		self.password.setText("")
		self.password.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
		self.password.setObjectName("password")
		self.verticalLayout.addWidget(self.password)
		self.db_name = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.db_name.setText("")
		self.db_name.setObjectName("db_name")
		self.verticalLayout.addWidget(self.db_name)
		self.table_name = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.table_name.setText("")
		self.table_name.setObjectName("table_name")
		self.verticalLayout.addWidget(self.table_name)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.encrypt_true = QtWidgets.QCheckBox(self.formLayoutWidget)
		self.encrypt_true.setObjectName("encrypt_true")
		self.horizontalLayout.addWidget(self.encrypt_true)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)

		self.retranslateUi(connection_settings)
		self.buttonBox.accepted.connect(connection_settings.accept_val)
		self.buttonBox.rejected.connect(connection_settings.reject)
		QtCore.QMetaObject.connectSlotsByName(connection_settings)

	def retranslateUi(self, connection_settings):
		_translate = QtCore.QCoreApplication.translate
		connection_settings.setWindowTitle(_translate("connection_settings", "Connection Settings"))
		self.host_label.setText(_translate("connection_settings", "Host Name"))
		self.user_label.setText(_translate("connection_settings", "User Name"))
		self.password_label.setText(_translate("connection_settings", "Password"))
		self.db_label.setText(_translate("connection_settings", "DB Name"))
		self.encrypt_true.setText(_translate("connection_settings", "Encrypt"))

	def accept_val(self):
		if self.host_name.text() == '' or self.password.text() == '' or self.user_name.text() == '':
			print 'Not possible'
			self.accept()
		else:
			params = {}
			params['host_name'] = self.host_name.text()
			params['user_name'] = self.user_name.text()
			params['password'] = self.password.text()
			params['db_name'] = self.db_name.text()
			if self.encrypt_true.isChecked() is True:
				params['encrypt_conn'] = '1'
			else:
				params['encrypt_conn'] = '0'
			app_data.set_credentials_conn(params)
			self.accept()
