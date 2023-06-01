# 저랑 비슷하게 짜셨고 저랑 동일한 문제를 겪으셨네요. 저의 경우 month가 12의 배수일 경우 해가 바뀌고 month가 0월이 되는 것이 문제였습니다.

# 이승학―2023.03.12 19:29
# 이승학
# today = "2021.12.08", terms = ["A 18"], privacies = ["2020.06.08 A"] 이렇게 넣어서 테스트해보세요.

# 이승학―2023.03.12 20:14

def solution(today, terms, privacies):
    today = int(today.replace(".","")) # 오늘 년,월,일
    dic = {}
    
    for i in terms: # 달은 1~100달
        a,b = map(str, i.split())
        dic[a] = int(b)
    
    result = []
    for i,v in enumerate(privacies):
        # 약관 시작일, 약관형태
        date, alphabet = map(str, v.split(" "))
        
        # 약관 시작일 -> 년,월,일 
        date_y, date_m, date_d = map(int, date.split("."))
        
        # 약관 시작 월 + 약관 기간 월 = 변환해야할 월 수
        all_month = date_m + dic[alphabet]
        
        y = 0
        m = 0
        
        if all_month % 12 == 0:
            y = all_month // 12 - 1
            m = all_month - (y*12)
        
        else:
            y = all_month // 12
            m = all_month % 12
        
        date_y += y
        date_m = m
        print(date_y, date_m)
        
        date_end = 10000*date_y + 100*date_m + date_d
        if today >= date_end:
            result.append(i+1)
        
    return result