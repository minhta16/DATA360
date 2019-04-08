# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:59:22 2019

@author: Minh Ta
"""

import pandas as pd
import requests      # for requesting data from the web
import re            # for regular expressions (fancy text searching)
import time          # for delaying

headers = {'User-Agent': "Augustana's DATA 360 Class"}
rosterDatList = []
for i in range(1, 177):
    time.sleep(1)
    try:
        URL = "https://athletics.augustana.edu/roster.aspx?roster="+str(i)
        raw_html = requests.get(URL, headers=headers).content
        
        # players are in table #2 that pandas finds on the page
        rosterDat = pd.read_html(raw_html)[2]
        
        # use a 'regular expression' to find the title of the page
        pageTitle = re.findall('<h2>(.*?)</h2>', str(raw_html))[0]
        rosterDat['title'] = pageTitle
        rosterDatList.append(rosterDat)
    except Exception as ex:
        print("Failed scraping", URL)
        print("Error message:", ex)
        
fullDat = pd.concat(rosterDatList)
fullDat.to_csv("augie_athletes.csv")