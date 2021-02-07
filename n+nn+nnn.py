# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:31:14 2021

@author: 91994
"""

a = int(input ("enter a number : "))
num1 = int("%s" % a)
num2 = int("%s%s" % (a,a))
num3 =int("%s%s%s" % (a,a,a))
print (num1, " + " ,num2, " + " ,num3 , " = " , num1 + num2 + num3)
