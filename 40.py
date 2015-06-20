# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:29:24 2015

@author: miha
"""

# EULER PROBLEM #40

import timeit

start = timeit.default_timer()

numbers = ""
i = 1
j = 0
while j < 1000010:
    j+=len(str(i))
    numbers = numbers + str(i-1)
    i+=1
    
sol = 1
i = 1
while i < 100000:
    i *= 10
    sol = sol * int(numbers[i])
    

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))