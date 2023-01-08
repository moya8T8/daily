def solution(money):
    answer = []
    coffee = 5500

    count = money // coffee
    answer.append(count)

    change = money - coffee * count
    answer.append(change)
    print(answer)
    return answer