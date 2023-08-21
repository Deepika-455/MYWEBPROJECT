#! /usr/bin/python3
print("Content-type: text/html")
print()
import cgi
import smtplib, ssl

mydata=cgi.FieldStorage()
message=mydata.getvalue("m")
gmailid=mydata.getvalue("g1")
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = " # Enter your address”
receiver_email =gmailid
password = ""
messagemail=message
print("<pre>")
print("Thanks for  using")
print("A confirmation mail has been sent to: "+gmailid)
print("</pre>")
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, messagemail)
 
