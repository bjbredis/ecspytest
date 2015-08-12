# ECSpyTest

#### Python code to Test/Demo EMC Elastic Cloud Storage (ECS)

Requirements: 
* [Python 2.7+](https://www.python.org)
* [Boto](https://github.com/boto/boto)

## Installation
* git clone https://github.com/bradjbarnes/ecspytest.git
* cd ecspytest
* virtualenv -p /usr/bin/python2.7 venv
* source venv/bin/activate
* pip install < requirements.txt

## Get Your ECS Test Drive Credentials

Go to [ECS TestDrive](https://portal.ecstestdrive.com) to get ECS credentials.

## Usage

* Add your ECS credentials to env variabls AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
```
$ AWS_ACCESS_KEY_ID=<your access key ID>; AWS_SECRET_ACCESS_KEY=<your secret key>;
$ echo $AWS_ACCESS_KEY_ID; echo $AWS_SECRET_ACCESS_KEY;
``` 
* customize some of the bucket names, object keys and contents  
* run: 
``` 
$ python ecspytest.py
```
