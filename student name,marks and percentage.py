# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 11:21:38 2021

@author: 91994
"""

import collections
student=collections.namedtuple("Student","rollno name marks")
subject=collections.namedtuple("Students","Physics Chemistry Biology")
Elizabeth=student("13","Elizabeth",482)
print("Name of the student : %s \n Total marks : %d \n Percentage : %.2f"%(Elizabeth.name,Elizabeth.marks,(Elizabeth.marks*100)/500))
