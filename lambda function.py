# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:03:19 2021

@author: 91994
"""
large=lambda a,b : max(a,b)
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
print("Largest : ", large(n1,n2))
div=lambda a: print("divisible by 5 : ")if not a%5 else print("Not divisible by 5 : ")
n=int(input("Enter number : ")) 
div(n)
s=['red','blue','black','rose','white']
result=list(filter(lambda a:len(a)>5,s)) 
print("New list : ",result)
n=[200,50,1300,800]
result=list(map(lambda a: a+a*0.1 if a>1000 else a+a*0.05,n))
print("Result : ",result)
      
        
        
    

