# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:45:38 2021

@author: 91994
"""

def sum(a,b,c):
    sum=a+b+c
    if(a==b==c):
        sum=sum*3
        return sum
n1=int(input("Enter first number : "))    
n2=int(input("Enter second number : "))
n3=int(input("Enter third number : "))
print("Sum : " ,sum(n1,n2,n3))
    