import hyve
from subprocess import Popen, PIPE


def start_k(cred):
	input_params = cred

	aws_conn = hyve.aws_connection.connect_S3(input_params)

	aws_conn.connect_to_aws_bucket(input_params['in_bucket'])

	rootwork_list = aws_conn.bucket.list()
	temp_rootwork_list = []

	aws_conn.connect_to_aws_bucket(input_params['out_bucket'])

	stores_list = aws_conn.bucket.list()
	temp_stores_list = []

	for r in rootwork_list:
		temp_rootwork_list.append(r.name)

	for s in stores_list:
		if '__w-' in s.name:
			key_s = s.name.split('/')
			slug = key_s[0]
			type_o = key_s[1]
			w = key_s[2]
			i = key_s[3]
			temp_stores_list.append('stores/' + slug + '/' + type_o + '/' + i)

	new = []
	for r in temp_rootwork_list:
		if 'stores/' in r:
			if r not in temp_stores_list:
				new.append('//hyve-rootwork/' + r)

	f = open('resources/new.txt', 'w')
	o = open('out/new_list.txt', 'w')
	for n in new:
		if n[(len(n) - 4):] == '.jpg':
			print n
			f.write(n + '\n')
			o.write(n + '\n')
	f.close()
	o.close()

	cmd = 'chmod +x resources/queue'
	process1 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
	print process1.communicate()
	cmd = 'resources/queue resources/new.txt'
	process2 = Popen([cmd], shell=True, stdin=PIPE, stderr=PIPE)
	print process2.communicate()
