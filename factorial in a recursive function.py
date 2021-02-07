# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:38:28 2021

@author: 91994
"""

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number : "))
print("The factorial of ",n, " : ",fact(n))

    
            