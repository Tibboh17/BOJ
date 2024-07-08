def solution(num_list):
    add, mul = 0, 1
    length = len(num_list)
    if length >= 11:
        for i in num_list:
            add += i
        return add
    else:
        for i in num_list:
            mul *= i
        return mul