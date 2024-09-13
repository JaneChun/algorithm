def solution(arr):
    # 최대공배수 = 두 수의 곱 / 최대공약수
    
    # 유클리드 호제법

    # 두 수 A와 B에서 A가 더 크다고 가정합니다.
    # A를 B로 나눈 나머지를 구합니다.
    # 나머지가 0이면 B가 최대공약수입니다.
    # 나머지가 0이 아니면, A를 B로, B를 나머지로 바꾸고 위 과정을 반복합니다.
    
    def getGCD(a, b):
        if a < b:
            a, b = b, a
        
        R = a % b
        if R == 0:
            return b
        else:
            return getGCD(b, R)
    
    def getLCM(a, b, GCD):
        return (a * b) // GCD
    
    acc_LCM = arr[0]
    for i in range(1, len(arr)):
        gcd = getGCD(acc_LCM, arr[i])
        acc_LCM = getLCM(acc_LCM, arr[i], gcd)
    
    return acc_LCM