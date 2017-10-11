# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:05:51 2017

@author: User
"""

class Custom_exception(Exception):
    
    def __init__(self,message):
        self.message=message
        
raise Custom_exception("Error Occured")