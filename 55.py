# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:40:18 2015

@author: miha
"""

# EULER PROBLEM #55

import timeit

start = timeit.default_timer()


def is_palindrom(n):
    return str(n)==str(n)[::-1]

def invert(n):
    return int(str(n)[::-1])

def is_lychrel(n, rec_control):
    if rec_control >= 50:
        return True
    sumd = n + invert(n)
    if is_palindrom(sumd):
        return False
    rec_control += 1
    return is_lychrel(sumd, rec_control)
	


sol = len([i for i in range(10000) if is_lychrel(i,1)])
    


stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))
