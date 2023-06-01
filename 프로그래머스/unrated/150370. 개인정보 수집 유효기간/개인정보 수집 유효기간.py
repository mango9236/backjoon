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
        
        # 더해지는 년 y, 남은 월 m
        y = 0
        m = 0
        
        # 만약 12달의 배수인경우 (12로 나누면 0월이되므로)
        if all_month % 12 == 0:
            y = all_month // 12 - 1
            m = all_month - (y*12)
        
        else:
            y = all_month // 12
            m = all_month % 12
        
        # 넘어가는 년은 더해주고 월은 m
        date_y += y
        date_m = m
        
        # 20181011 이렇게 8자리로 비교
        date_end = 10000*date_y + 100*date_m + date_d
        
        # 동일하거나 크면 append
        if today >= date_end:
            result.append(i+1)
        
    return result
