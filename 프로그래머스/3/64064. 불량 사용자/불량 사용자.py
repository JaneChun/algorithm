from collections import defaultdict

def solution(user_id, banned_id):
    answer = set()
    
    matching_candidates = []
    
    for b_id in banned_id:
        matching_users = []
        
        for u_id in user_id:
            if match(u_id, b_id):
                matching_users.append(u_id)
            
        matching_candidates.append(matching_users)
        
    # print(matching_candidates)
    # [['frodo', 'crodo'], ['frodo', 'crodo'], ['abc123', 'frodoc']]

    
    def dfs(depth, selected_users):
        # banned_id 별로 하나씩 선택 완료된 경우
        if depth == len(matching_candidates):
            answer.add(frozenset(selected_users))
            return

        # 그외의 경우, 선택을 이어감
        for user in matching_candidates[depth]:
            if user not in selected_users:
                dfs(depth + 1, selected_users + [user])

    # dfs 흐름
    # crodo, frodo, frodoc
    # crodo, frodo, abc123
    dfs(0, [])
    
    return len(answer)

    
def match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    
    for i in range(len(banned_id)):
        if banned_id[i] == '*':
            continue
        
        if user_id[i] != banned_id[i]:
            return False
    
    return True