import upload_from_local
from subprocess import Popen, PIPE
import edit_and_upload
import hyve_sql
import time
from PyQt5 import QtWidgets


def sync_s3_method_1(data, progressBar, console, success_count, error_count):
	upload_from_local.scan_dir.start_scan(data, progressBar, console, success_count, error_count)


def upload_method_cycle():
	f = open('out/succsess.txt', 'r')
	for line in f.readlines():
		path = '//hyve-rootwork/' + line
		cmd = 'chmod +x resources/queue_1'
		process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process1.communicate()
		cmd = 'resources/queue_1 ' + path
		process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		print process2.communicate()


def upload_method_0(data, progressBar, console, success_count, error_count):
		for i in range(100):
			console.append('Hello World' + str(i) + '\n')
			success_count.display(i)
			progressBar.setProperty('value', (i + 1))
			QtWidgets.QApplication.processEvents()
			time.sleep(0.5)

	# edit_and_upload.get_new_keys.start_k(data)


def update_db_method_3(data, progressBar, console, success_count, error_count):
	for i in range(100):
		time.sleep(0.2)
	# hyve_sql.gen_script.start_gen(data)
