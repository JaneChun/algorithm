# def solution(scores):
#     score_map = [{'att': att, 'peer': peer, 'total': att + peer, 'idx': idx} for idx, (att, peer) in enumerate(scores)]
    
#     score_map.sort(key = lambda x: -x['total'])
    
#     rank = 0
#     prev_score = None
#     same_rank_cnt = 1
#     for score in score_map:
#         att, peer, total, idx = score['att'], score['peer'], score['total'], score['idx']

#         # 인센티브를 받지 못하면 제외
#         if not can_get_incentive((att, peer), scores):
#             continue
        
#         if prev_score == total:
#             same_rank_cnt += 1
#         else:
#             rank += same_rank_cnt
            
#             # 변수 초기화
#             same_rank_cnt = 1
#             prev_score = total
            
#         # 완호라면 석차 반환
#         if idx == 0:
#             return rank
    
#     return -1

# def can_get_incentive(score, scores):
#     att, peer = score
#     higher_att = list(filter(lambda x: x[0] > att, scores))
#     higher_att_peer = list(filter(lambda x: x[1] > peer, higher_att))
    
#     if len(higher_att_peer):
#         return False
#     else:
#         return True
    
# for문 * can_get_incentive에서 filter문 => O(N^2)의 시간 복잡도

def solution(scores):
    score_map = [{'att': att, 'peer': peer, 'total': att + peer, 'idx': idx} for idx, (att, peer) in enumerate(scores)]
    
    # att를 기준으로 내림차순, peer 기준으로 오름차순 정렬
    score_map.sort(key = lambda x: [-x['att'], x['peer']] )
    
    max_peer = float('-inf')
    candidates = []
    
    for score in score_map:
        peer = score['peer']
    
        # att 기준 내림차순 정렬이므로 나는 이전의 모든 사원보다 att가 같거나 낮음
        # 따라서 만약 이전의 모든 사원 중 단 한 명이라도(max_peer) 그 사람보다 peer도 낮다면,
        # -> 두 점수 모두 낮은 경우이므로 인센티브를 받지 못함
        if peer < max_peer:
            continue
        else:
            candidates.append(score)
            max_peer = peer
            
    # 순위 계산을 위해 총점 기준 정렬
    candidates.sort(key = lambda x: -x['total'])
    
    rank = 0
    prev_score = None
    same_rank_cnt = 1
    for score in candidates:
        total, idx = score['total'], score['idx']

        if prev_score == total:
            same_rank_cnt += 1
        else:
            rank += same_rank_cnt
            
            # 변수 초기화
            same_rank_cnt = 1
            prev_score = total
            
        # 완호라면 석차 반환
        if idx == 0:
            return rank
        
    return -1
    
    