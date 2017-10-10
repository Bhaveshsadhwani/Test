# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:15:11 2017

@author: User
"""

sum=0
Number=input("Enter positive Number:")

while(Number > 0):
    digit = Number % 10
    sum = sum + digit
    Number = Number/10
    
print sum
    