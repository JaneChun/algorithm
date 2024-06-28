def getNumOfDivisor(num):
    count = 0
    for i in range(1, int(num ** 0.5) + 1): # 제곱근까지만 반복
        if num % i == 0:
            count += 1
            if i != num // i:  # i와 num // i가 같지 않으면 짝이 있는 약수이므로
                count += 1
    return count

def solution(number, limit, power):
    iron = 0
    for i in range(1, number + 1):
        numOfDivisor = getNumOfDivisor(i)
        if numOfDivisor > limit:
            iron += power
        else:
            iron += numOfDivisor
            
    return iron