# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:22:03 2017

@author: User
"""

"""Runtime Exception"""

a=input("Enter a number:")
b=input("Enter a number:")

try:
    sum=a/b
    print sum
    
except ZeroDivisionError as ze:
    print ze
    
 




    


