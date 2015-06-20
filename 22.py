# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:35:31 2015

@author: miha
"""


import pandas as pd

import string
abeceda = string.ascii_uppercase



abdict = dict()
i = 1
for crka in abeceda:
    abdict[crka] = i
    i += 1

pot = '/media/miha/6EB86D86B86D4E21/Documents and Settings/miha/Documents/euler/22t.txt'
df=pd.read_csv(pot, sep=',', header=None)

imena = list(df.values)[0]
imena[3302] = 'NA'
imena = sorted(imena)

i = 1
rezultat = 0
for ime in imena:
    vsota = 0
    for crka in ime:
        vsota = vsota + abdict[crka]
    rezultat = rezultat + i*vsota
    i+=1
        
                
