# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:45:45 2021

@author: 91994
"""

import math
a=int(input("Enter the starting range : "))
b=int(input("Enter the end: "))
for i in range(a,b+1):
    k=i;
    while k>0:
        q=0
        j=k%10
        if j%2==0:
            k=k//10
        else:
            q=1
            break
        if q==0:
            u=math.sqrt(i)
    if((u-math.floor(u)))==0:
            print(i)
