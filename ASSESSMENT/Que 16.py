# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:55:00 2017

@author: User
"""
count=0
fo=open("Demo.txt","r")
a=fo.readlines()
for i in a:
    count = count +1
print count
print (a)    
    
