from collections import *
import sys

input = sys.stdin.readline

n,m,r = map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

# res에 순서 담기 
res = [0] * (n+1)

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 정렬
for i in range(n+1):
    graph[i] = sorted(graph[i])

def bfs(graph, start):

    queue = deque([start])
    visited[start] = True
    cnt = 1
    res[start] = cnt

    while queue:

        v = queue.popleft()

        for adj in graph[v]:
            if visited[adj] == False:
                cnt += 1
                queue.append(adj)
                visited[adj] = True
                res[adj] = cnt 

    return

# 오름차순으로 bfs
bfs(graph, r)

# 결과출력
for i in range(1, len(res)):
    print(res[i])