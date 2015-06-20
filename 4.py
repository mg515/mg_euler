# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:13:47 2015

@author: miha
"""
     
def ispalindrom(x):
    x = str(x)
    if int(len(x)) ==1:
        return True
    else:
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-i-1]:
                return False
    return True
    

maks = 0    
for i in range(100, 1000):
    for j in range(100, 1000):
        k = i*j
        if ispalindrom(k) and k > maks:
            maks = k