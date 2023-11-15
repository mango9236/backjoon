from collections import *

# bfs로 풀어 나갈 것
# 2차원 배열일때는 좌표를 bfs 해야함 -> 원리는 동일하게 작용
# 고랭지 배추 1일때만 bfs 돌리면 됨
# visited 했으면 0으로 바꾸면됨.

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    queue = deque([(x,y)])
    maze[x][y] = 0

    while queue:

        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    queue.append((nx,ny))
                    maze[nx][ny] = 0 # 방문 처리 == 0으로 만들기


t = int(input())
for i in range(t):
    cnt = 0
    m,n,k = map(int, input().split())

    maze = [[0 for i in range(m)] for i in range(n)]

    # x 열, y 행 반대로 되어있음
    for j in range(k):
        x,y = map(int, input().split())
        maze[y][x] = 1
    
    for l in range(n):
        for k in range(m):
            if maze[l][k] == 1:
                bfs(l,k)
                cnt += 1
    
    print(cnt)