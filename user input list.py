# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:10:05 2021

@author: 91994
"""
import random
a=input("Enter list seperated with commas:")
ls=a.split(' ')
print("Entered list:",ls)
random.shuffle(ls)
print("List after shuffling:",ls)

