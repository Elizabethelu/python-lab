# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:36:22 2021

@author: 91994
"""

def area(l,b):
    area=l*b
    return area
def peremeter(l,b):
    perimeter=2*(l*b)
    return peremeter
def area(r):
    return(3.14*r*r)
def peremeter(r):
    return(2*3.14*r)
__all__=['area','perimeter']
def area(l,b,h):
    area=2*((l*b)+(b*h)+(h*l))
    return area
def perimeter(l,b,h):
    perimeter=4*(l+b+h)
    return perimeter
def circumference(r):
    return(2*3.14*r)
def area(r):
    return(4*3.14*r)
import graphics.rectangle
print("Rectangle")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
print("Area : ",graphics.rectangle.area(l,b))
print("Perimeter : ",graphics.rectangle.perimeter(l,b))
from graphics.circle import area as a
from graphics.circle import perimeter as p
print("Circle")
a.r=int(input("Enter the radius : "))
print("Area : ",a(r))
print("Perimeter : ",p(r))
from graphics.dgraphics.cuboid import area as a
from graphics.dgraphics.cuboid import perimeter as p
print("Cuboid")
l=int(input("Enter the length : "))
b=int(input("Enter the breadth : "))
h=int(input("Enter the height : "))
print("Area : ",a(l,b,h))
print("Perimeter : ",p(l,b,h))
from graphics.dgraphics.sphere import *
print("Sphere")
r=int(input("Enter the radius : "))
print("Area : ",area(r))
print("Circumference : ",circumference(r))
