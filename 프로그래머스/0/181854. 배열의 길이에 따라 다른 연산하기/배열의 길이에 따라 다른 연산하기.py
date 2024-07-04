def solution(arr, n):
    length = len(arr)
    if length % 2 == 0:
        for i in range(length):
            if i % 2 != 0:
                arr[i] += n
    else:
        for i in range(length):
            if i % 2 == 0:
                arr[i] += n
    return arr