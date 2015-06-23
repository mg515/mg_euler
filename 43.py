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
    prastevila = [2,3,5,7,11,13,17]
    
    for kombi in it.permutations(range(0,10)):
        k = 0
        for i in range(len(prastevila)):
            if make_int(kombi[(i+1):(i+4)]) % prastevila[i] == 0:
                k += 1
        if k == 7:
            pandigit_sum += make_int(kombi)
    return pandigit_sum
                

sol = find_pandigital()
                

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))