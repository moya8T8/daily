def solution1(my_string):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[-1-i]
    return answer

n = int(input())
for i in range(n):
    print('*' * (i+1)  )

def solution2(num_list):
    answer = []
    a = 0
    b = 0
    for num in num_list:
        if(num % 2 == 0):
            a +=1
        else :
            b +=1
    answer = [a,b]
    return answer
