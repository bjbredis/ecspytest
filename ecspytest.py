import boto 	# we want boto.s3.connection and boto.s3.key

#accessKeyId = '<override your environment variable AWS_ACCESS_KEY_ID here>' 
#secretKey = '<override your environment variable AWS_SECRET_ACCESS_KEY here>' 
host = 'object.ecstestdrive.com' 

#establish connection to ECS end-point using the shortcut
conn = boto.connect_s3(host = host)

#conn = boto.connect_s3(
#        aws_access_key_id = accessKeyId,
#        aws_secret_access_key = secretKey,
#        host = host,
#        #is_secure=False,               # uncomment if you are not using ssl
#        calling_format = boto.s3.connection.OrdinaryCallingFormat()
#        )	
				

print conn.get_all_buckets()  #list all buckets

#dump all objects names from all buckets (hopefully you don't have too many in there)
for bucket in conn.get_all_buckets():
	print "{name}:".format(name=bucket.name)
	for key in bucket.list():
		print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )
                
#create a new bucket with a new bucket name
newbucket = conn.create_bucket("new_bucket_aug11")

print conn.get_all_buckets()  #show the new bucket

#create a new key and object using arbitrary key and value
newkey = newbucket.new_key("hello_world")
newkey.set_contents_from_string("Here are the contents of my new object. \n")

#show contents of the new bucket only listing the new object
for key in newbucket.list():
	print "{name}\t{size}\t{modified}".format(
             name = key.name,
             size = key.size,
             modified = key.last_modified,
            )

#read in the contents of the object we just added                
newkey.get_contents_as_string()
