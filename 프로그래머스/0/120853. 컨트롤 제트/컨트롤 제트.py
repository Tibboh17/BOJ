def solution(s):
    myStack = []
    arr = s.split()
    
    for i in arr:
        try:
            n = int(i)
            myStack.append(n)
        except:
            myStack.pop()
            
    answer = sum(myStack)
    return answer