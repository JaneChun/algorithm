# 원의 방정식
# x^2 + y^2 <= r^2

# r2 원 안에 있는 점의 개수 - r1 원 안에 있는 점의 개수
# 1사분면만 구해서 * 4
import math

def solution(r1, r2):
    answer = 0
    
    for x in range(0, r2 + 1):
        maxY = math.floor(math.sqrt(r2*r2 - x*x))
        minY = 0 if r1 < x else math.ceil(math.sqrt(r1*r1 - x*x)) 
        
        answer += maxY - minY + 1
        
    # 경계선 부분 중복되므로 빼주기
    answer -= r2 - r1 + 1
    
    return answer * 4