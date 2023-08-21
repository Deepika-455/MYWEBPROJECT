#!/usr/bin/python3

import cgi
from twilio.rest import Client

print("content-type: text/html")
print()

#data = cgi.FieldStorage()
#num = data.getvalue('c')
#print(num)

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='',
    to='',
    body="hlw"
)
print("succesfully sent msg")
