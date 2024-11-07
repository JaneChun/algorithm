from collections import deque

def solution(order):
    truck = []
    container = deque(range(1, len(order) + 1)) # queue
    sub_container = [] # stack
    
    next_idx = 0
    
    while(container or sub_container):
        next_box = order[next_idx]
        
        # 컨테이너 벨트에서 순서에 맞는 상자를 꺼낼 수 있는 경우
        if container and container[0] == next_box:
            truck.append(container.popleft())
            next_idx += 1
        # 보조 컨테이너 벨트에서 순서에 맞는 상자를 꺼낼 수 있는 경우
        elif sub_container and sub_container[-1] == next_box:
            truck.append(sub_container.pop())
            next_idx += 1
        # 순서에 맞는 상자를 꺼낼 수 없어 보조 컨테이너 벨트로 이동하는 경우
        elif container:
            sub_container.append(container.popleft())
        # 위의 어떤 것도 불가능한 경우 반복문 종료
        else:
            break
    
    return len(truck)