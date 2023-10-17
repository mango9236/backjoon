from collections import *

def solution(clothes):
    answer = 1
    
    dic = defaultdict(int)
    
    for i in clothes:
        print(i)
        if i[1] not in dic:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    
    value = list(dic.values())
    
    for i in value:
        answer *= (i+1)
    
    
    return answer - 1 