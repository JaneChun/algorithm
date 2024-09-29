def solution(elements):
    sum_set = set()
    extended_elements = elements * 2
    
    # 길이별로 수열의 합 구하기
    for sub_len in range(1, len(elements) + 1): # 1, 2, 3, 4, 5
        for i in range(0, len(extended_elements)):
            sub_sum = extended_elements[i : i + sub_len]
            sum_set.add(sum(sub_sum))
            
    return len(sum_set)

# 위 방법은 시간 복잡도가 O(n^3)
# 시간 복잡도를 줄이기 위해 sub_sum을 구하는 부분에서 매번 슬라이싱하는 대신 누적 합을 사용할 수 있다.
# 누적 합 : 각 부분 수열의 첫 번째 합은 미리 계산하고, 그 후에는 한 칸씩 이동할 때 앞에서 하나를 빼고 뒤에서 하나를 더하는 방식으로 부분합을 업데이트하는 방법

# def solution(elements):
#     sum_set = set()
#     extended_elements = elements * 2
    
#     # 길이별로 수열의 합 구하기
#     for sub_len in range(1, len(elements) + 1): # 1, 2, 3, 4, 5
#         sub_sum = sum(elements[0 : sub_len]) # 초기 부분합 계산
#         sum_set.add(sub_sum)
        
#         # 한 칸씩 이동하며 부분합을 업데이트
#         for i in range(1, len(elements)):
#             sub_sum -= extended_elements[i - 1]
#             sub_sum += extended_elements[i + sub_len - 1]
#             sum_set.add(sub_sum)
            
#     return len(sum_set)

# O(n^2)