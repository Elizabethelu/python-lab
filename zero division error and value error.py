# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:56:44 2021

@author: 91994
"""
try:
    a=int(input("Enter the numerator : "))
    b=int(input("Enter the denominator : "))
    print("Result after division : " %(a/b))
except (ZeroDivisionError,ValueError) as er :
       print(er)
else:
     print("Successfully executed ")
finally:
        print("Executed ")       
    
