from collections import *
import sys

input = sys.stdin.readline

n = int(input())
graph = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    lst = list(map(int, input().split()))
    graph.append(lst)

# 최대 높이
max_h = max(map(max, graph))

def bfs(x, y, depth, visited):
    
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        v = queue.popleft()
        x,y = v[0],v[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0<= ny < n and graph[nx][ny] > depth and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny] = True


# 최대 안전 영역 갯수 
res = 0

# 높이 0 ~ 최대 높이 -1 까지 
# 최대 높이는 어차피 물 다 잠기므로
for i in range(0,max_h):
    visited = [[False] * (n) for _ in range(n)]

    # bfs 몇 번 돌았는지
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, i, visited)
                cnt += 1

    if res < cnt:
        res = cnt

print(res)
