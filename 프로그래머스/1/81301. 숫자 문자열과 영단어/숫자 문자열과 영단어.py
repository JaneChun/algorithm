import re

def solution(s):
    numArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(numArr)):
        num = numArr[i]
        pattern = rf"{num}"
        match = re.findall(pattern, s)
        
        if match:
            replacedS = re.sub(pattern, str(i), s)
            s = replacedS
            
    return int(s)
            