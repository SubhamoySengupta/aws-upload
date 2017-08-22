import boto
# from boto.s3.key import Key
import boto.s3.connection
import sys


class connect_to_S3:

	def __init__(self, credentials):
		try:
			print 'Connecting to AWS'
			self.connection = boto.s3.connect_to_region(
				credentials['region'],
				aws_access_key_id=credentials['aws_access_key_id'],
				aws_secret_access_key=credentials['aws_secret_access_key'],
				is_secure=True,
				calling_format=boto.s3.connection.OrdinaryCallingFormat()
			)
		except:
			print 'Error couldnot connect to S3'
			sys.exit(0)

	def connect_to_aws_bucket(self, bucket_name):
		try:
			self.bucket = self.connection.get_bucket(bucket_name)
			print 'Connected to bucket', bucket_name
		except:
			print 'Couldnot connect to bucket', bucket_name
			sys.exit(0)

	def get_all_keys(self):
		try:
			temp = self.bucket.list()
			temp2 = []
			for key in temp:
				if '__w-' not in key.name:
					continue
				else:
					temp2.append(key.name)
			print 'Acquired all keys'
			return temp2
		except:
			print 'Could not get a list of keys'
			sys.exit(0)
