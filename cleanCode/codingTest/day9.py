
#약수
def solution(n):
    answer = 0
    divisorsList = []

    for i in range(1, n + 1):
        if (n % i == 0) :
            divisorsList.append(i)
        
    for i in divisorsList:
        answer += i
    return answer
