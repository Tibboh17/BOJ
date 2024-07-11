def solution(s):
    s = s.lower()
    if "p" in s or "y" in s:
        p_count = s.count("p")
        y_count = s.count("y")
        if p_count == y_count:
            answer = True
        else:
            answer = False 
    else:
        answer = True
               
    return answer