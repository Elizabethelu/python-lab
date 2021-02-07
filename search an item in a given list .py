# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:26:54 2021

@author: 91994
"""

list=[3,5,6,7,2,9]
i=0
target=1
while i<len(list):
    if list[1]==target:
        print(target,"found at ",i)
        break
    i+=1
else:
        print("Item not found :")
        print("Number of occurence of ",target, "is:" ,list.count(target))
        