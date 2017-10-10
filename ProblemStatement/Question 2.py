# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 10:41:54 2017

@author: User
"""

T = raw_input("Enter the Temperature:")
Number = T[0:-1]
celsius = T[-1]
if (celsius=="C"):
    Ans = int(Number * 1.8 + 32)
    print "Temperature in Farenheit:", Ans
    
elif (celsius=="F"):
    Ans = int((Number - 32)/1.8)
    print "Temperature in Celcius:", Ans
    
else:
    print "Invalid Input"