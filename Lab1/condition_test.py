# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:27:58 2019

@author: minhta16
"""

x = int(input("Please enter a number: "))
if x < 3:
    print("small x")
elif x < 10:
    print("medium x")
else:
    print("big x")
    
honorific = "Dr."
name = input("Enter your surname: ")
if honorific == "Dr.":
    if name == "Sward":
        print("Your name is a weapon.")
    elif name == "Stonedahl":
        print("Your name was merged with your wife's when you married.")
    else:
        print("Sorry, I've never heard of Dr.", name)

smallPrimes = [2,3,5,7]
for prime in smallPrimes:
    print(prime, "is prime")
    
for i in range(1,10,2):
    print(i, "is odd")
    
def squareIt(num):
    return num * num;

answer = squareIt(9)

