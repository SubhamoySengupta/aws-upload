import hyve
from subprocess import Popen, PIPE


input_params = hyve.input_params.get_credentials()
if input_params is None or input_params is False:
	print 'No credentials provided!'
	exit(0)

aws_conn = hyve.aws_connection.connect_S3(input_params)

aws_conn.connect_to_aws_bucket(input_params['bucket'])

rootwork_list = aws_conn.bucket.list()
temp_rootwork_list = []

aws_conn.connect_to_aws_bucket(input_params['store-bucket'])

stores_list = aws_conn.bucket.list()
temp_stores_list = []

aws_conn.connect_to_aws_bucket(input_params['chain-bucket'])

chains_list = aws_conn.bucket.list()
temp_chains_list = []

'''
rootwork --> chains/b-enzo/menus/1.jpg
stores ----> 1-glam-n-glow/photos/__w-200-400-600-800-1000-1200-1400__/1.jpg
chains ----> b-enzo/menus/__w-200-800-1000__/1.jpg
'''
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

for c in chains_list:
	if '__w-' in c.name:
		key_c = c.name.split('/')
		slug = key_c[0]
		type_o = key_c[1]
		w = key_c[2]
		i = key_c[3]
		temp_chains_list.append('chains/' + slug + '/' + type_o + '/' + i)

new = []
for r in temp_rootwork_list:
	if 'chains/' in r:
		if r not in temp_chains_list:
			new.append('//hyve-rootwork/' + r)
	elif 'stores/' in r:
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
