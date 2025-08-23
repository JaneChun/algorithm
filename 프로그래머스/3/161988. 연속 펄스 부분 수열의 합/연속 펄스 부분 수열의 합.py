def solution(sequence):
    answer = 0
    a_sequence = [x if i % 2 == 0 else -x for i, x in enumerate(sequence)]
    b_sequence = [-x if i % 2 == 0 else x for i, x in enumerate(sequence)]
    
    a_max = get_max_sub_sum(a_sequence)
    b_max = get_max_sub_sum(b_sequence)
    
    return max(a_max, b_max)

# 카데인 알고리즘: O(n)의 시간 복잡도를 가지는 최대부분합 구하는 알고리즘
def get_max_sub_sum(arr):
    cur_sum = arr[0]
    max_sum = arr[0]
    
    for n in arr[1:]:
        cur_sum = max(cur_sum + n, n) # cur_sum = 이어가기(지금까지의 합) 또는 새로 시작
        max_sum = max(max_sum, cur_sum)
        
    return max_sum