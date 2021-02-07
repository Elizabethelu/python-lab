# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:25:48 2021

@author: 91994
"""

met=float(input("Enter the length in meter : "))
centi=float(input("Enter the length in centimeter : "))
feet1=3.28*met
inches1=39.37*met
feet2=0.0328*centi
inches2=0.3937*centi
print(" %.2f meter is equivalent to %.2f feets." %(met,feet1))
print(" %.2f meter is equivalent to %.2f inches." %(met,inches1))
print(" %.2f centimeter is equivalent to %.2f feets." %(centi,feet2)) 
print(" %.2f centimeter is equivalent to %.2f inches." %(centi,inches2))

     

