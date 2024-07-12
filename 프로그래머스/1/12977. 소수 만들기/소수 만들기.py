from math import sqrt
from itertools import combinations

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    
def solution(nums):
    cnt = 0
    comb = list(combinations(nums, 3))
    for arr in comb:
        if is_prime(sum(arr)):
            cnt += 1
    return cnt