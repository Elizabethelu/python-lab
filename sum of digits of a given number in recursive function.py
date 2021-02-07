# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:50:09 2021

@author: 91994
"""

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return n%10+sum_of_digits(int(n/10))
n=int(input("Enter the number : "))
print("sum of digits : ",sum_of_digits(n))
    