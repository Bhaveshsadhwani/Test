# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:49:42 2017

@author: User
"""

numheads=35
numlegs=94
for rabbits in range(0,numheads+1):
    chickens=numheads-rabbits
    if chickens * 2 + 4 * rabbits == numlegs:
        print chickens
        print rabbits