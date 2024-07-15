def solution(a, b, c, d):
    num_list = [a, b, c, d]
    num_set = set(num_list)
    
    max_num = max(num_list, key=num_list.count)
    min_num = min(num_list, key=num_list.count)
    
    max_cnt = num_list.count(max_num)
    min_cnt = num_list.count(min_num)
    
    if max_cnt == 4:
        answer = 1111 * max_num
    elif max_cnt == 3:
        answer = (10 * max_num + min_num) ** 2
    elif max_cnt == 2:
        if min_cnt == 2:
            num_set -= {max_num}
            temp = list(num_set)[0]
            answer = (max_num + temp) * abs(max_num - temp)
        else:
            num_set -= {max_num, min_num}
            temp = list(num_set)[0]
            answer = min_num * temp
    else:
        answer = min(num_list)
        
    return answer