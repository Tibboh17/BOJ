def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for i in s:
        if not i.isdigit():
            return False
    return True