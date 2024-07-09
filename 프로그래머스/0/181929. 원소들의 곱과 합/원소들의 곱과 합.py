def solution(num_list):
    list_sum = sum(num_list) ** 2
    list_mul = 1
    
    for num in num_list:
        list_mul *= num
        
    if list_sum > list_mul:
        answer = 1
    else:
        answer = 0
        
    return answer