# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 17:46:40 2021

@author: 91994
"""

a=int(input("Enter the step number : "))
for i in range(1,a+1): 
   for j in range(1,i+1):
      print(i*j,end=" ")
   print()        