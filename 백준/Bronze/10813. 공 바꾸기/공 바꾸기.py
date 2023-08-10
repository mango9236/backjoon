a,b = map(int, input().split())

lst = list(range(1,a+1))

for i in range(b):
    c,d = map(int, input().split())
    lst[c-1], lst[d-1] = lst[d-1], lst[c-1]

for i in range(len(lst)):
    print(lst[i], end=" ")