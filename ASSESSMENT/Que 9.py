# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:54:15 2017

@author: User
"""

import re


def validate(s):
    if (len(s) > 6) and (len(s) < 12): 
        if (re.search('[a-z]',s)) and (re.search('[A-Z]',s)) and (re.search('[@$#]',s)) and (re.search('[0-9]',s)):
          
           return "Valid password"
        else:
           
            return "Invalid password"
            
def main():
    b = raw_input("enter password:")
    a=validate(b)
    print a        
    
    
        
    
    
