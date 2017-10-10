# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:38:53 2017

@author: User
"""

str=""

for row in range(0,6):
    for column in range(0,6):
        if ((column==0) and(row>=0 and row<6) or (row==5) and (column>=0 and column < 4)):
            str = str+"*"
            
        else:
            str=str+""
            
    str=str+"\n"
print str