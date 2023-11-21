from collections import *
import sys

input = sys.stdin.readline

# 총 층수, 현재 위치, 목적지 위치, 올라갈때, 내려갈때
f, s, g, u, d = map(int, input().split())
graph = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [False] * (f+1)
def bfs(f,s,g,u,d):
    cnt = 0

    if s == g:
        return cnt
        
    queue = deque([(s,cnt)])
    visited[s] = True


    while queue:
        v,cnt = queue.popleft()
        
        if v == g:
            return cnt

        up_v = v+u
        up_d = v-d

        if 1 <= up_v <= f:
            if visited[up_v] == False:
                queue.append((up_v,cnt+1))
                visited[up_v] = True

        if 1 <= up_d <= f:
            if visited[up_d] == False:
                queue.append((up_d,cnt+1))
                visited[up_d] = True

    return "use the stairs"


res = bfs(f,s,g,u,d)
print(res)