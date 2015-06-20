# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:59:23 2015

@author: miha
"""

# EULER PROBLEM #5

import timeit


start = timeit.timeit() # start time

num = 2520
condition = True
while condition == True:
    condition = False
    k = 0
    for i in range(10,21)[::-1]:
        if num%i != 0:
            condition = True
            break
    if k == 10:
            condition = False
            
    num += 2520            
            
print "Solution: " + str(num)
stop = timeit.timeit() # end time
print("Time consumed: " + str(stop - start))