import math
# n번 블록은 n*2, n*3, n*4 ... 위치에 설치
# 1번 블록 : 2, 3, 4, 5 ...
# 2번 블록 : 4, 6, 8, 10, 12 ...
# 3번 블록 : 6, 9, 12, 15 ...
# 4번 블록 : 8, 12, 16, 20 ...
# 5번 블록 : 10, 15, 20, 25 ...
def solution(begin, end):
    answer = []
        
    # 만약 num가 9인 경우: 9의 약수 1, 3 으로 덮어씌워짐
    # 만약 num가 10인 경우: 10의 약수 1, 2, 5 로 덮어씌워짐
    # 만약 num가 12인 경우: 12의 약수 1, 2, 3, 4, 6 순서대로 값이 덮어씌워짐
    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue
        
        if num == 2 or num == 3:
            answer.append(1)
            continue
        
        max_divisor = 1
        
        for i in range(2, int(math.sqrt(num)) + 1):        
            if num % i == 0:        
                # num의 가장 작은 약수 i(2 이상) 를 찾으면, 그에 대응되는 가장 큰 약수는 num // i
                pair = num // i 
                if pair <= 10_000_000: # 약수(pair)가 1000만을 넘지 않는 경우 
                    max_divisor = pair
                    break
                # pair가 1000만을 넘는다면 약수(i) 중에 1000만을 넘지 않고 가장 큰 수
                if i <= 10_000_000:
                    max_divisor = i
        answer.append(max_divisor)
            
    return answer

        