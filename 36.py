# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:27:21 2015

@author: miha
"""

# EULER PROBLEM #36

import timeit

def toBin(x):
    binary = ''
    if x == 0:
        return 0
    while x != 0:
        binary += str(int(x % 2))
        x = x // 2
    return int(binary[::-1])
        
        
def ispalindrom(x): # copied this from my prob #4 solution
    x = str(x)
    if int(len(x)) == 1:
        return True
    else:
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-i-1]:
                return False
    return True
    
    
start = timeit.default_timer()    

sez = [i for i in range(1000000) if ispalindrom(i) and ispalindrom(toBin(i))]
sol = sum(sez)

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))