import sys 
input = sys.stdin.readline

left = list(input().rstrip())
length = len(left)
right = []

n = int(input())
for i in range(n):
    command = input().rstrip().split()
    if command[0] == "L":
        if len(left) == 0:
            continue
        right.append(left.pop())

    if command[0] == "D":
        if len(right) == 0:
            continue
        left.append(right.pop())

    if command[0] == "B":
        if len(left) == 0:
            continue
        left.pop()

    if command[0] == "P":
        left.append(command[1])

for i in left:
    print(i, end="")

for i in range(len(right)):
    print(right.pop(), end="")    