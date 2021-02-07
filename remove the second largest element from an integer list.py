# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:27:58 2021

@author: 91994
"""

n=[100,50,60,70,80,90]
ls=[int(i) for i in n]
print("List:",n)
ls.sort()
a=ls[-2]
ls.remove(a)
print("List after removing second largest number:",ls)
