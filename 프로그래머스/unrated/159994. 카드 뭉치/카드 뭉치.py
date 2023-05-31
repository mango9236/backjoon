from collections import deque
def solution(cards1, cards2, goal):
    q1 = deque(cards1)
    q2 = deque(cards2)
    g = deque(goal)
    check = True
    
    for i,v in enumerate(goal):
        word = g.popleft() 
        
        # 다 뽑았는데 비교를 하려하니까 index 에러 -> 길이 0 아니어야함
        if len(q1) != 0 and word == q1[0]:
            q1.popleft()
            continue
            
        if len(q2) != 0 and word == q2[0]: 
            q2.popleft()
            continue
            
        check = False
        break
    
    if check == True:
        result = "Yes"
    else:        
        result = "No"
        
    return result