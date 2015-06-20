# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:47:49 2015

@author: miha
"""

# EULER PROBLEM #14

import timeit

def collatz(n, dik=None): # dik = dictionary variable
    i = 1
    while n != 1:
        try:
            i1 = dik[n]
            return i1+i, dik
        except:
            if n%2 == 0:
                n = n/2
                i = i+1
            else:
                n = 3*n + 1
                i = i+1
    return i, dik
        
start = timeit.default_timer()
dik = dict()
for i in range(1000000):
    dik[i+1], dik = collatz(i+1, dik)
stop = timeit.default_timer()

m = max(dik, key=dik.get)
print "Solution: " + str(m)

print("Time consumed: " + str(stop - start))
#3.6s