#!/usr/bin/python3

import cgi

print("content-type: text/html")
print()


import subprocess as sp
form =  cgi.FieldStorage()

osname = form.getvalue("n")
osimage = form.getvalue("i")


cmd = "sudo docker run -d -i -t --name {0} {1}".format(osname, osimage)

output = sp.getstatusoutput(cmd)

status = output[0]

out = output[1]

if status == 0:
    print("os launched named {}..".format(osname))
else:
    print("error : ".format(out))

