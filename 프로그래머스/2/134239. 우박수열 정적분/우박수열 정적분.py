def solution(k, ranges):   
    # k가 1일 될 때까지 아래 반복문을 반복하며 우박수열을 계산
    collatz = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        collatz.append(k)
    print(collatz) # [5, 16, 8, 4, 2, 1]
    
    # 각 구간의 넓이 계산
    # 사다리꼴 공식 = (윗변 + 아랫변) / 2 * 높이 
    area = []
    for i in range(len(collatz) - 1):
        # 윗변:  collatz[i]
        # 아랫변:  collatz[i + 1]
        # 높이: 1 
        trapezoid = (collatz[i] + collatz[i + 1]) / 2
        area.append(trapezoid)
    print(area) # [10.5, 12.0, 6.0, 3.0, 1.5]
    
    # 각 구간의 면적에 대해 누적합 배열을 생성
    prefix_sum = [0]
    for i in range(len(area)):
        prefix_sum.append(prefix_sum[i] + area[i])
    print(prefix_sum) # [0, 10.5, 22.5, 28.5, 31.5, 33.0]
    
    # 정적분 결과 계산
    answer = []
    n = len(collatz) - 1 # 총 구간은 5개
    for a, b in ranges:
        end = n + b 
        if a > end: # 시작점이 끝점보다 커서 유효하지 않은 구간인 경우
            answer.append(-1)
        else:
            answer.append(prefix_sum[end] - prefix_sum[a])
    
    return answer