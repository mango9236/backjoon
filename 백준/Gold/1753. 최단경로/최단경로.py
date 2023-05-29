import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 매우 큰 수 = 10억을 둠, 간선 30만개인데 가중치 10이하니까 300만이 최대 

v,e = map(int, input().split())
start = int(input()) # 시작노드

graph = [[] for _ in range(v+1)] # 그래프
# visited = [False] * (v+1) --> 우선순위큐가 비워지면 끝난거니까 방문기록이 필요없어짐
distance = [INF] * (v+1) # 거리 테이블 생성

for i in range(e):
    u,v,w = map(int, input().split())
    graph[u].append((v,w)) # 그래프는 u-->v , w(가중치)로 이루어져있음.

def dijkstra(start):
    queue = [] 
    heapq.heappush(queue, (0,start)) # 최소힙 -> (거리, 노드번호) 대입 -> 거리가 작은순으로 우선순위 
    distance[start] = 0 # 시작노드의 거리는 0으로 시작 

    while queue:
        dist, node = heapq.heappop(queue) # 거리 작은 우선순위 높은 것 pop
        
        # 큐에서 뽑아낸 거리 < 갱신(기록)된 거리 일경우 이미 최단거리(방문되었다고 치자)이므로 건너뜀.
        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1] # 시작 --> node --> next 거리 = cost

            # 만약 기록되어있던 다음 노드의 거리보다 계산된 cost가 짧으면 --> 갱신! 
            if cost < distance[next[0]]: 
                distance[next[0]] = cost # 갱신!!
                heapq.heappush(queue, (cost, next[0])) # (cost(갱신된 거리), 다음노드의 번호)

dijkstra(start)

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
