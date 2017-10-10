# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:31:07 2017

@author: User
"""

a=[1,2,3,4,6,7,8]
length=len(a)

b=[x for x in range(a[0],a[-1]+1)]
a=set(a)
print list((a) ^ set(b))