def solution(n, m, section):
    start = section[0] # 페인트칠 시작점
    cnt = 1 # 처음도 칠한거니까 1로 시작
    
    # 안칠한 섹션 돌기
    for element in section:
        end = start+m-1 # 한번으로 start~end까지 색칠가능
        # 원소가 end안에 있으면 (한번에 칠해지는거니까 패스)
        if element <= end:
            continue
        # 원소가 end밖에 있으므로 새로운 색칠, 색칠 시작점을 그 원소로 바꾸기 
        else: 
            cnt+=1
            start = element
    
    return cnt
        