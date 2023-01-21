from collections import Counter

def solution(array):
    if len(array)==1:
        return array[0]

    counter=Counter(array)
    counter2=counter.most_common() 
    if counter2[0][1]==counter2[1][1]:
        return -1
    return counter2[0][0]


def solution33(my_string, letter):
    answer = ''
    for index, item in enumerate(my_string):
        if(item == letter):
            answer = my_string[:index]
    print(answer)
    return answer

solution33('BCBdbe', 'B')   

'''
머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다.
 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 
양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요
'''
def solution(n, k):
    answer = 0
    event = n//10
    if(event >= 1):
        answer = n*12000 + int(k-event)*2000
    else:
        answer = n*12000 + k*2000
    return answer


def solution(n):
    answer = 0
    for i in range(n+1):
        if(i % 2 ==0):
            print(i)
            answer += i
    print(answer)

    return answer