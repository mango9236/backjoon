def solution(players, callings):
    dic_name = {}
    for i,v in enumerate(players):
        dic_name[v]=i
        
    for call in callings:
        post = dic_name[call] # 후발 번호
        pre = post - 1 # 선발 번호
        
        dic_name[players[post]] = pre 
        dic_name[players[pre]] = post
        
        players[post] , players[pre] = players[pre], players[post]
        
        

    return players

