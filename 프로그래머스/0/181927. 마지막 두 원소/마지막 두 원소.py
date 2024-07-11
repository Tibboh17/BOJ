def solution(num_list):
    answer = num_list
    m, n = answer[-1], answer[-2]
    
    if m > n:
        answer.append(m - n)
    else:
        answer.append(2 * m)
        
    return answer