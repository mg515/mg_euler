# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:45:56 2015

@author: miha
"""

# EULER PROBLEM #32

import timeit

start = timeit.default_timer()

# makes a int out of list
def make_int(nums):
    return int(''.join(map(str, nums)))





a = find_pandigital()
sol = sum(a)

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))