# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:17:38 2021

@author: 91994
"""

str1='lets rock'
str2=' '
i=0
while i<len(str1):
    if not(i%2):
       str2=(str2+str1[i])
    i=i+1
print("String : ",str1)
print("After removing odd indexed characters :",str2)
    