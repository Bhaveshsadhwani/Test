# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 11:42:06 2017

@author: User
"""

import re

User = raw_input("Enter the Password:")

if (len(User) > 6) and (len(User) < 16): 
    if (re.search('[a-z]',User)) and (re.search('[A-Z]',User)) and (re.search('[$#@]',User)) and (re.search('[0-9]',User)):
        print "valid Password"
    
    else:
        print "Invalid password"
    