# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:08:11 2021

@author: 91994
"""

rows=5
for i in range(0,rows):
    for j in range(0,i+1):
        print('*' ,end=' ')
    print()
for i in range(rows,0,-1):
    for j in range(0,1,-1):
        print(" * " ,end= ' ')
    print()    
    