import sys
input = sys.stdin.readline

# 간선 정보 받기
# v = 노드 갯수, e = 간선 갯수
v, e = map(int, input().split())

# 부모 테이블 초기화 (자기 자신으로)
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

# Find 연산 : 특정 노드 x의 부모 노드 찾기
def find(parent, x):
    if parent[x] != x: # ex) 
        parent[x] = find(parent, parent[x]) 
    return parent[x]

# Union 연산 : 같은 부모로 만들어 주기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    # 더 작은 노드 번호의 부모값으로 만들어주기
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b

edges = [] # 간선 정보들 담을 리스트
mst_cost = 0 # 총 MST 비용

# 모든 간선 정보 
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # 비용순으로 오름차순 정렬하기 위해 튜플 첫 값을 cost로

# 모든 간선 비용 기준 오름차순 정렬 
edges.sort()

for i in edges:
    cost, a, b = i[0], i[1], i[2] # (비용, a, b) 순서 연결 했으므로
    
    # a, b 부모 다르다 = 사이클 발생 x --> Union 연결
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        mst_cost += cost

# MST 총 비용 출력
print(mst_cost)