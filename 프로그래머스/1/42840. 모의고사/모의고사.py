def solution(answers):
    answer = []
    
    lst1 = [1,2,3,4,5]
    lst2 = [2,1,2,3,2,4,2,5]
    lst3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 1,2,3번 맞은 갯수 
    chk = [0,0,0]
    
    for i in range(len(answers)):
        
        if answers[i] == lst1[i % 5]:
            chk[0] += 1
            
        if answers[i] == lst2[i % 8]:
            chk[1] += 1
            
        if answers[i] == lst3[i % 10]:
            chk[2] += 1
    
    max_num = max(chk)
    
    for i in range(len(chk)):
        if max_num == chk[i]:
            answer.append(i+1)
        
    
    return answer