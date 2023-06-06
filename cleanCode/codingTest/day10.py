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

def firss():
    print('화면이 생각보다 잘 보이는구나 괜찮을지도 모르겠다 이정도 거리에서 설치해서 쓰는거 말야 ㅇㅅㅇ...응! ')
