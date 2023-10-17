from collections import *

def solution(maps):
    
    # 행 n 열 m
    n = len(maps)
    m = len(maps[0]) 
    
    # 방문 체크
    visited = [[False] * m for _ in range(n)]
    
    # 시작지점 0,0, 시작 방문 체크
    queue = deque([(0,0)])
    visited[0][0] = True
    
    # 동서남북
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    
    # 큐가 비었을 때까지 BFS 
    while queue:
        # 가장 가까운 노드 꺼내기
        y,x = queue.popleft()
        # 4방향으로 테스트
        for i in range(4):
            # 다음자리 체크하기 위해 nx, ny
            nx = x+dx[i]
            ny = y+dy[i]
            # 만약 다음자리가 갈 수 있는 곳이고 방문 안했으면
            if 0 <= nx <= m-1 and 0 <= ny <= n-1 and maps[ny][nx] == 1:
                if visited[ny][nx] == False:
                    # 방문했음으로 바꾸고 다음 좌표를 Queue에 넣기
                    # 거리는 1 증가 기록
                    visited[ny][nx] = True
                    queue.append((ny,nx))
                    maps[ny][nx] = maps[y][x] + 1
    
    # 마지막이 도착 못했을 경우 == 그대로 1일 경우
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
                
    