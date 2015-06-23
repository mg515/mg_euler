# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:11:26 2015

@author: miha
"""

# EULER PROBLEM #48

import timeit
import sys

start = timeit.default_timer()


def last10dig_p48(n):
    vs = 0
    mod = 10**10
    
    for i in range(1,n+1):        
        temp = i        
        
        for j in range(1,i):            
            temp *= i
            if temp >= sys.maxint:
                temp %= mod        
                
        vs += temp
        vs %= mod
    return vs


sol = last10dig_p48(10)


stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))