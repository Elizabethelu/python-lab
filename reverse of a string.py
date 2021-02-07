# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:16:42 2021

@author: 91994
"""

def reverse(str):
    if len(str)==0:
        return str
    else:
        return reverse(str[1:])+str[0]
mystr=input("Enter the string :")
print("The reverse of string is : ",reverse(mystr))    