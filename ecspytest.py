import boto 	# we want boto.s3.connection and boto.s3.key

#accessKeyId = '<override your environment variable AWS_ACCESS_KEY_ID here>' 
#secretKey = '<override your environment variable AWS_SECRET_ACCESS_KEY here>' 
host = 'object.ecstestdrive.com' 

#establish connection to ECS end-point using the shortcut
conn = boto.connect_s3(host = host)

#conn = boto.connect_s3(
#       aws_access_key_id = accessKeyId,
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
bucket = conn.create_bucket("new_bucket_aug11")
# or connect to existing bucket:
# bucket = conn.get_bucket("new_bucket_aug11")

print conn.get_all_buckets()  #show the new bucket

#create a new key and object using arbitrary key and value
newkey = bucket.new_key("hello_world")  #change this each time
newkey.set_contents_from_string("Here are the contents of my new object. \n")

#show contents of the new bucket only listing the new object
for key in bucket.list():
	print "{name}\t{size}\t{modified}".format(
             name = key.name,
             size = key.size,
             modified = key.last_modified,
            )

#read in the contents of the object we just added                
print newkey.get_contents_as_string()

# set the new object's permissions to public readable and generate a public URL with no 
# expiration limit, without requiring authorization, over standard HTTP (no /S)
newkey.set_canned_acl('public-read')
newkey_url = newkey.generate_url(0, query_auth=False, force_http=True)

# The object will be available here:
#
# http://<your namespace ID>.public.ecstestdrive.com/<your bucket name>/hello_world or 
# http://<your bucket name>.<your namespace ID>.public.ecstestdrive.com/hello_world 
#
# $ curl http://<your bucket name>.<your namespace ID>.public.ecstestdrive.com/hello_world
print "Your URL will be 