# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:48:06 2021

@author: 91994
"""

num=int(input("Enter the number : "))
print("Factors of : ",num)
for i in range (1,num+1):
    if not num%i:
        print(i,end=" ")
