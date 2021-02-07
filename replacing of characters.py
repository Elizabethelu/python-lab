# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 19:18:29 2021

@author: 91994
"""

base_str = " malayala manorama "
char1 = base_str[0]
base_str = base_str.replace(char1 ,'&')
base_str = char1 + base_str[1:]
print (base_str)

