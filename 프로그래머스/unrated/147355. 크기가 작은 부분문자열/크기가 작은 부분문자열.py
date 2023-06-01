def solution(t, p):
    p_num = int(p) # 숫자 p
    cnt = 0 
    # 계속 옆으로 슬라이싱
    for i in range(len(t)-len(p)+1):
        sub = int(t[i:i+len(p)])
        if p_num >= sub:
            cnt += 1
        
    return cnt
        