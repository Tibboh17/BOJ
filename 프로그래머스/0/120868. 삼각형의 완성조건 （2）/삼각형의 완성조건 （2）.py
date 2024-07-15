def solution(sides):
    answer = 0
    m, n = max(sides), min(sides)
    
    for i in range(m - n + 1, m + 1):
        answer += 1
    for j in range(m + 1, m + n):
        answer += 1
        
    return answer