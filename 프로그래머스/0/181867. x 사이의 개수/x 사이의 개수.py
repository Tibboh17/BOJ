def solution(myString):
    myList = myString.split("x")
    answer = [len(i) for i in myList]
    return answer