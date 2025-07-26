# def solution(gems):
#     answer = []
    
#     unique_gems = set(gems)
    
#     for window_size in range(len(unique_gems), len(gems) + 1):
#         for i in range(0, len(gems) - len(unique_gems) + 1):
#             sliced = gems[i:i + window_size]
#             if check(sliced, unique_gems):
#                 return [i + 1, i + window_size]
    
#     return answer

# def check(sliced, unique_gems):
#     if len(sliced) < len(unique_gems):
#         return False
    
#     for u in unique_gems:
#         if u not in sliced:
#             return False
    
#     return True


from collections import defaultdict

def solution(gems):
    unique_gems = set(gems)
    gems_counter = defaultdict(int)
    
    answer = [0, len(gems) - 1] # 최대값으로 기본값
    start = 0
    
    for end in range(len(gems)): # 오른쪽 포인터를 이동시키며 순회
        gems_counter[gems[end]] += 1 # 오른쪽 추가
        
        # 모든 종류가 포함되어 있다면
        while len(gems_counter) == len(unique_gems):
            # 더 짧다면 갱신
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
                
            # 왼쪽 삭제
            gems_counter[gems[start]] -= 1
            if gems_counter[gems[start]] == 0:
                del gems_counter[gems[start]]

            # 포인터 이동
            start += 1 
    
    return [answer[0] + 1, answer[1] + 1]
        
        
        
        
        

