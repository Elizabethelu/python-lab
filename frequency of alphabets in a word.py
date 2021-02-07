# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:44:16 2021

@author: 91994
"""

character={}
word='programming'
for c in word.lower():
    character[c]=character.get(c,0)+1
print(character)    