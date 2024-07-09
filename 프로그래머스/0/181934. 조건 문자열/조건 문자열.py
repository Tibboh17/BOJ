def solution(ineq, eq, n, m):
    if eq == "=":
        expression = f"{n}{ineq}{eq}{m}"
    else:
        expression = f"{n}{ineq}{m}"
        
    if eval(expression):
        answer = 1
    else:
        answer = 0
    return answer