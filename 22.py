# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:35:31 2015

@author: miha
"""

# EULER PROBLEM #22

import pandas as pd
import timeit
import string

start = timeit.default_timer()

alphabet = string.ascii_uppercase
abdict = dict()
i = 1
for letter in alphabet:
    abdict[letter] = i
    i += 1

path = '/media/diskC/Documents and Settings/miha/Documents/euler/22t.txt'
df=pd.read_csv(path, sep=',', header=None)

names = list(df.values)[0]
names[3302] = 'NA'
names = sorted(names)

i = 1
solution = 0
for name in names:
    sums = 0
    for letter in name:
        sums = sums + abdict[letter]
    solution = solution + i*sums
    i+=1
    
stop = timeit.default_timer()

print "Solution: " + str(solution)          
print("Time consumed: " + str(stop - start))