H, M = map(int, input().split())
make_M = int(input()) # 만드는 시간
make_H = make_M // 60 # 60(분)으로 나눈 몫 = 시간
make_M = make_M % 60 # 나머지는 = 분

H += make_H 
M += make_M

# 분이 60이상이면
if M > 59:
    M -= 60
    H += 1

# 시간이 24이상이면
if H > 23:
    H -= 24


print("{} {}".format(H,M))