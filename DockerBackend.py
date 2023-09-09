#!/usr/bin/python3

print("conent-type: text/html")
print()

import subprocess
import cgi

data=cgi.FieldStorage()
my=data.getvalue("n")

output = subprocess.getoutput("sudo {}".format(my))
print("<pre>")
print(output)
print("</pre>")
