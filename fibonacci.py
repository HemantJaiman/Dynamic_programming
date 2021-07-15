

#### with lru caching method ######### 
'''
from functools import lru_cache
@lru_cache(maxsize=16)
def fib(n):
    if n<=2 : 
        return 1
    return fib(n-1) + fib(n-2)

print(fib(50))
'''

######################### with memoization technique #########
def fib(n,memo):
    
    if (n in memo):
        return memo[n]
    if n<=2 : 
        return 1
    memo[n]  = fib(n-1,memo) + fib(n-2,memo)
    
    return memo[n]
memo={}
print(fib(15,memo))

