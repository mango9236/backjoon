n = int(input())
cnt = 0
for i in range(n):
    check = True
    word = input()
    for j in range(len(word)-2):
        if word[j] != word[j+1] and word[j] in word[j+2:]:
            check = False
            break
    if check == True:
        cnt += 1
print(cnt)