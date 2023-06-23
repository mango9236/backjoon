import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 매우 큰 수
graph = [[] for _ in range(100001)] # 그래프: n,k 모두 10만을 넘지 못함
distance = [INF] * (100001) # 거리 테이블 생성

for i in range(100001):
    # 값의 범위는 0<= n,k <= 10만 이어야함.
    if i*2 <= 100000: 
        graph[i].append((i*2,1))
    if (i+1) <= 100000:
        graph[i].append((i+1,1))
    if (i-1) >= 0:
        graph[i].append((i-1,1))

start, end = map(int, input().split()) # 시작 끝

def dijkstra(start):
    q = [] 
    heapq.heappush(q, (0,start)) 
    distance[start] = 0 

    while q:
        dist, node = heapq.heappop(q) 
        if node == end: 
            print(distance[node])
            break

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1]

            if cost < distance[next[0]]: 
                distance[next[0]] = cost 
                heapq.heappush(q, (cost, next[0])) 

dijkstra(start)