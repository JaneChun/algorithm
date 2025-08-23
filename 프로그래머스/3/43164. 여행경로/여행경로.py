# def solution(tickets):
#     answer = ['ICN']
#     visited = [False] * len(tickets)
    
#     tickets.sort(key = lambda x: [x[0], x[1]])
    
#     def dfs(departure, depth):
#         if depth == len(tickets):
#             return answer
        
#         for index, ticket in enumerate(tickets):
#             if ticket[0] == departure and not visited[index]:
#                 answer.append(ticket[1])
#                 visited[index] = True
#                 return dfs(ticket[1], depth + 1)
            
#     return dfs('ICN', 0)
# -> 정렬만으로는 올바른 순서(모든 티켓을 다 사용하는 루트)를 보장하지 못하므로, 백트래킹이 반드시 필요하다.

def solution(tickets):
    answer = ['ICN']    
    visited = [False] * len(tickets)
    
    tickets.sort(key = lambda x: [x[0], x[1]])
    
    def dfs(departure, depth):
        if depth == len(tickets):
            return True
        
        for index, ticket in enumerate(tickets):
            if ticket[0] == departure and not visited[index]:
                answer.append(ticket[1])
                print(answer)
                visited[index] = True
                
                # 경로 완성인 경우
                if dfs(ticket[1], depth + 1):
                    return True
                # 그 외의 경우 백트래킹(돌아가서 다른 경로 시도)
                answer.pop()
                visited[index] = False
                
    dfs('ICN', 0)
            
    return answer