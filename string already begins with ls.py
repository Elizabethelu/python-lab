# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:57:05 2021

@author: 91994
"""

def string_fun(s):
    if s[:2]=='ls':
        return s
    else:
        s='ls '+ s
        return s 
s1=input("Enter a string : ")
print("Orginal string : ",s1)
print("New string is : ", string_fun(s1))
