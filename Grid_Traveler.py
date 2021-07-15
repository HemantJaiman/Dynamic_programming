# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:05:27 2021

@author: Hackie_Packie
"""
'''
from functools import lru_cache
@lru_cache(maxsize=16)


def grid_traveler(m,n):
    if(m == 1 and n == 1):
        return 1
    if(m==0 or n==0):
        return 0
        
    return grid_traveler(m-1, n) + grid_traveler(m, n-1)

print(grid_traveler(18, 18))
'''

def grid_traveler(m,n,memo):
    
    key = str(m)+','+str(n)
    
    if key in memo:
        return memo[key]
    if(m == 1 and n == 1):
        return 1
    if(m==0 or n==0):
        return 0
    
    memo[key] = grid_traveler(m-1, n,memo) + grid_traveler(m, n-1,memo)
    
    return memo[key]
memo={}
print(grid_traveler(11, 11,memo))