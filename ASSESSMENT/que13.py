# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:46:14 2017

@author: User
"""

num=input("enter positive number ")

while (num > 1):
    if (num%2==0):
        num=num/2
        print num
    else:
        num = 3*num+1
        print num
