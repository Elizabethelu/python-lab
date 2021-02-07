# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 23:37:45 2021

@author: 91994
"""

words = { }
line = " I love my kerala and it is a gods own " 
for k in line.split():
 words[k]=words.get (k,0) +1
print(words)



    