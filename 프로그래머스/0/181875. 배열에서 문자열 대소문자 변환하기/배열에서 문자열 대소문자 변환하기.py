def solution(strArr):
    answer = strArr
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer[i] = answer[i].lower()
        else:
            answer[i] = answer[i].upper()
    return answer