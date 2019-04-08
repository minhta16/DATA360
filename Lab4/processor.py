# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:30:51 2019

@author: Minh Ta
"""

import pandas as pd

def cleanData(fullDat):
    
    fullDat['B-T'] = fullDat['Custom Field 1'].combine_first(fullDat['B-T'])
    del fullDat['Custom Field 1']
    
    fullDat['Name'] = fullDat['Name'].combine_first(fullDat['NAME']).combine_first(fullDat['Full Name'])
    del fullDat['NAME']
    del fullDat['Full Name']
    
    fullDat['Events'] = fullDat['Event'].combine_first(fullDat['Events'])
    del fullDat['Event']
    
    fullDat['Hometown'] = fullDat['Hometown'].combine_first(fullDat['HOMETOWN'])
    del fullDat['HOMETOWN']
    
    fullDat['Captain'] = fullDat['Captain'].combine_first(fullDat['C'])
    del fullDat['C']
    
    fullDat['Ht'] = fullDat['Ht'].combine_first(fullDat['HT']).combine_first(fullDat['Ht.'])
    del fullDat['HT']
    del fullDat['Ht.']
    
    fullDat['High School'] = fullDat['High School'].combine_first(fullDat['HIGH SCHOOL'])
    del fullDat['HIGH SCHOOL']
    
    fullDat['Letters'] = fullDat['Letters'].combine_first(fullDat['LETTERS'])
    del fullDat['LETTERS']
    
    fullDat['No'] = fullDat['No'].combine_first(fullDat['NO'])
    del fullDat['NO']
    
    fullDat['Pos'] = fullDat['Pos'].combine_first(fullDat['POS']).combine_first(fullDat['Pos.'])
    del fullDat['POS']
    del fullDat['Pos.']
    
    fullDat['Wt'] = fullDat['Wt'].combine_first(fullDat['Wt.'])
    del fullDat['Wt.']
    
    fullDat['Year'] = fullDat['Year'].combine_first(fullDat['YR']).combine_first(fullDat['Yr']).combine_first(fullDat['Yr.'])
    del fullDat['YR']
    del fullDat['Yr']
    del fullDat['Yr.']
    
    fullDat.to_csv("augie_athletes_clean.csv")
    print(fullDat.keys())
    
def feetToInches(height):
    heightSplit = height.split('-')
    return int(heightSplit[0]) * 12 + int(heightSplit[1])
    
    return int(height.split())
fullDat = cleanData(pd.read_csv("augie_athletes.csv"))
