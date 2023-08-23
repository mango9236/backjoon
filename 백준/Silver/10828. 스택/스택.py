import sys

input = sys.stdin.readline

# Python list = stack 
lst = []

n = int(input())
for i in range(n):

    # input을 나눠서 저장
    word = input().rstrip().split() 
    
    # 명령어
    command = word[0]

    # push
    if command == 'push':
        lst.append(word[1])

    # pop
    elif command == 'pop':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

    # size
    elif command == 'size':
        print(len(lst))
    
    # empty
    if command == 'empty':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    # top
    if command == 'top':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
