# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:05:04 2021

@author: 91994
"""
c=input("Enter colors seperated with comma : ")
list=c.split(',')
print("List of colors : ", list)
new=[list[i] for i in range(len(list)) if i%2==0]
print("Atternative colors : ",new)
 





