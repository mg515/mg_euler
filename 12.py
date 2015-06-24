# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:14:31 2015

@author: miha
"""

# EULER PROBLEM #12

import timeit
from math import sqrt

start = timeit.default_timer()

def factors(n):
    facs = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            facs.add(i)
            facs.add(n//i)
    return list(facs)
        
    
triangle = 0
k = 1
cond = False
while cond == False:
    triangle += k
    k += 1
    num_facs = len(factors(triangle))
    if num_facs > 500:
        cond = True
        
sol = triangle
stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))
