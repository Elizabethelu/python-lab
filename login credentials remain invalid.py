# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 13:47:17 2021

@author: 91994
"""

class LoginError(Exception):pass
try:
    user_name1="abcde"
    password1="A123"
    user_name2=input("Enter the user name : ")
    password2=input("Enter the password : ")
    if user_name1==user_name2 and password1==password2 :
        print("Successfull login ")
    else:
        raise LoginError("Invalid username or password ")
except LoginError as e:
       print(e)
        