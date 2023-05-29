import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) 
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    a,b,c= map(int, input().split())
    graph[a].append((b,c)) 
    graph[b].append((a,c))

def dijkstra(start):
    queue = [] 
    heapq.heappush(queue, (0,start)) 
    distance[start] = 0 

    while queue:
        dist, node = heapq.heappop(queue) 
        
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1] 

            if cost < distance[next[0]]: 
                distance[next[0]] = cost 
                heapq.heappush(queue, (cost, next[0])) 

s,t = map(int, input().split())
dijkstra(s)
print(distance[t])