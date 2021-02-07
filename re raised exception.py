# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:33:27 2021

@author: 91994
"""

try:
    x=int(input("Enter an integer :"))
    try:
        y=0
        assert y!=0,"Invalid Operation"
        print(x/y)
    except AssertionError as msg:
        print(msg)
        raise
    else:
         print("Result",x/y)
except AssertionError as ae:
    print("Re raised exception : ",ae)         
        
        