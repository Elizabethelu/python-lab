# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:07:48 2021

@author: 91994
"""

def printword(w,n):
    for i in range(n):
        print(w,end=' ')
word=input("Enter a word : ")
num=int(input("Enter a number : "))
printword(word,num)        