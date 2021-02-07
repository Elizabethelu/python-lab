# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:13:14 2021

@author: 91994
"""
n=input("Enter a list of numbers:")
ls=n.split(",")
ls=[int(i) for i in ls]
print("list:",ls)
ls.sort()
print("Ascending order:",ls)
ls.sort(reverse=True)
print("Descending order:",ls)

