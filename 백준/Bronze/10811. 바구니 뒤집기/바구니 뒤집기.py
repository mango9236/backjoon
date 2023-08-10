a,b = map(int, input().split())

lst = list(range(1,a+1))

for i in range(b):
    c,d =  map(int, input().split())
    front = lst[0:c-1]
    slice = list(reversed(lst[c-1:d])) 
    back = lst[d:]
    lst = front + slice + back

for i in range(len(lst)):
    print(lst[i], end=" ")