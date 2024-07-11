def solution(arr, queries):
    answer = []
    for query in queries:
        query_arr = [
            arr[i] for i in range(len(arr)) 
            if (query[0] <= i <= query[1]) and arr[i] > query[2]
        ]
        if query_arr:
            answer.append(min(query_arr))
        else:
            answer.append(-1)
    return answer