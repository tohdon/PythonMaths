# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 20:19:21 2022

@author: Don
"""

def fibnoacci(n):
    if n<=2:
        return 1
    else:
        totalfib = fibnoacci(n-1) + fibnoacci(n-2)
        return totalfib
    
print(fibnoacci(5))