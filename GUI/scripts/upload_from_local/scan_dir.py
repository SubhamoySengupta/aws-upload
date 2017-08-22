import aws_hyve
from sys import exit
from PyQt5 import QtWidgets


def start_scan(cred, progressBar, console, success_count, error_count):
	console.append('Analyzing files! This will take time\n')
	QtWidgets.QApplication.processEvents()
	source, dest = cred['source'], cred['destination']

	aws_hyve.files.get_list(source, dest)
	aws_hyve.trimmer.trim_file_list('out/temp.txt', dest)
	success, error = aws_hyve.trimmer.check('out/trimmed.txt')
	aws_hyve.files.save_list(success, 'out/success.txt')
	if not len(error) == 0:
		console.append('There were a few errors. Please check errors.txt and success.txt\n')
		QtWidgets.QApplication.processEvents()
		aws_hyve.files.save_list(error, 'out/errors.txt')
		# exit(0)

	if not len(success) == 0:
		# aws_hyve.common.confirm('Upload to aws S3 bucket?')
		aws_hyve.files.upload_to_aws(success, source, dest, progressBar, console, success_count, error_count)
		console.append('All clear! syncing files with s3 buckets\n')
		console.append('===========================================\n')
		QtWidgets.QApplication.processEvents()

	console.append('All files are properly synced\n')
	QtWidgets.QApplication.processEvents()
