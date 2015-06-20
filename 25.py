# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:14:14 2015

@author: miha
"""

# EULER PROBLEM #25

import timeit

start = timeit.default_timer()

fib = [1, 1, 2]
i = 3
condition = False
while condition == False:
    fib.append(fib[i-1] + fib[i-2])
    if len(str(fib[i])) >= 1000:
        condition = True
    i+=1
    
stop = timeit.default_timer()

print "Solution: " + str(i)          
print("Time consumed: " + str(stop - start))