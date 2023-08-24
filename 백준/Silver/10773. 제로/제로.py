import sys
input = sys.stdin.readline

k = int(input())
lst = []
for i in range(k):
    n = int(input())
    if n == 0:
        lst = lst[:-1] # 마지막 슬라이싱
    else:
        lst.append(n) 
print(sum(lst))