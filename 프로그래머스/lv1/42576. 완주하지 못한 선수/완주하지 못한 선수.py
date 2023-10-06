def solution(participant, completion):
    dic = {}
    answer = ""
    # 참가 시 1 증가
    for i in participant:
        # 이미 있을 경우 cnt++
        if i in dic:
            dic[i] += 1
        else:    
            dic[i] = 1

    # 완주 시 다시 감소
    for i in completion:
        dic[i] -= 1
        
    for i in dic:
        if dic[i] == 1:
            return i

        
'''답안 2'''
'''정렬을 활용, 효율성은 좀 떨어짐'''
#     participant = sorted(participant)
#     completion = sorted(completion)
#     completion.append("")
    
#     for i,v in enumerate(participant):
#         if v != completion[i]:
#             return v
