# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:25:38 2017

@author: User
"""

str=""

for row in range(0,7):
    for column in range(0,7):
        if ((row==0 or row==6) and (column>=0 and column<5) or (row==3) and (column>=0 and column<4) or (column==0) and (row>0 and row<7)):
            str=str+"*"
        else:
            str=str+""
            
    str=str+"\n"
    
print str