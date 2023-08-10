a,b = map(int, input().split())
lst = [0]*(a+1)
for i in range(b):
    s,e,n = map(int, input().split())
    for j in range(s, e+1):
        lst[j] = n

for i in range(1,len(lst)):
    print(lst[i], end=" ")