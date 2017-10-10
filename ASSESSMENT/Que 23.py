# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:33:01 2017

@author: User
"""

fo=open("Demo.txt","a")
str=raw_input("Enter the string:")

fo.write(str)
fo.close()
f1=open("Demo.txt","r")
a=f1.readlines()
print a
