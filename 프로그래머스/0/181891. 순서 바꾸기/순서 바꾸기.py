def solution(num_list, n):
    left = num_list[:n]
    right = num_list[n:]
    answer = right + left
    return answer