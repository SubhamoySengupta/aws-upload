from subprocess import Popen, PIPE
from PyQt5 import QtWidgets


def get_list(source, dest):
	cmd = 'aws s3 sync --dryrun '
	exclude = '--exclude "." --exclude ".ini" --exclude "*.ini" --exclude ".picasaoriginals" '
	include = '--include "/menus/.jpg" --include "/photos/.jpg" '
	extra_cards = '--size-only '
	source = source + ' '
	dest = dest + ' '
	stdout = '> out/temp.txt'
	cmd = cmd + exclude + include + extra_cards + source + dest + stdout
	process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
	return process.communicate()


def save_list(data, file_name):
	f = open(file_name, 'w')
	for line in data:
		f.write(line)
	f.close()


def upload_to_aws(success, source, dest, progressBar, console, success_count, error_count):
	aws_cmd = 'aws s3 cp '
	p = len(success)
	for key in success:
		# last character is eol
		cmd = aws_cmd + source + key[:len(key) - 1] + ' ' + dest + key[:len(key) - 1]
		console.append('command-->', cmd)
		QtWidgets.QApplication.processEvents()
		process = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
		console.append(process.communicate())
		console.append('\n')
		progressBar.setProperty('value',  (((p + 1) / len(success)) * 100))
		QtWidgets.QApplication.processEvents()
		p = p + 1
