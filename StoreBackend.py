#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi
import boto3

session=boto3.Session(aws_access_key_id='', aws_secret_access_key='', region_name='ap-south-1')

BUCKET_NAME = ''
s3 = session.client('s3')



form = cgi.FieldStorage()

if 'image' in form:
    image = form['image']

    s3.upload_fileobj(image.file, BUCKET_NAME, image.filename)
    print("<h2>Image uploaded successfully!</h2>")
else:
    print("<h2>No image selected for upload.</h2>")
