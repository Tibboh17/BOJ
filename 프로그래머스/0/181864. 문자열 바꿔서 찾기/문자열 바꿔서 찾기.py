def solution(myString, pat):
    alteredString = ""
    for i in myString:
        if i == "A":
            alteredString += "B"
        else:
            alteredString += "A"
            
    if pat in alteredString:
        answer = 1
    else:
        answer = 0
        
    return answer