# 8/24

# 괄호문제: 완벽한 대칭괄호쌍을 만들기
# VPS: Valid Parenthesis String을 만들기
line = input()

while line[0] != ".":
    stack = []
    for letter in line:
        
        if letter == '(' or letter == '[':
            stack.append(letter)
        
        elif letter == "]":
            if len(stack) == 0:
                stack.append(letter)
                break
            
            elif stack[-1] == "[":
                stack.pop()
            
            else:
                stack.append(letter)
                break
        
        elif letter == ")":
            if len(stack) == 0:
                stack.append(letter)
                break
            
            elif stack[-1] == "(":
                stack.pop()
            
            else:
                stack.append(letter)
                break
    
    if len(stack) == 0:
        print("yes")
    
    else:
        print("no")

    line = input()
