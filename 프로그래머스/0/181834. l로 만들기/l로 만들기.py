def solution(myString):
    answer = ""
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
    
    for i in myString:
        if alphabet.index(i) < alphabet.index("l"):
            answer += "l"
        else:
            answer += i
            
    return answer