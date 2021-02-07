# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:47:00 2021

@author: 91994
"""

list=[4,8,56,73,90,31,56,78,46,237,39,6]
i=0
while i<len(list):
    if list [i]==237:
        print(list [i])
        break
    else :
        if not list [i] %2:
            print(list [i])
        i=i+1    