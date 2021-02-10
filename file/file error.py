# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:57:42 2021

@author: 91994
"""

inf=False
out=False
try:
 inf=open('infile.txt')
 out=open('outfile.txt','w')
 line=inf.read()
 while line:
   out.write(line)
   inf=False
   inf=open('outfile.txt')
   line=inf.readline()
 print(line)
except IOError as io:
   print(io)
finally:
  if inf:inf.close()
  if out:out.close()       