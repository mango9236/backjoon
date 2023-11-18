from collections import *
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
graph = []

# 폭탄 쓴 경로, 안쓴 경로 + 2차원배열 = 3차월 배열
# 이것이 이 문제 푸는 데 핵심 포인트
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    lst = list(map(int, str(input().rstrip())))
    graph.append(lst)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,bomb):

    queue = deque([(x,y,bomb)])    

    while queue:
        v = queue.popleft()
        x,y,bomb = v[0],v[1],v[2]

        # 도착했을 경우
        if x == n-1 and y == m-1:
            return visited[x][y][bomb]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
                
            # 벽 있고 폭탄 남아있으면
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and bomb == 0:
                queue.append((nx,ny,1))
                visited[nx][ny][1] = visited[x][y][0] + 1
            
            # 벽 아니고, 아직 방문 안했으면 
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visited[nx][ny][bomb] == 0:
                queue.append((nx,ny,bomb))
                visited[nx][ny][bomb] = visited[x][y][bomb] + 1

    # 도달하지 못했을 경우
    return -1 

print(bfs(0,0,0))
