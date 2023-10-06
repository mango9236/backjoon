def solution(participant, completion):
    dic = {}
    answer = ""
    for i in participant:
        # 이미 있을 경우 cnt++
        if i in dic:
            dic[i] += 1
        else:    
            dic[i] = 1
    
    for i in completion:
        dic[i] -= 1
        
    for i in dic:
        if dic[i] == 1:
            return i
