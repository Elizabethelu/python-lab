# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:26:38 2021

@author: 91994
"""

def binary(n):
    if n>1:
        binary(n//2)
    print(n%2,end=' ')
dec=int(input("Enter the decimal number : "))
print("Binary equivalent : ")
binary(dec)
