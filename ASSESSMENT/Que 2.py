# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:37:03 2017

@author: User
"""

str=""
num=65
for i in range(0,5):
    for j in range(0,i+1):
      str=str+chr(num)
      
      num=num+1
    str=str+"\n"
print str      