from collections import *
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

tomato = []
visited = [[False] * n for _ in range(m)]

# deque에 모든 시작 지점을 넣고 bfs 돌리면 됨.
queue = deque([])

for i in range(m):
    lst = list(map(int, input().rstrip().split(" ")))
    tomato.append(lst)
    for j in range(n):
        if lst[j] == 1:
            queue.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs():
    
    while queue:
        v = queue.popleft()
        x,y = v[0],v[1]
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < m and 0<= ny < n and tomato[nx][ny] == 0 and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True
                tomato[nx][ny] = tomato[x][y] + 1

# bfs 사용
bfs()

# 2차원 배열에서 최대값 - 1 = 최대 걸린 날짜
# 0이 한개라도 남아있으면 -1 출력
check = True

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            check = False
            break

if check == False:
    print(-1)
else:
    print(max(map(max, tomato))-1)