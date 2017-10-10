# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:41:30 2017

@author: User
"""

def binary(List,x,lower=0,high="none"):
    if high is "none":
        high=len(List)
    while lower<high:
        mid=lower+high//2
        middle=List[mid]
        if middle < x:
            lower=mid+1
        elif middle>x:
            high=mid
        else:
            return mid
    return -1
            
                
binary([1,2,3,4,5,6],2)
        