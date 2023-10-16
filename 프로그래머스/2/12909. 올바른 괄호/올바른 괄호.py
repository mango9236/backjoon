def solution(s):
    answer = True
    
    lst = []
    
    for i in s:
        if i == "(":
            lst.append("(")
        else:
            if len(lst) == 0:
                return False
            if lst[-1] == "(":
                lst.pop()
    
    if len(lst) == 0:
        return True
    else:
        return False 