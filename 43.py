# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 10:41:54 2015

@author: miha
"""

# EULER PROBLEM #43

import timeit
import itertools as it

start = timeit.default_timer()

def make_int(nums):
    return int(''.join(map(str, nums)))

def find_pandigital():
    
    pandigit_sum = 0
    primes = [2,3,5,7,11,13,17]
    
    for perm in it.permutations(range(0,10)):
        cond = True
        # start from the last condition, takes out most of the numbers:
        for i in range(len(primes))[::-1]:
            if make_int(perm[(i+1):(i+4)]) % primes[i] != 0:
                cond = False
                break
        if cond:
            pandigit_sum += make_int(perm)
    return pandigit_sum
                

sol = find_pandigital()
                

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))