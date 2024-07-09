def solution(n):
    if n % 2 != 0:
        arr = [i for i in range(1, n + 1, 2)]
    else:
        arr = [j * j for j in range(2, n + 1, 2)]
    answer = sum(arr)
    return answer