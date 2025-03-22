def solution(cards):
    group_sizes = []
    queue = []
    visited = [False] * len(cards)
    cards = list(map(lambda x: x - 1, cards)) # cards는 1 based index이므로 0 based index로 수정해준다.
    
    for i in range(len(cards)):        
        if not visited[i]:
            queue.append(i) # BFS 시작점 세팅
            visited[i] = True
            count = 1
    
            while queue: # [0]
                cur_idx = queue.pop(0) # 인덱스 0번째 상자에 있는
                cur_box = cards[cur_idx] # 8번 카드
                if not visited[cur_box]:
                    queue.append(cur_box)
                    visited[cur_box] = True
                    count += 1
            # BFS 종료 후
            group_sizes.append(count)
    
    group_sizes.sort(reverse = True)
    
    return 0 if len(group_sizes) <= 1 else group_sizes[0] * group_sizes[1]