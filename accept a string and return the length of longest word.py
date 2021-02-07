# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:03:15 2021

@author: 91994
"""

S=input("Enter a string : ")
a=S.split()
print("The string : ", S)
max = 0
word = 0
for i in a:
    if max == len(i):
        word=1
    if max<len(i):
        word=0
        max=len(i)
    if word==1:
        print("TATTO")
    else:
        print("Length of longest word : ", max)
        
        
    
    
        