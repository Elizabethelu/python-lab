# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:02:24 2021

@author: 91994
"""

words = input("Enter comma seperated list of words : ")
words = words.split(',')
unq_words=[]
i=0
while i<len(words):
        if words[i].strip() not in unq_words :
            unq_words.append(words[i].strip())
            i+=1
unq_words.sort()
print("Result is : ",unq_words)
      
    