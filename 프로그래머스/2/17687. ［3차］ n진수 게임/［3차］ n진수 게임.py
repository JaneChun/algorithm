def solution(n, t, m, p):
    answer = ''

    whole_string = ''
    for i in range(m * t):
        whole_string += to_base(i, n)
    
    for i in range(len(whole_string)):
        if (i % m) + 1 == p: # 튜브 차례
            answer += whole_string[i]

        if len(answer) == t:
            return answer
    
    

def to_base(number, n):
    if number == 0:
        return "0"
    
    digits = []
    while number:
        rest = number % n
        
        if rest >= 10:
            digits.append(chr(ord('A') + rest - 10)) # 10 -> A
        else:
            digits.append(str(rest))
        
        number //= n
    return ''.join(digits[::-1])