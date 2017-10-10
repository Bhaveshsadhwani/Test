# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 18:47:38 2017

@author: User
"""

str=""
for row in range(0,7):
    for column in range(0,7):
        if ((column==0 or column ==5) and (row>0 and row<7) or (row==1) and (column==1 or column==5) or (row==2) and (column==2 or column==5) or (row==3 and column==3)):
            str=str+"*"
        else:
            str=str+""
    str=str+"\n"
print str