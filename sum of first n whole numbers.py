# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:07:35 2021

@author: 91994
"""

def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
n=int(input("Please enter the number : "))
print("sum of first" ,n, "whole numbers : ",sum(n))
    