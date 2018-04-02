**Amazon Elastic Cloud Compute EC2 - BOTO 3**
====================================================


Introduction
------------

This tutorial is to guide you through the steps for using BOTO version 3 for Amazon Web Services (AWS) EC2. BOTO is a python library that provides abstraction layer and hides the complexities of directly integrating with AWS API's to interact with EC2 compute machines. In the sections below more detailed steps are shown to install and use BOTO for AWS EC2.

Documentation
-------------
	Documentation can be found at [https://boto3.readthedocs.io/en/latest/]


Access key
------------------------

	Initial setup is required to be able to access AWS EC2 from BOTO wherein you provide the key and region details. 
	You can find the key details from IAM console on AWS.

BOTO configuration
------------------

BOTO can be configured in two ways, either by using the aws configure command if you have AWS Command line interface installed or simply by manually creating and editing the ~/.aws/credentials file to include below parameters.

	[default]
	aws_access_key_id = <YOUR_ACCESS_KEY>
	aws_secret_access_key = <YOUR_SECRET_KEY>

Similar to libcloud, BOTO also requires the region where you would create your EC2 instance, the same can be maintained by creating a config file.

	vi .aws/config
	[default]
	region=<region name> # for example us-east

Requirements
------------

Setting up an AWS account online

	- Login to AWS website at aws.amazon.com
	- Click on "Complete Sign Up" button and follow instructions to create a new AWS account.
	- Install BOTO3

Installation
------------

	pip install boto3

Examples
------------

List EC2 instances
---------------

Below code snippet describes all the EC2 instances under the account.

	import boto3
	
	ec2 = boto3.client('ec2')
	response = ec2.describe_instances()
	print(response)


Start or Stop instances
-----------------------

List container objects function shows the list of all objects in that container. Please note the output could be large depending on the files present in the bucket.

The script below takes in two parameters, on/off to start or stop the EC2 instance and the second is the instance id. If the code is run through a file named boto_ec2.py then here is how you would run the code from command line.

	# To start the instance
	$ python boto_ec2.py <on> <instance id>

	# To stop the instance
	$ python boto_ec2.py <off> <instance id>

	# Add below code to a file for example boto_ec2.py

    # Code from the online documentation
	# http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html

	import sys
	import boto3
	from botocore.exceptions import ClientError
	
	instance_id = sys.argv[2]
	action = sys.argv[1].upper()
	
	ec2 = boto3.client('ec2')

 
	if action == 'ON':
	    # Do a dryrun first to verify permissions
	    try:
	        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
	    except ClientError as e:
	        if 'DryRunOperation' not in str(e):
	            raise
	
	    # Dry run succeeded, run start_instances without dryrun
	    try:
	        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
	        print(response)
	    except ClientError as e:
	        print(e)
	else:
	    # Do a dryrun first to verify permissions
	    try:
	        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
	    except ClientError as e:
	        if 'DryRunOperation' not in str(e):
	            raise
	
	    # Dry run succeeded, call stop_instances without dryrun
	    try:
	        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
	        print(response)
	    except ClientError as e:
	        print(e)


Reboot instances
----------------

	# Code from the online documentation
	# http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html

	import boto3
	from botocore.exceptions import ClientError
	
	
	ec2 = boto3.client('ec2')
	
	try:
	    ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=True)
	except ClientError as e:
	    if 'DryRunOperation' not in str(e):
	        print("You don't have permission to reboot instances.")
	        raise
	
	try:
	    response = ec2.reboot_instances(InstanceIds=['INSTANCE_ID'], DryRun=False)
	    print('Success', response)
	except ClientError as e:
	    print('Error', e)


References
-----------

	https://github.com/boto/boto3
	https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation
	http://boto3.readthedocs.io/en/latest/guide/ec2-example-managing-instances.html



