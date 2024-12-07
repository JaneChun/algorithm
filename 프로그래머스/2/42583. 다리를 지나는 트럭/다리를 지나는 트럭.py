from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    # 다리 상태 초기화 : 다리 길이만큼 0으로 채움
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    cur_bridge_weight = 0
    
    while truck_weights or cur_bridge_weight > 0:
        time += 1

        # 트럭 나감 & 다리에서 트럭이 나감 (현재 다리 무게 계산)
        cur_bridge_weight -= bridge[0]
        
        # 다리에 새로운 트럭이 오를 수 있는지 확인
        if truck_weights and cur_bridge_weight + truck_weights[0] <= weight:
            cur_truck = truck_weights.pop(0)
            bridge.append(cur_truck) # 트럭 올라옴
            cur_bridge_weight += cur_truck # (다리 무게 계산)
        else:
            bridge.append(0)
    
    return time