# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:32:57 2019

@author: minhta16
"""

import matplotlib.pyplot as plt

# Start account with $0 and each year deposit $10, then $20, then $30, etc.
numYears = int(input("How many years (whole number)? "))
interestRate = float(input("What interest rate percent (e.g. 6)? "))
balance = 0
balanceOverTime = [] # empty list
yearList = range(numYears+1)

for year in yearList:
    balance = balance * (1 + interestRate / 100)  + year * 10
    balanceOverTime.append(balance) # add balance to the end of the list
    
plt.figure() # makes a new figure
plt.plot(yearList, balanceOverTime, "r*:") # red, star markers, dotted line
plt.bar(yearList, balanceOverTime)
plt.xlabel("years")
plt.ylabel("$")
plt.title("bank balance over time")