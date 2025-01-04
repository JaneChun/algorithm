def solution(arrayA, arrayB):
    # 최대공약수 계산
    gcd_A = arrayA[0]
    for i in range(1, len(arrayA)):
        gcd_A = getGCD(gcd_A, arrayA[i])

    gcd_B = arrayB[0]
    for i in range(1, len(arrayB)):
        gcd_B = getGCD(gcd_B, arrayB[i])
    
    # 상대 배열의 모든 요소를 나눌 수 없는지 확인
    indivisible_gcd_A = gcd_A if isIndivisible(gcd_A, arrayB) else 0
    indivisible_gcd_B = gcd_B if isIndivisible(gcd_B, arrayA) else 0
    
    return max(indivisible_gcd_A, indivisible_gcd_B)

def getGCD(a, b):    
    if b == 0:
        return a
    return getGCD(b, a % b)

def isIndivisible(divisor, counter_array):
    return all(num % divisor != 0 for num in counter_array)