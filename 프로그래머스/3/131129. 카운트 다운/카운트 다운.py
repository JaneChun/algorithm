# 싱글로 얻을 수 있는 점수 : 1 ~ 20
# 더블 : 2,4 ..~ 40
# 트리플 : 3 ~ 60
# 불 : 50
def solution(target):
    answer = []
    
    scores = []
    # 싱글
    for i in range(1, 21):
        scores.append((i, 1))
    # 더블
    for i in range(1, 21):
        scores.append((i*2, 0))
    # 트리플
    for i in range(1, 21):
        scores.append((i*3, 0))
    # 불
    scores.append((50, 1))
    
    print(scores)
    
    # dp[i] = (dart_cnt, singbull_cnt)
    # i 점수를 받을 수 있는 경우 중 최소한의 다트를 사용하고 싱글/불 횟수가 최대가 되는 경우
    dp = [(float('inf'), 0) for _ in range(target + 1)]
    dp[0] = (0, 0)
    
    for i in range(1, target + 1): # 1, 2, 3 ...
        for (score, singbull) in scores: # (1,1), (2, 0), (2, 1), (3, 0), (3, 1)..
            if i - score < 0:
                continue
                
            dart_cnt, singbull_cnt = dp[i]
            
            cur_dart_cnt = dp[i - score][0] + 1
            cur_singbull_cnt = dp[i - score][1] + singbull

            if (
                cur_dart_cnt < dart_cnt or # 최소한의 다트가 가장 중요하고
                (cur_dart_cnt == dart_cnt and cur_singbull_cnt > singbull_cnt) # 다트 수가 같다면 싱글, 불이 최대한 많아야 함
            ):
                dp[i] = (cur_dart_cnt, cur_singbull_cnt) 
    
    return dp[target]