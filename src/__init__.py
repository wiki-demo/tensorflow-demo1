#!/usr/bin/python
# -*- coding: UTF-8 -*-


import os

try:
    fo = open("test132.txt","r")
except Exception,err:
    print "error"+ err
else:
    fo.write("33333222")