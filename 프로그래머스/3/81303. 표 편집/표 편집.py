def solution(n, k, cmd):
    answer = ['O'] * n
    deleted = []
    cur = k
    
    # 각 행(i)의 이전 행, 다음 행을 저장
    prev = [i - 1 for i in range(n)]
    nxt = [i + 1 for i in range(n)]
       
    prev[0] = -1
    nxt[n - 1] = -1
    
    for command in cmd:       
        if len(command) == 1:
            action = command
        else:
            action, count = command.split(' ')
            count = int(count)
            
        if action == 'U':
            # i번 위로 올라감 = i번 이전 행이 현재 행이 됨
            for i in range(count):
                cur = prev[cur]
        elif action == 'D':
            # i번 아래로 내려감 = i번 다음 행이 현재 행이 됨
            for i in range(count):
                cur = nxt[cur]
        elif action == 'C':
            deleted.append(cur)
            answer[cur] = 'X'
            
            # 현재 행이 삭제되므로 이전 행과 다음 행을 연결
            if prev[cur] != -1: # 이전 행이 있는 경우, 이전 행의 nxt가 다음 행을 가리키게 (이전 행이 없는 경우 그대로 -1을 가리킴)
                nxt[prev[cur]] = nxt[cur]
            if nxt[cur] != -1: # 다음 행이 있는 경우, 다음 행의 prev가 이전 행을 가리키게
                prev[nxt[cur]] = prev[cur]
                
            # 커서 이동: 현재 행이 마지막 행이라면 이전 행이 현재 행이 되고, 그 외의 경우 다음 행이 현재 행이 됨  
            cur = prev[cur] if nxt[cur] == -1 else nxt[cur]
        else: # action == 'Z'
            restored = deleted.pop()
            answer[restored] = 'O'
            
            # 현재 행이 복원되므로 이전 행과 현재 행을 연결, 현재 행과 다음 행을 연결
            if prev[restored] != -1:
                nxt[prev[restored]] = restored
            if nxt[restored] != -1:
                prev[nxt[restored]] = restored
    
    return ''.join(answer)