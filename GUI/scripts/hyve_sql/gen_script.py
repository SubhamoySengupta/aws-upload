import hyve


def start_gen(cred):
	target_bucket = cred['out_bucket']

	credentials = cred

	aws_conn = hyve.aws_conn.connect_to_S3(credentials)

	aws_conn.connect_to_aws_bucket(target_bucket)

	bucket_keys = aws_conn.get_all_keys()

	print 'total number of keys', len(bucket_keys)

	key_groups = hyve.params.refine_keys(bucket_keys)

	hyve.params.save_keys(key_groups)

	mysql_conn = hyve.sql_conn.mysql_connection(credentials, target_bucket)

	sql_script = mysql_conn.generate_sql_2(key_groups, target_bucket)

	hyve.params.save_script(sql_script, target_bucket)

	print "Do you want to execute script? (Y/y==> 'Yeah!')"

	ip = raw_input('>')

	if ip == 'Y' or ip == 'y':
		mysql_conn.execute_script(sql_script)

	print '~~GAME OVER~~'
