def solution(s, n):
    answer = ''
    for char in s:
        if char == ' ':
            answer += ' '
        else:
            ascii = ord(char) # ord: 문자 -> ASCII 변환
            ascii += n
            
            if (char.islower() and ascii > 122) or (char.isupper() and ascii > 90): # z = 122, Z = 90
                ascii -= 26
                
            char = chr(ascii) # chr: ASCII -> 문자 변환
            answer += char
    return answer