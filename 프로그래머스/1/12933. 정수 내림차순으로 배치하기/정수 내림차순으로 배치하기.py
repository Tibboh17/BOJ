def solution(n):
    arr = [int(i) for i in str(n)]
    reverse = [str(j) for j in sorted(arr, reverse=True)]
    return int("".join(reverse))