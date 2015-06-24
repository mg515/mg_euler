# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 23:10:46 2015

@author: miha
"""

# EULER PROBLEM #145
# does not work yet

import timeit

start = timeit.default_timer()


def reverse(n):
    return int(str(n)[::-1])
    
def check_dig_oddity(n):
    digits = map(int, str(n))
    for i in range(len(digits)):
        if digits[i] % 2 == 0:
            return False
    return True


def check_zeros(n):
    string = str(n)
    k = len(string)
    if int(string[k-1])==0:
        return True
    return False


sol = 0
for i in range(1,10**7):
    revd = reverse(i)
    sumd = i + revd
    if not check_dig_oddity(sumd):
        continue
    if check_zeros(i):
        continue
    sol += 1
    
    
    
           

stop = timeit.default_timer()

print "Solution: " + str(sol)          
print("Time consumed: " + str(stop - start))
