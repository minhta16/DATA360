
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
 
fullDat = pd.read_csv("augie_athletes_clean.csv")
 
# Challenge A
def feetToInches(height):
    heightSplit = height.split('-')
    if (len(heightSplit) == 2 and heightSplit[1] != ''):
        return int(heightSplit[0]) * 12 + int(heightSplit[1])
    return 0
    
fullDat.Ht.fillna('0', inplace=True)
fullDat['height_inches'] = fullDat.Ht.apply(feetToInches)

# Challenge B
print("\n\nTallest athletes: ", fullDat[fullDat['height_inches'] == fullDat['height_inches'].max()])
"""
 Comments: The tallest person is in the basketball team and he has been playing for Augie for 2 seasons.
"""

# Challenge C
print("\n\nShortest athletes: ", fullDat[fullDat['height_inches'] == fullDat[fullDat['height_inches'] > 0].min()['height_inches']])
"""
 Comments: There are 2 shortest athletes, Hilary Kargl and Natalie Rosborough. Hilary played for Lacrosse and Natalie is playing for Volleyball.
"""


# Challenge E

def findBasketball(str):
    return str.find('Basketball') != -1

import matplotlib.pyplot as plt

hasHtDat = fullDat[fullDat['height_inches'] != 0]
meanBasket = hasHtDat[hasHtDat['title'].apply(findBasketball)]['height_inches'].mean()
meanNonBasket = hasHtDat[~hasHtDat['title'].apply(findBasketball)]['height_inches'].mean()
    
meanHt = [meanBasket, meanNonBasket]
x = range(len(meanHt))

fig, ax = plt.subplots()
plt.bar(x, meanHt)
plt.xticks(x, ('Basketball', 'Non-Basketball'))
plt.ylabel('Mean Height')
plt.xlabel('Player')
plt.title('Mean Height between Basketball and Non-Basketball Player')
plt.gca().set_ylim(bottom=68, top=74)
plt.show()

"""
 Comments: This graph shows that the average height of basketball players is greater than that of non-Basketball players.
             To test this thoroughly we need a satistic test though.
"""
