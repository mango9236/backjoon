import sys
input = sys.stdin.readline
left = list(input().strip('\n'))
right = []
n = int(input())

for i in range(n):
    command=input().split()

    if command[0]=="L":
        if len(left) !=0:
            right.append(left.pop())

    if command[0] == "D":
        if len(right)!=0:
            left.append(right.pop())

    if command[0]=="B":
        if len(left) != 0:
            left.pop()

    if command[0]=="P":
        left.append(command[1])


left.extend(reversed(right))


print(''.join(map(str,left)))