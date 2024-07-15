def solution(my_string):
    answer = []
    for i in range(1, len(my_string) + 1):
        my_list = list(my_string[-1:-(i + 1):-1])[-1::-1]
        string = "".join(my_list)
        answer.append(string)
    answer.sort()
    return answer