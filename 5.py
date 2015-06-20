# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:59:23 2015

@author: miha
"""

a = 2520
pogoj = True


while pogoj == True:
    pogoj = False
    k = 0
    for i in range(10,21)[::-1]:
        if a%i != 0:
            pogoj = True
            break
    if k == 10:
            pogoj = False
            
    a += 2520            
            
print a