# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 17:38:37 2017

@author: User
"""


str=""
for rows in range(0,7):
    for column in range(0,7):
        if((rows==0 or rows==6) and (column>0 and column <5) or (column == 1 or column == 5) and (rows > 0 and rows < 6)):
            str=str+"*"
            
        else:
            str=str+" "
    str=str+"\n"
print str        

            
    