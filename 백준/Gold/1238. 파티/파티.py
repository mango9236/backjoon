import heapq
import sys
input = sys.stdin.readline

n,m,x = map(int, input().split()) # 노드, 간선, 끝지점 --> x에 갔다가 와야함
INF = (1e9)
graph = [[] for _ in range(n+1)]


for i in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))

# 1. 모든 노드에 대하여 -> x까지 최단거리
def dijkstra_end(start, end):
    q = []
    heapq.heappush(q, (0,start)) 
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if node == end:
            return distance[node]

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

distance_go = [INF] 
for i in range(1,n+1):
    distance = [INF] * (n+1)
    distance_go.append(dijkstra_end(i,x))
# print(distance_go)

# 2. x로부터 모든 노드까지 거리
def dijkstra(distance, start):
    q = []
    heapq.heappush(q, (0,start)) 
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

distance_come = [INF] * (n+1)
dijkstra(distance_come, x)
# print(distance_come)

# 거리합
res = []
for i in range(1,n+1): # 0번 무한대 빼고 1~n번까지 오고가고 합
    res.append(distance_come[i]+distance_go[i])

print(max(res))