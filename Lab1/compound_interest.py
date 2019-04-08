# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 09:26:14 2019

@author: minhta16
"""

principle = 1000
interestRate = float(input("What interest rate percent? (e.g. 6) "))
interest = principle * (1 + (interestRate / 100)) ** 3
print("Interest after 3 years compounded annually: " + str(interest))