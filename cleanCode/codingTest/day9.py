
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

#개미군단  1차시도 
def solution(hp):
    jangun = 5
    beong = 3
    yil = 1

    sanyagam = hp
    answer = 0
    if(sanyagam % jangun > 0):
        abc = sanyagam // jangun
        answer += abc
        sanyagam = sanyagam - (abc * jangun)
        if(sanyagam % beong > 0):
            ef = sanyagam // beong
            answer += ef
            sanyagam = sanyagam -(ef * beong)
            if(sanyagam != 0):
                answer += sanyagam
        else :
            ef = sanyagam // beong
            answer += ef
    else :
        abc = sanyagam // jangun
        answer += abc
    print(answer)

    return answer


#2차시도 
def solution(hp):
    answer = 0
    answer += hp//5
    hp %= 5
    answer += hp//3
    hp %= 3
    answer += hp//1

    return answer