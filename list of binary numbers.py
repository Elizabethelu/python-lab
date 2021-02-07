# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:43:29 2021

@author: 91994
"""

num=input("Enter comma seperated 4 digit binary numbers : ")
num=num.split(',')
i=0
final_list=[]
while i<len(num):
    if not int(num[i],2)%5:
        final_list.append(num[i])
    i+=1
print('List of binary numbers divisible by 5 : ',','.join(final_list))    