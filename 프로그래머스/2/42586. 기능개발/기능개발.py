from collections import *

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        cnt = 0
        
        for i,v in enumerate(progresses):
            progresses[i] += speeds[i]
            
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        
        if cnt != 0:
            answer.append(cnt)
        print(progresses)
    
    return answer