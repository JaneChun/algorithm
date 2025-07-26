def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    # 첫 번째부터 떼는 경우, 마지막은 못 뗌
    dp1 = [0] * len(sticker)
    dp1[0] = sticker[0]
    
    for i in range(1, len(sticker) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i]) 
        # dp[i - 1] : i번째를 안떼는 경우
        # dp[i - 2] + sticker[i] : i번째를 떼는 경우
    
    
    # 두 번째부터 떼는 경우, 마지막 뗄 수 있음
    dp2 = [0] * len(sticker)
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i]) 
        
    return max(dp1[-2], dp2[-1])