# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'credentials.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import app_data


class Ui_credentials(QtWidgets.QDialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def setupUi(self, credentials):
		credentials.setObjectName("credentials")
		credentials.resize(360, 240)
		credentials.setMinimumSize(QtCore.QSize(360, 240))
		credentials.setMaximumSize(QtCore.QSize(360, 240))
		self.formLayoutWidget = QtWidgets.QWidget(credentials)
		self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 221))
		self.formLayoutWidget.setObjectName("formLayoutWidget")
		self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
		self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
		self.formLayout.setContentsMargins(0, 0, 0, 0)
		self.formLayout.setObjectName("formLayout")
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")
		self.key_id_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.key_id_label.setObjectName("key_id_label")
		self.verticalLayout.addWidget(self.key_id_label)
		self.access_key_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.access_key_label.setObjectName("access_key_label")
		self.verticalLayout.addWidget(self.access_key_label)
		self.region_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.region_label.setObjectName("region_label")
		self.verticalLayout.addWidget(self.region_label)
		self.in_bucket_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.in_bucket_label.setObjectName("in_bucket_label")
		self.verticalLayout.addWidget(self.in_bucket_label)
		self.out_bucket_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.out_bucket_label.setObjectName("out_bucket_label")
		self.verticalLayout.addWidget(self.out_bucket_label)
		self.encrypt_label = QtWidgets.QLabel(self.formLayoutWidget)
		self.encrypt_label.setObjectName("encrypt_label")
		self.verticalLayout.addWidget(self.encrypt_label)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.aws_access_key_id = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.aws_access_key_id.setObjectName("aws_access_key_id")
		self.verticalLayout_2.addWidget(self.aws_access_key_id)
		self.aws_secret_access_key = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.aws_secret_access_key.setObjectName("aws_secret_access_key")
		self.verticalLayout_2.addWidget(self.aws_secret_access_key)
		self.region = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.region.setObjectName("region")
		self.verticalLayout_2.addWidget(self.region)
		self.in_bucket = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.in_bucket.setObjectName("in_bucket")
		self.verticalLayout_2.addWidget(self.in_bucket)
		self.out_bucket = QtWidgets.QLineEdit(self.formLayoutWidget)
		self.out_bucket.setObjectName("out_bucket")
		self.verticalLayout_2.addWidget(self.out_bucket)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.encrypt_true = QtWidgets.QCheckBox(self.formLayoutWidget)
		self.encrypt_true.setObjectName("encrypt_true")
		self.horizontalLayout.addWidget(self.encrypt_true)
		self.verticalLayout_2.addLayout(self.horizontalLayout)
		self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
		self.buttonBox = QtWidgets.QDialogButtonBox(self.formLayoutWidget)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
		spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)

		self.retranslateUi(credentials)
		self.buttonBox.accepted.connect(credentials.accept_val)
		self.buttonBox.rejected.connect(credentials.reject)
		QtCore.QMetaObject.connectSlotsByName(credentials)

	def retranslateUi(self, credentials):
		_translate = QtCore.QCoreApplication.translate
		credentials.setWindowTitle(_translate("credentials", "AWS Credentials"))
		self.key_id_label.setText(_translate("credentials", "AWS_ACCESS_KEY_ID"))
		self.access_key_label.setText(_translate("credentials", "AWS_SECRET_ACCESS_KEY"))
		self.region_label.setText(_translate("credentials", "REGION"))
		self.in_bucket_label.setText(_translate("credentials", "IN_BUCKET"))
		self.out_bucket_label.setText(_translate("credentials", "OUT_BUCKET"))
		self.encrypt_true.setText(_translate("credentials", "Encrypt"))

	def accept_val(self):
		if self.aws_access_key_id.text() == '' or self.region.text() == '' or self.aws_secret_access_key.text() == '' or self.in_bucket.text() == '' or self.out_bucket.text() == '':
			print 'Not possible'
			self.accept()
		else:
			params = {}
			params['aws_access_key_id'] = self.aws_access_key_id.text()
			params['aws_secret_access_key'] = self.aws_secret_access_key.text()
			params['region'] = self.region.text()
			params['in_bucket'] = self.in_bucket.text()
			params['out_bucket'] = self.out_bucket.text()
			if self.encrypt_true.isChecked() is True:
				params['encrypt_cred'] = '1'
			else:
				params['encrypt_cred'] = '0'
			app_data.set_credentials_cred(params)
			self.accept()
