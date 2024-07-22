def solution(num_list):
    even_sum = 0
    odd_sum = 0
    
    for i in range(1, len(num_list) + 1):
        if i % 2 == 0:
            even_sum += num_list[i - 1]
        else:
            odd_sum += num_list[i - 1]
    
    answer = max(even_sum, odd_sum)
    
    return answer