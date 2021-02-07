# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:02:19 2021

@author: 91994
"""

def check(n):
    if abs(1000 - n)<=100:
        print(n,"is within 100 of 1000 : ")
    elif abs(2000 - n)<=100:
        print(n,"is within 100 of 1000 : ")
a=int(input("Enter a number : "))
check(a)        