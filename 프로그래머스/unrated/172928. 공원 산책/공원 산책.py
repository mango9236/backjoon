def solution(park, routes):
    graph = [] 
    # 그래프로 변환
    for i, line in enumerate(park):
        height = len(park)-1
        sub = []
        for j, cell in enumerate(line): # 출발 0 가능 1 불가능 2
            width = len(line)-1
            if cell == "S":
                sub.append(0)
                s_row = i # 출발 행
                s_col = j # 출발 열
                
                
            if cell == "O":
                sub.append(1)
                
            if cell == "X":
                sub.append(2)
        
        graph.append(sub)
    # 동서남북 정의
    dir = {"E": [0,1], "W": [0,-1] ,"S": [1,0], "N":[-1,0]} # [행, 열] 정의
    
    # 시작점 복사 
    start_row = s_row
    start_col = s_col
    
    # 명령
    for command in routes:
        op = command[0]
        n = int(command[2]) # 1~9이므로 두자리 이상될 일 없음
        
        # 명령어 행, 열 변화값 정의
        d_row = dir[op][0] 
        d_col = dir[op][1]
        
        # 계속 가면서 체크
        for _ in range(n):
            # 안 벗어나고 장애물을 안만나면
            if 0<=(s_row+d_row)<=height and 0<=(s_col+d_col)<=width and graph[s_row+d_row][s_col+d_col] != 2:
                s_row += d_row
                s_col += d_col
                
            else:
                s_row = start_row
                s_col = start_col
                break
        
        # for문을 다 돌았다는건 명령 수행 가능 -> 시작점 저장 
        start_row = s_row
        start_col = s_col
        
        result=[s_row,s_col]

    return result