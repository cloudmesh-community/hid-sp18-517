**Amazon Simple Storage Service S3 - libcloud**
====================================================


Introduction
------------

This tutorial is to guide you through the steps for using libcloud for Amazon Web Services (AWS) S3. Apache libcloud is a python library that provides abstraction layer and hides the complexities of directly integrating with AWS API's, for that matter it allows you to do so for different cloud providers. In the sections below more detailed steps are shown to install and use libcloud for AWS S3.

Documentation
-------------
	Documentation can be found at [https://libcloud.readthedocs.org]

Supported Python versions
-------------------------

    Python 2.5, 2.6, 2.7,
    PyPy,
    Python 3 (since 0.7.1)

Access key
------------------------

	To be able to access AWS S3 from libcloud we need the access key to be specified in the call. 
	Access key can be setup on AWS console by navigating to My Security credentials->Encryption Keys->Access Keys.

Requirements
------------

Setting up an AWS account online

	- Login to AWS website at aws.amazon.com
	- Click on "Complete Sign Up" button and follow instructions to create a new AWS account.
	- Install apache-libcloud

Installation
------------

	pip install apache-libcloud

Examples
------------

Create a new bucket on AWS S3
------------
In S3 you first need to create a bucket which is nothing but a container where you store your data in the form of files. This is where you can also define access controls.

	- Click on S3 link on the AWS console under storage section, this will bring you to the create bucket window.
	- Click on "Create Bucket" button, this opens up a wizard.
	- Answer all mandatory questions on each page.
	- Important point here is to note the "Bucket Name" and the "Region" you are creating this bucket in, 
	  as this information will be used while calling the API.

List Containers
---------------

List Containers function list all the containers of buckets available for the user in that particular region.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver


	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')
 
	d = driver.list_containers();

	print d;


list container objects
----------------------

List container objects function shows the list of all objects in that container. Please note the output could be large depending on the files present in the bucket.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver
	
	# Note I have used S3_US_EAST2 as this is the "region" where my S3 bucket is located.

	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')
	
	container = driver.get_container(container_name='<bucket name>')
	
	d = driver.list_container_objects(container);
	
	print d;

Upload a file
-------------

Upload a file helps in uploading a local file to S3 bucket.

	from libcloud.storage.types import Provider
	from libcloud.storage.providers import get_driver

	FILE_PATH = '/<file path>/<filename>'

	# Note I have used S3_US_EAST2 as this is the "region" where my S3 bucket is located.

	cls = get_driver(Provider.S3_US_EAST2)
	driver = cls('api key', 'api secret key')

	container = driver.get_container(container_name='<bucket name>')

	extra = {'meta_data': {'owner': '<owner name>', 'created': '2018-03-24'}}

	with open(FILE_PATH, 'rb') as iterator:
    obj = driver.upload_object_via_stream(iterator=iterator,
                                          container=container,
                                          object_name='backup.tar.gz',
                                          extra=extra)


References
------------
https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html
http://libcloud.readthedocs.io/en/latest/_modules/libcloud/storage/drivers/s3.html
https://libcloud.readthedocs.io/en/latest/storage/examples.html
http://libcloud.apache.org/apidocs/0.6.1/libcloud.storage.base.StorageDriver.html

