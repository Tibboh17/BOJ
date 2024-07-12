def solution(x):
    list_x = [int(i) for i in str(x)]
    if x % sum(list_x) == 0:
        answer = True
    else:
        answer = False
    return answer