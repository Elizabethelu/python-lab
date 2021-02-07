# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 13:49:03 2021

@author: 91994
"""

n=[1,2,5,6,-2,9,-3,-7,-1,-50]
print("The list k : ",n)
positive=[i for i in n if i>0]
print("Positive numbers are : ",positive)
n=[1,4,3,6,9,2,8]
print("The list is : ",n)
sq=[i*i for i in n]
print ("Square of numbers : ",sq)
s='comprehension'
print("The list is : ",s)
v=[i for i in s if i in 'aeiou']
print("Vowels in the list : ",v)
a=" python programming "
print("The word is " ,a) 
o=[ord(i) for i in a]
list=[20,10,55,9,3,60,1]
print("Orginal list : ",o)
new=[i for i in list if i%2!=0]
print("List after removing even numbers : ",new)
y=int(input("Enter the future year upto check : "))
print("List of leap years : ")
leap=[year for year in range (2020,y) if (year %4 == 0) and (year %100!= 0) or (year %400==0)]
print("leap years : ",leap)


