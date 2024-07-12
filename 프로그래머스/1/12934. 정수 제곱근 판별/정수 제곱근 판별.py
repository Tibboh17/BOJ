from math import sqrt

def solution(n):
    temp = int(sqrt(n))
    if temp ** 2 == n:
        answer = (temp + 1) ** 2
    else:
        answer = -1
    return answer