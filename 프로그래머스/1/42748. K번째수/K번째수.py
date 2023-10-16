def solution(array, commands):
    answer = []
    for i in commands:
        slice = sorted(array[i[0]-1:i[1]])
        answer.append(slice[i[2]-1])
    return answer