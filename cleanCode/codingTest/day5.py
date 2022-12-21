def solution(array):
    answer = 0
    array.sort()
    test = len(array)/2
    test = int(test)
    
    answer = array[test]

    return answer

    #중간값 구하기 