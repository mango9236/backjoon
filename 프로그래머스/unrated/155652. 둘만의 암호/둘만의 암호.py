def solution(s, skip, index):
    skip = list(skip)
    alphabet = [] 
    
    # 97~122 (a~z)
    for i in range(97,123):
        alphabet.append(chr(i))
    
    # skip단어 제거
    for skip_word in skip:
        alphabet.remove(skip_word)
    
    result = ""
    for letter in s:
        idx = alphabet.index(letter)
        new_idx = idx + index
        
        if new_idx > len(alphabet)-1: # 0~len-1까지 문자가있으므로
            new_idx %= len(alphabet) # index가 큰 값일 수도 있으므로 -= 말고 %=
            
        result += alphabet[new_idx]
        
    return result
