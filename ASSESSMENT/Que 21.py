# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:12:52 2017

@author: User
"""

fo=open("Demo.txt","r")
a=fo.readlines()
for i in reversed(a):
    print i
