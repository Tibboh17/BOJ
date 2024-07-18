def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)

def solution(m, n):
    gcd = GCD(m, n)
    lcm = (m * n) / gcd
    answer = [gcd, lcm]
    return answer