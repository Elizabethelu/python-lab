# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:36:52 2021

@author: 91994
"""

def fibo(n):
    if not n:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
n=int(input("Enter the number : "))
print(n,"th term in fibonacci series is : ",fibo(n))
    
        