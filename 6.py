# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:10:53 2015

@author: miha
"""

# EULER PROBLEM #6

def diff_EP6(n):
    numbers = [i for i in range(n+1)]
    squares = sum(numbers)**2    
    part_sums = [0 for i in range(n+1)]
    for i in range(1,n+1):
        part_sums[i] = part_sums[i-1] + i**2
    return squares-part_sums[n]
    
    

import timeit

start = timeit.timeit()
print "Solution: " + str(diff_EP6(100000))
stop = timeit.timeit()
print("Time consumed: " + str(stop - start))