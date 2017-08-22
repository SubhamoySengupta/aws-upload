from cryptography.fernet import Fernet


def get_credentials():
	key = 'Dt3fyZxiCiuUi8ewCto8DIfsDlvXhaTElqHrrRS3l_c='
	fernet = Fernet(key)
	f = open('resources/app_data', 'r')
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()
		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	if app_data['encrypt_conn'] == '1':
		app_data['HOST_NAME'] = fernet.decrypt(app_data['HOST_NAME'])
		app_data['USER_NAME'] = fernet.decrypt(app_data['USER_NAME'])
		app_data['PASSWORD'] = fernet.decrypt(app_data['PASSWORD'])
		app_data['DB_NAME'] = fernet.decrypt(app_data['DB_NAME'])
	if app_data['encrypt_cred'] == '1':
		app_data['aws_access_key_id'] = fernet.decrypt(app_data['aws_access_key_id'])
		app_data['aws_secret_access_key'] = fernet.decrypt(app_data['aws_secret_access_key'])
		app_data['region'] = fernet.decrypt(app_data['region'])
		app_data['in_bucket'] = fernet.decrypt(app_data['in_bucket'])
		app_data['out_bucket'] = fernet.decrypt(app_data['out_bucket'])
	return app_data


def set_credentials_conn(data):
	key = 'Dt3fyZxiCiuUi8ewCto8DIfsDlvXhaTElqHrrRS3l_c='
	fernet = Fernet(key)
	f = open('resources/app_data', 'r')
	for i in data:
		print i, '==>', data[i]
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()
		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	if data['encrypt_conn'] == '1':
		app_data['HOST_NAME'] = fernet.encrypt(data['host_name'].encode('utf-8'))
		app_data['USER_NAME'] = fernet.encrypt(data['user_name'].encode('utf-8'))
		app_data['PASSWORD'] = fernet.encrypt(data['password'].encode('utf-8'))
		app_data['DB_NAME'] = fernet.encrypt(data['db_name'].encode('utf-8'))
	else:
		app_data['HOST_NAME'] = data['host_name']
		app_data['USER_NAME'] = data['user_name']
		app_data['PASSWORD'] = data['password']
		app_data['DB_NAME'] = data['db_name']
	app_data['encrypt_conn'] = data['encrypt_conn']
	f = open('resources/app_data', 'w')
	for key, value in app_data.iteritems():
		line = key + '=' + value
		f.write(line + '\n')
	f.close()


def set_credentials_cred(data):
	key = 'Dt3fyZxiCiuUi8ewCto8DIfsDlvXhaTElqHrrRS3l_c='
	fernet = Fernet(key)
	f = open('resources/app_data', 'r')
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()

		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail=' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	if data['encrypt_cred'] == '1':
		app_data['aws_access_key_id'] = fernet.encrypt(data['aws_access_key_id'].encode('utf-8'))
		app_data['aws_secret_access_key'] = fernet.encrypt(data['aws_secret_access_key'].encode('utf-8'))
		app_data['region'] = fernet.encrypt(data['region'].encode('utf-8'))
		app_data['in_bucket'] = fernet.encrypt(data['in_bucket'].encode('utf-8'))
		app_data['out_bucket'] = fernet.encrypt(data['out_bucket'].encode('utf-8'))
	else:
		app_data['aws_access_key_id'] = data['aws_access_key_id']
		app_data['aws_secret_access_key'] = data['aws_secret_access_key']
		app_data['region'] = data['region']
		app_data['in_bucket'] = data['in_bucket']
		app_data['out_bucket'] = data['out_bucket']
	app_data['encrypt_cred'] = data['encrypt_cred']
	f = open('resources/app_data', 'w')
	for key in app_data:
		line = key + '=' + app_data[key]
		f.write(line + '\n')
	f.close()


def set_credentials_update_db(data):
	f = open('resources/app_data', 'r')
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()
		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail=' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	app_data['send_mail'] = data['send_mail']
	if data['send_mail'] == '1':
		app_data['mail_recipients'] = data['mail_recipients']
	app_data['execute_query'] = data['execute_query']
	f = open('resources/app_data', 'w')
	for key in app_data:
		line = key + '=' + app_data[key]
		f.write(line + '\n')
	f.close()


def set_credentials_sync_s3(data):
	f = open('resources/app_data', 'r')
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()
		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail=' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	app_data['exclude_cards'] = data['exclude_cards']
	app_data['destination'] = data['destination']
	app_data['source'] = data['source']
	f = open('resources/app_data', 'w')
	for key in app_data:
		line = key + '=' + app_data[key]
		f.write(line + '\n')
	f.close()


def set_credentials_iron(data):
	f = open('resources/app_data', 'r')
	app_data = {}
	for line in f.readlines():
		if 'HOST_NAME=' in line:
			app_data['HOST_NAME'] = line.replace('HOST_NAME=', '').strip()
		elif 'USER_NAME=' in line:
			app_data['USER_NAME'] = line.replace('USER_NAME=', '').strip()
		elif 'PASSWORD=' in line:
			app_data['PASSWORD'] = line.replace('PASSWORD=', '').strip()
		elif 'DB_NAME=' in line:
			app_data['DB_NAME'] = line.replace('DB_NAME=', '').strip()
		elif 'aws_access_key_id=' in line:
			app_data['aws_access_key_id'] = line.replace('aws_access_key_id=', '').strip()
		elif 'aws_secret_access_key=' in line:
			app_data['aws_secret_access_key'] = line.replace('aws_secret_access_key=', '').strip()
		elif 'region=' in line:
			app_data['region'] = line.replace('region=', '').strip()
		elif 'in_bucket=' in line:
			app_data['in_bucket'] = line.replace('in_bucket=', '').strip()
		elif 'out_bucket=' in line:
			app_data['out_bucket'] = line.replace('out_bucket=', '').strip()
		elif 'upload_procedure=' in line:
			app_data['upload_procedure'] = line.replace('upload_procedure=', '').strip()
		elif 'exclude_cards=' in line:
			app_data['exclude_cards'] = line.replace('exclude_cards=', '').strip()
		elif 'mail_recipients=' in line:
			app_data['mail_recipients'] = line.replace('mail_recipients=', '').strip()
		elif 'send_mail=' in line:
			app_data['send_mail'] = line.replace('send_mail=', '').strip()
		elif 'execute_query=' in line:
			app_data['execute_query'] = line.replace('execute_query=', '').strip()
		elif 'encrypt_conn=' in line:
			app_data['encrypt_conn'] = line.replace('encrypt_conn=', '').strip()
		elif 'encrypt_cred=' in line:
			app_data['encrypt_cred'] = line.replace('encrypt_cred=', '').strip()
		elif 'use_iron=' in line:
			app_data['use_iron'] = line.replace('use_iron=', '').strip()
		elif 'destination=' in line:
			app_data['destination'] = line.replace('destination=', '').strip()
		elif 'source=' in line:
			app_data['source'] = line.replace('source=', '').strip()
	app_data['use_iron'] = data['use_iron']
	f = open('resources/app_data', 'w')
	for key in app_data:
		line = key + '=' + app_data[key]
		f.write(line + '\n')
	f.close()
