# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:14:14 2015

@author: miha
"""


fib = [1, 1, 2]
i = 3
pogoj = False
while pogoj == False:
    fib.append(fib[i-1] + fib[i-2])
    if len(str(fib[i])) >= 1000:
        pogoj = True
    i+=1