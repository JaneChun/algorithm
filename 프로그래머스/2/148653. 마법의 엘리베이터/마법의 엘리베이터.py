def solution(storey):
    answer = 0
    
    while storey > 0:
        digit = storey % 10 # 현재 자릿수
        
        if digit < 5: # 5 미만이면 그냥 이동
            answer += digit
        elif digit > 5: # 5 초과면 올림하여 더 작은 비용으로 이동
            answer += (10 - digit)
            storey += 10
        else: # 5인 경우 다음 자릿수를 고려해서 이동
            next_digit = (storey // 10) % 10
            if next_digit < 5:
                answer += digit
            else:
                answer += (10 - digit)
                storey += 10
        
        storey //= 10 # 다음 자릿수로 이동
    
    return answer