def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        numSet = set(str(i))
        if (numSet == {"0"}) or (numSet == {"5"}) or (numSet == {"0", "5"}):
            answer.append(i)
        
    if not answer:
        answer.append(-1)
        
    return answer