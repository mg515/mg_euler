# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:27:21 2015

@author: miha
"""



def toBin(x):
    binarno = ''
    if x == 0:
        return 0
    while x != 0:
        binarno += str(int(x % 2))
        x = x // 2
    return int(binarno[::-1])
        
        
def ispalindrom(x): #iz naloge 4 
    x = str(x)
    if int(len(x)) == 1:
        return True
    else:
        for i in range(int(len(x)/2)):
            if x[i]!=x[len(x)-i-1]:
                return False
    return True
    
    
sez = [i for i in range(1000000) if ispalindrom(i) and ispalindrom(toBin(i))]
vs = sum(sez)
