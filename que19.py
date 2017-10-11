# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:49:08 2017

@author: User
"""

class Demo:
    
    def __init__(self,string):
        self.string=string
        
    def __print__(self):
        print self.string
        
        
objectD1=Demo("Hello")
objectD2=Demo("BBye")

objectD1.__print__()
objectD2.__print__()