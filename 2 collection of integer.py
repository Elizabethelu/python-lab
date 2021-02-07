# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:28:22 2021

@author: 91994
"""

Set1 = {1,2,3,4}
Set2 = {4,5,6,7}
print("Set 1 : ", Set1)
print("Set 2 : ", Set2)
if (len(Set1) ==len(Set2)):
    print("Length of sets are equal " )
else :
    print("Length is not equal ")
if(sum (Set1) == sum (Set2)) :
    print("Sum of sets are equal " )
else :
    print("Sum are not equal ")
if(Set1.isdisjoint(Set2)) :
      print("No common elements " )
else :
    print("Have common elements : ", Set1.intersection(Set2))
      
    
     
  