def solution(t, p):
    answer = 0
    numlist = [int(t[i:i + len(p)]) for i in range(len(t) - len(p) + 1)]
    for num in numlist:
        if num <= int(p):
            answer += 1
    return answer