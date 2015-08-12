# ECSpyTest

#### Python code to Test/Demo EMC Elastic Cloud Storage (ECS)

Requirements: 
* [Python 2.7+](https://www.python.org)
* [Boto](https://github.com/boto/boto)

## Installation
* git clone https://github.com/bradjbarnes/ecspytest.git
* cd ecspytest
* pip install < requirements.txt

## Get Your ECS Test Drive Credentials

Go to [ECS TestDrive](https://portal.ecstestdrive.com) to get ECS credentials.

## Usage

* Store your credentials in your [~/.boto](http://boto.readthedocs.org/en/latest/boto_config_tut.html#details)
* customize some of the bucket names, object keys and contents  
* run: 
``` 
$ python ecspytest.py
```
