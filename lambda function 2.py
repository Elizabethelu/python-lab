# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:54:40 2021

@author: 91994
"""

s=['red','blue','black','rose','white']
result=list(filter(lambda a:len(a)>5,5)) 
print("New list : ",result)
n=[200,50,1300,800]
result=list(map(lambda a: a+a*0.1 if a>1000 else a+a*0.05,n))
print("Result : ",result)