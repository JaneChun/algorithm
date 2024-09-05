def solution(s):
    step = 0
    count = 0
    
    while s != '1':
        zero_removed_s = ''.join([digit for digit in s if digit != '0'])
        count += len(s) - len(zero_removed_s)
        
        binary = bin(len(zero_removed_s))[2:]
        s = str(binary)
        step += 1
    
    return [step, count]