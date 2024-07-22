def solution(arr):
    i = 0
    numlist = arr
    
    while True:
        temp = numlist.copy()
        for j in range(len(numlist)):
            if (numlist[j] % 2 == 0) and (numlist[j] >= 50):
                numlist[j] /= 2
            elif (numlist[j] % 2 != 0) and (numlist[j]) < 50:
                numlist[j] = numlist[j] * 2 + 1
        if temp == numlist:
            answer = i
            break
        i += 1
        
    return answer