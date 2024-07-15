def solution(my_string, is_suffix):
    suffix = []
    for i in range(1, len(my_string) + 1):
        my_list = list(my_string[-1:-(i + 1):-1])[-1::-1]
        string = "".join(my_list)
        suffix.append(string)
    if is_suffix in suffix:
        answer = 1
    else:
        answer = 0
    return answer