def solution(arr, query):
    answer = arr
    for i in range(len(query)):
        n = query[i]
        if i % 2 == 0:
            answer = answer[:n + 1]
        else:
            answer = answer[n:]
    return answer