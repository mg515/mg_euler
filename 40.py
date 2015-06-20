# -*- coding: utf-8 -*-
"""
Created on Thu May 28 22:29:24 2015

@author: miha
"""

stevila = ""
i = 1
j = 0
while j < 1000010:
    j+=len(str(i))
    stevila = stevila + str(i-1)
    i+=1
    
rez = 1
i = 1
while i < 100000:
    i *= 10
    rez = rez * int(stevila[i])
    print(int(stevila[i]))
    print(rez)
    print(i)