# 배열을 내림차순으로 정리한 풀이 -> 시간초과
# def solution(scoville, K):
#     count = 0
#     scoville.sort(reverse = True)
    
#     while scoville[-1] < K:
#         if len(scoville) < 2:
#             return -1
        
#         first = scoville.pop()
#         second = scoville.pop()
        
#         new_scoville = first + second * 2
#         scoville.append(new_scoville)
#         count += 1
#         scoville.sort(reverse = True)
        
#     return count

# 최소 힙 사용 풀이
import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville) # scoville을 최소 힙으로 변환
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)
        count += 1
        
    return count