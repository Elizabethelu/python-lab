# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:50:35 2021

@author: 91994
"""

s=['abcd','knock','jungle','mom','dad']
i=0
c=0
while i<len(s):
    if len(s[i])>=2 and s[i][0]==s[i][-1]:
        c+=1
    i+=1
print("List : ",s)
print("The number of strings starts and ends with same character : ",s)
    