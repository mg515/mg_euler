# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 23:06:34 2015

@author: miha
"""

# EULER PROBLEM #19

import timeit
from datetime import date
from datetime import timedelta


start = timeit.default_timer()

nedelja = date(1901, 1, 7)
i = 0
while nedelja.year < 2000:
    if nedelja.day == 1:
        i += 1
    nedelja += timedelta(days=7)
    
sol = i
    


stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))
