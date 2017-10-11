# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:57:46 2017

@author: User
"""


def Operation(s):
    balance = 0
    while True:
        
        if s[0].upper() == 'D':
            balance += int(s[1:])
    
        elif s[0].upper() == 'W':
            if int(s[1:]) > balance:
                print("you have not sufficient amount Please Enter valid amount")
            else:
                balance -= int(s[1:])
                print "current balance is:",balance   
        else:
            print ("Enter valid operation")
            break
        
        s = raw_input("Enter amount to be deposited eg.D350 or withdrawan eg.W250:")



s = raw_input("Enter amount to be deposited EX.D350 or withdrawan EX.W250:")

Operation(s)