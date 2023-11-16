from collections import *
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

visited = [False] * (n+1)
graph = [[] for i in range(n+1)]
cnt = 0
#print(graph)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start, visited):
    
    queue = deque([start])
    visited[start] = True

    while queue:

        v = queue.popleft()

        for adj in graph[v]:
            if visited[adj] == False:
                visited[adj] = True
                queue.append(adj)

    
for i in range(1, n+1):
    if visited[i] == False:
        bfs(graph, i, visited)
        cnt += 1
    
print(cnt)