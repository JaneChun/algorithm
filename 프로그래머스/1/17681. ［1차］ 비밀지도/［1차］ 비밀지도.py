def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        a1 = bin(int(arr1[i]))[2:].zfill(n) # 2진수 변경 -> 접두사 자름 -> n자리 맞춤
        a2 = bin(int(arr2[i]))[2:].zfill(n)
        
        line = ''
        for j in range(len(a1)):
            if int(a1[j]) + int(a2[j]) == 0:
                line += ' '
            else:
                line += '#'
        answer.append(line)
    return answer