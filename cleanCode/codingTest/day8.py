def solution(n):
    answer = []
    for i in range(n+1):
        if(i%2 != 0):
            answer.append(i)
    return answer

#조건에 맞는 범위 자르기 
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])   
    print(answer)
    return answer

def solution(age):
    answer = ''
    age = str(age)
    for i in range(len(age)):
        if(age[i]=='0'):
            answer += 'a'
        if(age[i]=='1'):
            answer += 'b'
        if(age[i]=='2'):
            answer += 'c'
        if(age[i]=='3'):
            answer += 'd'
        if(age[i]=='4'):
            answer += 'e'
        if(age[i]=='5'):
            answer += 'f'
        if(age[i]=='6'):
            answer += 'g'
        if(age[i]=='7'):
            answer += 'h'
        if(age[i]=='8'):
            answer += 'i'
        if(age[i]=='9'):
            answer += 'k'
    print(answer)
    return answer
