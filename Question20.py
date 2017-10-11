# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 17:14:49 2017

@author: User
"""

class Person:
    def getGender(self):
        pass
    
class Male(Person):
    def getGender(self):
        print 'Male'
        
class Female(Person):
    def getGender(self):
        print 'Female'
        
class main():
    Male().getGender()
    Female().getGender()
    
if __name__ == "__main()__":
    main()