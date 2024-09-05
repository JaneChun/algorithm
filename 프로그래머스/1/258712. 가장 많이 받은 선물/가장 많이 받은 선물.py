def solution(friends, gifts):
    gift_dict = {}
    
    for name in friends:
        gift_dict[name] = {}
        for friend in friends:
            if name != friend:
                gift_dict[name][friend] = 0
    
    # 선물 주고받기 기록
    for gift in gifts:
        giver, receiver = gift.split(' ')
        gift_dict[giver][receiver] += 1
        
    # 각 사람이 다음 달에 받을 선물 개수를 저장할 딕셔너리
    next_month_gifts = {name: 0 for name in gift_dict}

    # 각 사람을 순회하며 선물 계산
    for giver, receivers in gift_dict.items():
        for receiver, give_count in receivers.items():
            receive_count = gift_dict[receiver][giver]
            
            # 더 많이 준 사람이 다음 달에 하나 받음
            if give_count > receive_count: 
                next_month_gifts[giver] += 1
            elif give_count < receive_count:
                next_month_gifts[receiver] += 1
            # 선물 지수로 결정 (선물 지수 : 내가 준 선물 수 - 내가 받은 선물 수 )
            else: 
                giver_gift_index = sum(gift_dict[giver].values()) - sum(gift_dict[name][giver] for name in gift_dict if name != giver)
                receiver_gift_index = sum(gift_dict[receiver].values()) - sum(gift_dict[name][receiver] for name in gift_dict if name != receiver)
                if giver_gift_index > receiver_gift_index:
                    next_month_gifts[giver] += 1
                elif giver_gift_index < receiver_gift_index:
                    next_month_gifts[receiver] += 1
                else:
                    continue
        
    return max(next_month_gifts.values()) / 2
