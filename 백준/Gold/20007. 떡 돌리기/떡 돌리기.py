import heapq
import sys

input = sys.stdin.readline
n,m,x,y = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n)] # 0번 부터
distance =[INF]*n

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
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

dijkstra(y)
for i,v in enumerate(distance): 
    distance[i] = 2*v

distance = sorted(distance)
cnt = 0
day = 1
check = True 

for i in distance:
    
    if i > x:
        print(-1)
        check = False
        break
    cnt += i
    if cnt > x:
        day += 1
        cnt = i

if check == True:
    print(day)
    