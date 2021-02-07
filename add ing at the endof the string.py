# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:51:46 2021

@author: 91994
"""

S=input("Enter a string : " )
print("String : " , S)
length=len(S)
if S[-3 : ] == 'ing':
    S+=' ly '
else :
    S+='ing'
print("result : " , S)

    
       
