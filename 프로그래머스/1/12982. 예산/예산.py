def solution(d, budget):
    d.sort()
    while True:
        if sum(d) <= budget:
            break
        d.pop()
    answer = len(d)
    return answer