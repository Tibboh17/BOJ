from math import sqrt

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        temp = int(sqrt(i))
        if temp ** 2 == i:
            answer -= i
        else:
            answer += i
    return answer