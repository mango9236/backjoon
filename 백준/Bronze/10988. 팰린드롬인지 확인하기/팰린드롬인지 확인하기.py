word = input()
cnt = 1
for i in range(len(word) // 2):
    if word[i] != word[-1-i]:
        cnt = 0
        break 

print(cnt)