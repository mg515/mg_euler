# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:02:40 2015

@author: miha
"""

# EULER PROBLEM #23

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
        
def is_abundant(n):
    return sum(factors(n))-n > n

def find_abundant(limit):
    return [i for i in range(1,limit+1) if is_abundant(i)]
    
def all_sums(nums, limit):
    sums = set()
    for i in nums:
        for j in nums:
            if i+j <= limit:
                sums.add(i+j)
    return list(sums)

limit = 28123
uni = (limit+1)*limit/2
abundant = find_abundant(limit)
sums = all_sums(abundant, limit)
sol = uni - sum(sums)




stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))
