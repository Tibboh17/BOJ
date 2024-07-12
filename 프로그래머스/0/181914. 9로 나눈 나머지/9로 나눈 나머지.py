def solution(number):
    str_number = str(number)
    list_number = [int(i) for i in str_number]
    answer = sum(list_number) % 9
    return answer