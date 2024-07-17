def solution(arr):
    if 2 not in arr:
        answer = [-1]
    else:
        idx = []
        for i in range(len(arr)):
            if arr[i] == 2:
                idx.append(i)
        answer = arr[min(idx):max(idx) + 1]
    return answer