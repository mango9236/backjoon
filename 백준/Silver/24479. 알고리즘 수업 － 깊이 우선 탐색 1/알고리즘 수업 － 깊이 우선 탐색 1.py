import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
res = [0] * (n+1)
cnt = 1

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i] = sorted(graph[i])

def dfs (graph, start, visited):
    # 전역변수 cnt  
    global cnt 

    visited[start] = True
    res[start] = cnt
    cnt += 1

    for adj in graph[start]:
        if visited[adj] == False:
            dfs(graph, adj, visited)
    
    return 

dfs(graph, r, visited)

for i in range(1, len(res)):
    print(res[i])