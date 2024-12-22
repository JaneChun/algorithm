# def solution(weights):
#     answer = 0
#     cases = [[1, 1], [1, 2], [2, 3], [3, 4]] # 경우의 수
    
#     for i in range(len(weights) - 1):
#         for j in range(i + 1, len(weights)):
#             a = weights[i]
#             b = weights[j]
            
#             for n, m in cases:
#                 if (a * n == b * m) or (a * m == b * n):
#                     answer += 1
#     return answer
# O(n^2)의 시간 복잡도를 가지며, 이는 제한 조건의 최대 길이 100,000에 대해 비효율적

from collections import Counter

def solution(weights):
    answer = 0
    # 1. 몸무게 몇 번 나왔는지 세기
    weight_count = Counter(weights)

    # 2. 같은 몸무게끼리 짝꿍 계산
    for weight, count in weight_count.items():
        if count > 1:  # 같은 몸무게가 2번 이상이면
            answer += count * (count - 1) // 2  # 짝꿍 수 계산

    # 3. 다른 몸무게끼리 짝꿍 계산
    # 가능한 거리 비율
    ratios = [1/2, 2/3, 3/4]
    
    for weight in weights:
        for ratio in ratios:
            # 거리 비율에 따라 몸무게 곱하기
            target_weight = weight * ratio
            # 그 몸무게가 실제로 존재하면 짝꿍 추가
            if target_weight in weight_count:
                answer += weight_count[target_weight]

    return answer
