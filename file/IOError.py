# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:19:43 2021

@author: 91994
"""
try:
    a=open("Appendpgm.txt","a")
    x=input("Enter a text:")
    while x:
        a.write(x+"\n")
        x=input("Enter a text:")
    a.close ()
except IOError as io:
    print(io)
      
