# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:36:22 2021

@author: 91994
"""

from graphics.rectangle1 import *
from graphics.circle1 import *
from graphics.dgraphics.sphere1 import *
from graphics.dgraphics.cube1 import *
rl=int(input("Enter the length of rectangle : "))
rb=int(input("Enter the breath : "))
print('\nArea of rectangle :',rectarea(rl,rb))
print("Perimeter of rectangle : ",rectperimeter(rl,rb))      
print('\n \n')
cr=int(input("Enter the radius of the circle : "))
print('\nArea of circle : ',cirarea(cr))
print("Perimeter of circle : ",cirperimeter(cr))
print('\n \n')
cl=int(input("Enter the length of the cuboid : "))
cb=int(input("Enter the breath of cuboid : "))
ch=int(input("Enter the height of the cuboid : "))
print('\nArea of cuboid :',cubarea(cl,cb,ch))
print("Perimeter of cuboid : ",cubperimeter(cl,cb,ch))
print('\n \n')
sr=int(input("Enter the radius of sphere : "))
print('\nArea of sphere : ',spherearea(sr))
print("Circumference of sphere : ",spherecircum(sr))
