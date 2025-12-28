import itertools

# 시작점이 될 수 있는 weak의 개수는 최대 15가지
# 점검하러 보낼 친구는 최대 8명이므로 8! = 40,320가지
# 모든 경우를 계산하는 경우 15 * 40,320 = 604,800번 연산
def solution(n, weak, dist):
    answer = float('inf')
    weak_len = len(weak)
    
    # 원형 -> 선형으로 변환
    extra = [w + n for w in weak]
    weak = weak + extra # [1, 5, 6, 10, 12, 17, 18, 22]
    
    # 내림차순 정렬
    dist.sort(reverse=True)
    
    # 친구들을 배치하는 모든 경우의 수(순열) 구하기
    perms = list(itertools.permutations(dist)) # [(4, 3, 2, 1), (...), ...]
    
    for i in range(weak_len): # 모든 시작점에 대해
        for perm in perms: # 모든 순열에 대해: 이 조합으로 모든 취약점을 커버할 수 있는지 확인
            sent_cnt = 0
            cur_idx = i # 현재 취약점 인덱스 (초기값이므로 첫 시작점)
            end_idx = i + weak_len - 1 # 마지막 취약점 인덱스
            
            for friend in perm: # 4
                sent_cnt += 1
                start_point = weak[cur_idx] # 현재 친구의 시작점
                end_point = start_point + friend # 현재 친구가 커버할 수 있는 최대 거리
                
                # 커버할 취약점이 남았고 & 친구가 커버할 수 있는 범위 내에 현재 취약점이 있다면
                while cur_idx <= end_idx and weak[cur_idx] <= end_point:
                    cur_idx += 1 # 커버
                
                # 모든 취약점 커버 완료
                if cur_idx > end_idx:
                    answer = min(answer, sent_cnt) # 최소값 갱신
                    break
    
    if answer == float('inf'):
        return -1
    
    return answer