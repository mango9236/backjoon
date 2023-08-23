# 시간제한 0.5초 --> input 1만개 = sys.stdin.readline() 사용
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

    # 1
    if command == '1':
        lst.append(word[1])

    # 2
    elif command == '2':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())

    # 3
    elif command == '3':
        print(len(lst))
    
    # empty
    if command == '4':
        if len(lst) == 0:
            print(1)
        else:
            print(0)

    # 5
    if command == '5':
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
