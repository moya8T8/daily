from collections import Counter

def solution(array):
    if len(array)==1:
        return array[0]

    counter=Counter(array)
    counter2=counter.most_common() 
    if counter2[0][1]==counter2[1][1]:
        return -1
    return counter2[0][0]


#정말..풀다가 미쳐버리는줄..