def solution(num_list):
    cnt_list = []
    
    for i in num_list:
        cnt = 0
        while True:
            if i == 1:
                cnt_list.append(cnt)
                break
            else:
                if i % 2 == 0:
                    i /= 2
                else:
                    i = (i - 1) / 2
            cnt += 1
    
    answer = sum(cnt_list)
    return answer