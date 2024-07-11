def solution(arr, queries):
    answer = arr
    for query in queries:
        for i in range(query[0], query[1] + 1):
            if i % query[2] == 0:
                answer[i] += 1
    return answer