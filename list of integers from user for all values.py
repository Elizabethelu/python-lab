# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:13:58 2021

@author: 91994
"""

n=input("Enter integer numbers : ")
a=list(map(int,n.split()))
for i in a:
  if i>100:
        print(" Over ")
  else:
       print(i)
        