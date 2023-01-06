import math
def solution(n):
    answer = 0
    answer = math.ceil(n / 7)
    
    return answer


def lcm(a, b):
    return a * b / math.gcd(a, b)

def solution2(n):
    ch = lcm(n,6)
    answer = int(ch / 6)
    return answer

