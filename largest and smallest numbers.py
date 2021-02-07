# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:21:19 2021

@author: 91994
"""

n=input("Enter a list of numbers:")
ls=n.split(",")
ls=[int(i) for i in ls]
print("list:",ls)
print("Largest number:",max(ls))
print("Smallest number:",min(ls))
