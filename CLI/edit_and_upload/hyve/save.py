import json


def saveFile(filename, data):
	f = open(filename, 'w')
	f.write(json.dumps(data))
	f.close()


class openErrorFile:
	def __init__(self, filename):
		self.log = open(filename, 'w')

	def report(self, dat):
		self.log.write(str(dat)+'\n')

	def note(self, dat):
		self.log.write('========================================================\n')
		self.log.write('\t'+str(dat)+'\n')
		self.log.write('========================================================\n\n')
