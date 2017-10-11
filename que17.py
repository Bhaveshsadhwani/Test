# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:44:56 2017

@author: User
"""

class Circle:
    
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        Area=3.14*self.radius*self.radius
        print Area
        
        
object=Circle(5)

object.area()