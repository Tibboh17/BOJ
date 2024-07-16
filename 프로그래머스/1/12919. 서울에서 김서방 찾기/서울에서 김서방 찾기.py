def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            idx = i
            break
    answer = f"김서방은 {idx}에 있다"
    return answer