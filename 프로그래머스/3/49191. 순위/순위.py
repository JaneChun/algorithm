def solution(n, results):
    answer = 0
    graph = {i: { 'wins': set(), 'losses': set() } for i in range(1, n + 1)}
    
    def find_all_wins(player):
        direct_losers = list(graph[player]['wins'])
        stack = direct_losers[::]
        visited = set()

        while stack:
            opponent = stack.pop()
            
            if opponent not in visited:
                visited.add(opponent)
                
                # player가 이긴 상대에 대해서, 상대가 이긴 사람도 player가 이긴 것
                for next_opponent in graph[opponent].get('wins'):
                    if next_opponent not in visited:
                        stack.append(next_opponent)
                        graph[player]['wins'].add(next_opponent)
    
    def find_all_losses(player):
        direct_winners = list(graph[player]['losses'])
        stack = direct_winners[::]
        visited = set()
        
        while stack:
            opponent = stack.pop()
            
            if opponent not in visited:
                visited.add(opponent)
                
                # player가 진 상대에 대해서, 상대가 진 사람에게도 player가 진 것
                for next_opponent in graph[opponent].get('losses'):
                    if next_opponent not in visited:
                        stack.append(next_opponent)
                        graph[player]['losses'].add(next_opponent)
                
    
    # 직접 대결 결과 등록
    for winner, loser in results:
        graph[winner]['wins'].add(loser)
        graph[loser]['losses'].add(winner)
    
    # 간접 대결 결과 계산
    for player in graph:
        find_all_wins(player)
        find_all_losses(player)
        
    for record in graph.values():
        win_count = len(record.get('wins'))
        lose_count = len(record.get('losses'))
    
        # win_count + lose_count의 개수가 n - 1이면 모든 사람과의 승패가 명확히 정해진(등수가 정해진) 사람임
        if win_count + lose_count == n - 1:
            answer += 1
    
    return answer