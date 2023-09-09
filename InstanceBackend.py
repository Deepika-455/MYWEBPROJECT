#!/usr/bin/python3

print("content-type: text/html")
print()

import boto3

session=boto3.Session(aws_access_key_id=’’', aws_secret_access_key='', region_name='ap-south-1')
launch = session.client('ec2',region_name='ap-south-1')
launch.run_instances(ImageId="ami-0ded8326293d3201b",
                        InstanceType="t2.micro",
                        MaxCount=1,
                        MinCount=1)

print("done")
