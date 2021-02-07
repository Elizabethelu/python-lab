# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:45:45 2021

@author: 91994
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number : "))
print("The factorial of " ,n, " : ",fact(n))
    