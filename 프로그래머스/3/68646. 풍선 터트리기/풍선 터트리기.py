# a b 'c' d e -> c가 살아남으려면 a, b 가 c보다 커야 함 & d, e 가 c보다 커야 함. 단 1개만 작아도됨

# 어떤 풍선이 살아남을 수 있으려면
# 그 풍선의 한쪽 방향에는 자기보다 작은 값이 최대 1개만 있어야 한다.
# def solution(a):
#     answer = 0
    
#     for i in range(len(a)):
#         cur = a[i]
#         left = a[:i]
#         right = a[i + 1:]

#         left_min = float('inf')
#         right_min = float('inf')
        
#         if left:
#             left_min = min(left)
#         if right:
#             right_min = min(right)
        
#         if left_min < cur and right_min < cur:
#             continue
        
#         answer += 1
    
#     return answer

# 시간초과 -> for 문 * min 연산 => O(N^2) 시간 복잡도

def solution(a):
    answer = 0
    
    # 왼쪽에서부터 i 까지의 최솟값을 담은 배열
    left_dp = [float('inf')] * len(a)
    left_dp[0] = a[0]
    
    # 오른쪽에서부터 i 까지의 최솟값을 담은 배열
    right_dp = [float('inf')] * len(a)
    right_dp[-1] = a[-1]
    
    for i in range(1, len(a)):
        left_dp[i] = min(a[i], left_dp[i - 1]) # min(현재값, 이전까지의 최소값)
    
    for i in range(len(a) - 2, -1, -1):
        right_dp[i] = min(a[i], right_dp[i + 1]) # min(현재값, 이전까지의 최소값)
        
    
    for i in range(len(a)):
        cur = a[i]
        left_min = left_dp[i]
        right_min = right_dp[i]
        
        if left_min < cur and right_min < cur:
            continue
        
        answer += 1
    
    return answer