def solution(arr):
    answer = arr
    answer.remove(min(arr))
    if not answer:
        answer.append(-1)
    return answer