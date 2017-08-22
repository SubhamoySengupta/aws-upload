import boto
import boto.s3.connection


class connect_S3:

	def __init__(self, credentials):
		try:
			self.connection = boto.s3.connect_to_region(
					credentials['region'],
					aws_access_key_id=credentials['aws_access_key_id'],
					aws_secret_access_key=credentials['aws_secret_access_key'],
					is_secure=True,
					calling_format=boto.s3.connection.OrdinaryCallingFormat()
				)
			print 'Connection to AWS S3 is successful'
		except:
			print 'Could not connect to AWS'

	def connect_to_aws_bucket(self, bucket_name):
		try:
			self.bucket = self.connection.get_bucket(bucket_name)
			print 'Connected to bucket', bucket_name
		except:
			print 'Couldnot connect to bucket', bucket_name

	def list_input_bucket(self):
		try:
			temp = self.bucket.list()
			output_bucket = ''
			slug = ''
			type_o = ''
			# obj = dict(output_bucket= dict(slug = dict(type= [])))
			obj = dict()

			for key in temp:
				k = key.name.split('/')
				if k[0] != output_bucket:
					output_bucket = k[0]
					obj[output_bucket] = dict()
				if k[1] != slug:
					slug = k[1]
					obj[output_bucket][slug] = dict()
					type_o = ''
				if k[2] != type_o:
					type_o = k[2]
					obj[output_bucket][slug][type_o] = []

				obj[output_bucket][slug][type_o].append(k[3])
			return obj

		except:
			print 'Couldnot list the bucket keys'

	def list_output_bucket(self):
		try:
			temp = self.bucket.list()
			slug = ''
			type_o = ''
			obj = dict()

			for key in temp:
				if '__w-' not in key.name:
					continue
				else:
					k = key.name.split('/')
					if k[0] != slug:
						slug = k[0]
						obj[slug] = dict()
						type_o = ''
					if k[1] != type_o:
						type_o = k[1]
						obj[slug][type_o] = []
					obj[slug][type_o].append(k[3])
			return obj
		except:
			print 'Couldnot list the bucket keys'
