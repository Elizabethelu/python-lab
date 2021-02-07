# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:59:51 2021

@author: 91994
"""

celsius1=float(input("Enter the temperature in celsius : "))
fahrenheit1=(celsius1*9/5)+32
print("The temperature %.2f Celsius in fahrenheit is : %.2f Fahrenheit " %(celsius1,fahrenheit1))
fahrenheit2=float(input("Enter the temperature in fahrenheit : "))
celsius2=(fahrenheit2-32)*5/9
print("The temperature %.2f Fahrenheit in celsius is : %.2f Celsius " %(fahrenheit2,celsius2))

