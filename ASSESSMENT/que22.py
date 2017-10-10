# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:24:20 2017

@author: User
"""

str="hello world! 123"
dcount=0
acount=0
for i in str:
    if (i.isdigit()==True):
        dcount=dcount+1
        
    elif (i.isalpha()==True):
        acount=acount+1
        
print "No. of Digits:",dcount 
print "No. of Alphabets:",acount 