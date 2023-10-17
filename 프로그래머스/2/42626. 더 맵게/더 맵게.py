from heapq import *

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    # print(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        scov1 = heappop(scoville)
        scov2 = heappop(scoville)
        new_scov = scov1 + scov2 * 2
        
        heappush(scoville, new_scov)
        
        answer += 1
        
    
    return answer