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
                
#create a new bucket with a new bucket name or connect to existing bucket:
bucket_name = "new_bucket_aug11"
try:
	bucket = conn.create_bucket(bucket_name)
except Exception as e:
	print "Bucket: \'"+bucket_name+"\' already exists! Opening the existing bucket"
else:		
	bucket = conn.get_bucket(bucket_name)

print "Here is the list of buckets:"
print conn.get_all_buckets()  #show the new bucket

#create a new key and object using arbitrary key and value
newkey = bucket.new_key("hello_world")  #change this each time
newkey.set_contents_from_string("Here are the contents of my new object. \n")

#show contents of the bucket
print "Here is the content of the bucket <"+bucket_name+">:"
for key in bucket.list():
	print "{name}\t{size}\t{modified}".format(
             name = key.name,
             size = key.size,
             modified = key.last_modified,
            )

#read in the contents of the object we just added                
print "The content of the object with key <\'"+newkey.name+"\'> are:"	
print newkey.get_contents_as_string()

# set the new object's permissions to public readable and generate a public URL with no 
# expiration limit, without requiring authorization, over standard HTTP (no /S)
print "Creating a public read-only HTTP URL for the object we just created"
newkey.set_canned_acl('public-read')
newkey_url = newkey.generate_url(0, query_auth=False, force_http=True)

#get the access_key to formulate the URL since it's slightly different on ECS
## Here are ECS' string formulation rules
##
## http://<your namespace ID>.public.ecstestdrive.com/<your bucket name>/hello_world or 
## http://<your bucket name>.<your namespace ID>.public.ecstestdrive.com/hello_world 
access_key = boto.config.get_value('Credentials', 'aws_access_key_id')
arr = access_key.split("@")  # namespace stored in arr[0]
namespace = arr[0]
ecs_key_url = "http://"+bucket_name+"."+namespace+".public.ecstestdrive.com/"+newkey.name

print "Try this in your web browser: "+ecs_key_url
print "Try this in the command line:\n $ curl -v \""+ecs_key_url+"\""


