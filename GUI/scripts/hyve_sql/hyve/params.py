import sys


def get_credentials():
	c = open('resources/credentials_sql.txt')
	response = {}
	try:
		for line in c.readlines():
			strings = line.split('=')
			if len(strings) == 2:
				response[strings[0].strip()] = strings[1].strip()
		if len(response) == 0:
			print 'No info found in resources/credentials_sql.txt'
			sys.exit(0)
		else:
			return response
	except:
		print 'No info found in resources/credentials_sql.txt'
		sys.exit(0)


def refine_keys(key_dict):
	# divide key into parts
	new_dict = {}
	for key in key_dict:
		slug, type_pm, w, image = key.split('/')
		if slug not in new_dict:
			new_dict[slug] = {}
		if type_pm not in new_dict[slug]:
			new_dict[slug][type_pm] = {}
		if w not in new_dict[slug][type_pm]:
			new_dict[slug][type_pm][w] = []
		new_dict[slug][type_pm][w].append(image)
	return new_dict


def save_script(dat, target_bucket):
	f_name = 'out/update_data_' + target_bucket + '.sql'
	f = open(f_name, 'w')
	f.write(dat)
	print 'Saved sql script to ' + f_name
	f.close()


def save_keys(key_groups):
	f = open('out/new_list.txt', 'w')
	for slug in key_groups:
		f.write('============================================\n')
		f.write(slug + '\n')
		for type_pm in key_groups[slug]:
			f.write('\tType = ' + type_pm + '\n')
			for w in key_groups[slug][type_pm]:
				for image in key_groups[slug][type_pm][w]:
					f.write('\t\t' + image + '\n')
	f.close()
