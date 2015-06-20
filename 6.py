# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 21:10:53 2015

@author: miha
"""



def razlika6(n):
    stevila = [i for i in range(n+1)]
    kvadrat = sum(stevila)**2    
    vsota = [0 for i in range(n+1)]
    for i in range(1,n+1):
        vsota[i] = vsota[i-1] + i**2
    return kvadrat-vsota[n]
    
    

import timeit

start = timeit.timeit()
print razlika6(100)
end = timeit.timeit()
print end - start     
     