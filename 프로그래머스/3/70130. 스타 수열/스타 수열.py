from collections import Counter 
# 스타수열의 조건
# 1. 길이가 2 이상인 짝수 길이
# 2, 연속된 두 원소씩 쌍을 이루고, 모든 쌍에 교집합 원소가 있어야함 (1개 이상)
# 3. 각 쌍내의 원소는 서로 달라야함

# => 교집합 원소를 먼저 구하고, 그 원소로 만들 수 있는 최대 쌍의 개수를 구한다
def solution(a):  
    count_map = Counter(a)
    max_pairs_cnt = 0
    
    # 모든 숫자를 교집합 원소로 시도
    for x in count_map:
        if count_map[x] <= max_pairs_cnt: # 현재 원소의 등장 횟수가 이미 구한 max_pairs보다 작다면 스킵
            continue
    
        # x를 포함하는 쌍 만들기
        pairs = []
        i = 0
        
        while i < len(a) - 1:
            if (a[i] == x or a[i + 1] == x) and a[i] != a[i + 1]:
                pairs.append((a[i], a[i + 1]))
                i += 2
            else:
                i += 1
                
        max_pairs_cnt = max(max_pairs_cnt, len(pairs))
    
    return max_pairs_cnt * 2