def solution(my_string, n):
    str_list = list(my_string)[-1:-(n + 1):-1]
    str_list.reverse()
    answer = "".join(str_list)
    return answer