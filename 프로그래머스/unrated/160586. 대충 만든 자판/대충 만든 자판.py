from collections import defaultdict

def solution(keymap, targets):
    key_dic = {}
    for key in keymap:
         for i in range(65, 91):
                check = chr(i)
                num = key.find(check)
                # -1(문자가 없음) -> 넘어감
                if num == -1:
                    continue
                # check 값이 딕셔너리에 없거나 새로운 값이 더 작은경우 -> 갱신
                if check not in key_dic or key_dic[check] > num:
                    key_dic[check] = num+1
    
    result = []

    for word in targets:
        cnt = 0
        check = True # 키 값이 없는지 체크
        
        for i in word:
            # 만약 key가 없을 경우
            if i not in key_dic:
                check = False
                result.append(-1)
                break
            cnt += key_dic[i]
        
        if check == True:
            result.append(cnt)
        
    return result