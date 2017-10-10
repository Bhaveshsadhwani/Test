# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 14:59:42 2017

@author: User
"""




import re

User = raw_input("Enter the Password:").split(',')

str = []
for password in User:
    if (password in range(6,12)):
        if (re.search('[a-z]',password)) and (re.search('[A-Z]',password))  and (re.search('[0-9]',password)):
            str.append(password)
print str            
            
        
    
    
        
    
       
            
            
               
               
       
        
        
     
