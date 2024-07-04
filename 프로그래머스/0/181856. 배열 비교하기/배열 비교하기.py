def solution(arr1, arr2):
    length1, length2 = len(arr1), len(arr2)
    if length1 == length2:
        sum1, sum2 = sum(arr1), sum(arr2)
        if sum1 == sum2:
            answer = 0
        elif sum1 > sum2:
            answer = 1
        else:
            answer = -1
    elif length1 > length2:
        answer = 1
    else:
        answer = -1
    return answer