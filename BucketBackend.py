!/usr/bin/python3

print("content-type: text/html")
print()

import boto3
import cgi

data = cgi.FieldStorage()
name=data.getvalue("b")

session=boto3.Session(aws_access_key_id='', aws_secret_access_key='', region_name='ap-south-1')

bucket = session.client('s3')
bucket.create_bucket(
Bucket=name,
ACL='private',
CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

print("done")
