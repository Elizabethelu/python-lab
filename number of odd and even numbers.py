# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:29:52 2021

@author: 91994
"""

num=[5,7,1,4,9,0,3]
i=0
odd=0
even=0
while i<len(num):
    if not num[i]%2:
        even+=1
    else:
        odd+=1
    i+=1
print("List : ",num)
print("Number of odd numbers : ",odd)
print("Number of even numbers : ",even)    