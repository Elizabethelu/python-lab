# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:13:31 2021

@author: 91994
"""

def myfun(n1,n2):
    if n1==n2:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")
    if n1+n2==5:
        print("They adds up to 5")
    else:
        print("They not adds upto 5")
    if n1-n2==5:
        print("Their difference is 5")
    else:
        print("Their difference is not 5")
num1=int(input("Enter first num:"))
num2=int(input("Enter second num:"))
myfun(num1,num2)            