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

def solution(slice, n):
    answer = 0
    if(n % slice == 0):
        answer = n // slice
    else:
        answer = n//slice + 1
    print(answer)
    return answer

solution(7,10);
