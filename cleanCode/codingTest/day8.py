def solution(n):
    answer = []
    for i in range(n+1):
        if(i%2 != 0):
            answer.append(i)
    return answer


def solution(numbers, num1, num2):
    return numbers[num1:num2+1]

def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1):
        answer.append(numbers[i])   
    print(answer)
    return answer