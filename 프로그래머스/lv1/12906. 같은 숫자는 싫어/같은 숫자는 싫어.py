from collections import deque

def solution(arr):
    cur = -1
    answer = []
    
    for i in arr:
        if i == cur:
            continue
        cur = i
        answer.append(cur)
        
        
    return answer