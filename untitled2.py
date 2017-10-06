# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 11:04:57 2017

@author: User
"""
 Write a Python program which accepts the user's first and
 last name and print them in reverse order with a space between them

First_name = raw_input("Enter the First Name: ")

Last_name = raw_input("Enter the Last Name: ")

print Last_name +" "+ First_name




Write a Python program which accepts a sequence of comma-separated numbers
 from user and generate a list and a tuple with those numbers


a = raw_input("Enter the Numbers:")

List = a.split(',')
print "List:",List

Tuple = tuple(List)
print "Tuple:",Tuple



import math

r = 6.0

volume = 4.0/3.0 * math.pi * r**3

print volume 




Write a Python program to get the difference between a given number and 17, 
if the number is greater than 17 return double the absolute difference:
    
    
a = input("Enter the number:")

b = 17

c = a - b

if (c > 17):
    
    d = c*c
    
    print d
    
else:
    print c


 Write a Python program to calculate the sum of three given numbers
 , if the values are equal then return thrice of their sum
 
 
a = input("Enter the value of a:")
b = input("Enter the value of b:")
c = input("Enter the value of c:")

sum = a + b + c

if (a==b==c):
    print sum*3
else:
    print sum



Write a Python program to find those numbers which are divisible by 7 
and multiple of 5, between 1500 and 2700 (both included).


for x in range(1500,2700):
    if (x%7==0) and (x%5==0):
        print x
        
    else:
        print "Wrong logic"





import random
user_no = random.randint(1,10)
guessed_no = 2

while(user_no!=guessed_no):
    guessed_no=input("Try again:")
print "Right guess"



for i in range(0, 5):
	for j in range(0, i+1):
		print("* ",end=" ")
	print()   



for g in range (6,0,-1):
    print(g * ' ' + (6-g) * '*')
    
    
    
    
    
    
for i in range(1,6,1):
    print(i * ' '+ (1+i) * '*' )



numbers=(1,2,3,4,5,6,7)
Ecount=0
Ocount=0
for x in numbers:
    if (x%2==0):
        Ecount=Ecount+1
        
    else:
        Ocount=Ocount+1
        
        
print Ecount
print Ocount
        
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1),
            [5, 12], {"class":'V', "section":'A'}]

for x in datalist:
    print ("Type of", x ,"is", type(x))





for i in range(0,5):
    for j in range(0,i+1):
        print ("*"),
    print    


for i in range(0,5):
    for j in range(i+1,5):
        print ("*"),
        
    print    

for x in range(0,50):
    if(x%3==0):
        print "Fizz",
    if(x%5==0):
        print "Buzz",
    if(x%3==0) and (x%5==0):
        print "FizzBuzz",
    else:
        print x

values=1111,1001,1010,0110,0011

if(values%5==0):
    print values.split(',')



str="bhavesh"
print str.count('h')
print str.endswith('h')
print str.find('y')
print str.index('h')
print str.isalnum()

str1 = "_"
seq = ("aa","bb","cc")
print str1.join(seq)

print str.lower()

print str.upper()
print max(str)

print str.split(',')

List = list(seq)
print List

print List.append(str)
print List.extend(str)

List.remove('aa')
print List

List.pop(0)
print List

Tuple = 1,3.5,"hello"  #packing
print Tuple

dict={1:'Bhavesh',2:'asish'}
print dict.pop(1)
print dict

L = list(dict)
print L








lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)





#Write a Python program that accepts an integer
# (n) and computes the value of n+nn+nnn.


n = int(input("Enter the Number:"))

n1 = int("%d" % n)
n2 = int("%d%d" % (n,n))
n3 = int("%d%d%d" % (n,n,n))

result = (n1 + n2 + n3)


print "Value of n is:" ,result



import sys
print dir(sys)
print "version::",sys.version
print sys.version_info





import math

r=input("Enter the radius:")

area=math.pi*r*r

print "Area of circle:", area


#from math import pi 
#
#r = float(input ("Input the radius of the circle : "))
#
#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

    
    
