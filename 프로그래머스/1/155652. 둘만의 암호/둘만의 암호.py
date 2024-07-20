def solution(s, skip, index):
    answer = ''    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alphabet= alphabet.replace(sk, '')

    for i in range(len(s)):
        originalIndex = alphabet.index(s[i])
        newIndex = (originalIndex + index) % len(alphabet)
        answer += alphabet[newIndex]
        
    return answer