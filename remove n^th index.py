# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:50:33 2021

@author: 91994
"""
def remove(string, n):
    first = string [ : n ]
    last = string [ n+1 : ]
    return first + last
string = input (" Enter the string : ")
n=int(input(" Enter the index of the character to remove : "))
print("string :",str)
print("Modified string:")
print(remove(str, n))  









