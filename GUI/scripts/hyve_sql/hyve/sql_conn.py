import MySQLdb
import sys


class mysql_connection:
	def __init__(self, credentials, table):
		try:
			# self.connection = MySQLdb.connect(credentials['HOST_NAME'], credentials['USER_NAME'], credentials['PASSWORD'], credentials['DB_NAME'])
			self.TARGET_TABLE = table[table.find('-') + 1:len(table) - 1]
			print 'Connected to Mysql database'
		except:
			print 'Error connecting database'
			sys.exit(0)

	def execute_script(self, script):
		cursor = self.connection.cursor()
		try:
			cursor.execute(script)
			self.connection.commit()
			print 'Successfully executed script'
		except:
			print 'Sorry could not execute the script'
			sys.exit(0)

	def generate_sql(self, key_dict, target_bucket):
		sql_0 = 'UPDATE ' + str(self.TARGET_TABLE) + '\n'
		sql_p = sql_0 + 'SET image_urls = \n\tCASE slug\n'
		sql_m = sql_0 + 'SET menu_urls = \n\tCASE slug\n'
		for slug in key_dict:
			if 'photos' in key_dict[slug]:
				images = {}
				image_urls = ''
				for w in key_dict[slug]['photos']:
					for image in key_dict[slug]['photos'][w]:
						link = 'http://' + target_bucket + '.s3.amazonaws.com/'
						link += slug + '/photos/' + w + '/' + image
						images[int(image.split('.')[0])] = link
				for string in sorted(images.items()):
					a, b = string
					image_urls += b + ','
				image_urls = image_urls[:len(image_urls) - 1]
				sql_p += "\twhen '" + slug + "' then '" + image_urls + "'\n"
			if 'menus' in key_dict[slug]:
				menus = {}
				menu_urls = ''
				for w in key_dict[slug]['menus']:
					for menu in key_dict[slug]['menus'][w]:
						link = 'http://' + target_bucket + '.s3.amazonaws.com/'
						link += slug + '/menus/' + w + '/' + menu
						menus[int(menu.split('.')[0])] = link
				for string in sorted(menus.items()):
					a, b = string
					menu_urls += b + ','
				menu_urls = menu_urls[:len(menu_urls) - 1]
				sql_m += "\twhen '" + slug + "' then '" + menu_urls + "'\n"
		sql_m += 'END'
		sql_p += 'END;\n\n\n\n'
		return sql_p + sql_m

	def generate_sql_2(self, key_dict, target_bucket):
			sql_0 = 'UPDATE ' + str(self.TARGET_TABLE)
			sql_p = ''
			sql_m = ''
			for slug in key_dict:
				if 'photos' in key_dict[slug]:
					images = {}
					image_urls = ''
					for w in key_dict[slug]['photos']:
						for image in key_dict[slug]['photos'][w]:
							link = 'http://' + target_bucket + '.s3.amazonaws.com/'
							link += slug + '/photos/' + w + '/' + image
							images[int(image.split('.')[0])] = link
					for string in sorted(images.items()):
						a, b = string
						image_urls += b + ','
					image_urls = image_urls[:len(image_urls) - 1]
					sql_p += sql_0 + " SET image_urls = \'" + image_urls + "' WHERE slug = '" + slug + "';\n"
				if 'menus' in key_dict[slug]:
					menus = {}
					menu_urls = ''
					for w in key_dict[slug]['menus']:
						for menu in key_dict[slug]['menus'][w]:
							link = 'http://' + target_bucket + '.s3.amazonaws.com/'
							link += slug + '/menus/' + w + '/' + menu
							menus[int(menu.split('.')[0])] = link
					for string in sorted(menus.items()):
						a, b = string
						menu_urls += b + ','
					menu_urls = menu_urls[:len(menu_urls) - 1]
					sql_m += sql_0 + " SET menu_urls = \'" + menu_urls + "' WHERE slug = '" + slug + "';\n"
					# sql_m += "\twhen '" + slug + "' then '" + menu_urls + "'\n"
			return sql_p + '\n\n' + sql_m
