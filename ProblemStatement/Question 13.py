# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 12:26:21 2017

@author: User
"""

user = raw_input("Enter a alphabet:")

if user in ('a','e','i','o','u') and user in ('A','E','I','O','U'):
    print "It is a vowel"
    
else:
    print "It is consonant"