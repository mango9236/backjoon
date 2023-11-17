from collections import *
import sys
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]

for i in range(n):
    lst = list(map(int, str(input().rstrip())))
    graph.append(lst)

# print(graph)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    cnt = 0

    queue = deque([(x,y)])
    visited[x][y] = True
    cnt += 1

    while queue:
        v = queue.popleft()
        x,y = v[0],v[1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx < n and 0<= ny < n and graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx,ny))
    
    return cnt


# bfs 결과 담기, res의 길이가 총 단지 갯수
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            res.append(bfs(i,j))

print(len(res))

res = sorted(res)
for i in res:
    print(i)