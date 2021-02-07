# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:55:14 2021

@author: 91994
"""

ls=[1,5,3,6,3,5,6,1]
print("The orginallist is : " + str(ls))
res = [i for n,i in enumerate(ls) if i not in ls[:n]]
print("The list after removing duplicates : " + str(res))
