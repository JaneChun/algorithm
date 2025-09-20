from collections import defaultdict

def solution(enroll, referral, seller, amount):
    profit_dict = defaultdict(int) # { 구성원: 이익 }
    ref_dict = {} # { 구성원: 추천인 }
    
    for e, r in zip(enroll, referral):
        ref_dict[e] = r
        
    for s, a in zip(seller, amount):
        me = s
        profit = a * 100
        
        while me != '-' and profit > 0:
            commission = int(profit * 0.1) # 수수료 10%
            profit_dict[me] += profit - commission # 본인 이익 - 수수료
            
            me = ref_dict[me]
            profit = commission
    
    return [profit_dict[name] for name in enroll]