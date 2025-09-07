import heapq

# 비어있다면 가장 우선순위가 높은 작업을 큐에서 꺼냄
# 우선순위: 시간이 짧은 것 > 요청 시간이 빠른 것 > 번호가 작은 것

def solution(jobs):
    N = len(jobs)
    now = 0 # 현재 시간
    total_time = 0 # 작업에 소요된 시간 (반환시간)
    
    heap = []
    jobs = sorted([(s, l) for s, l in jobs], key=lambda x: x[0]) # 요청시간 기준 정렬
    jobs = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    
    while jobs or heap:
        while jobs and jobs[0][0] <= now: # 현재 시간까지 요청된 작업 모두
            s, l, i = jobs.pop(0)
            heapq.heappush(heap, (l, s, i)) # 힙에 추가
        
        if heap:
            l, s, i = heapq.heappop(heap)
            now += l # 작업시간만큼 시간이 흐름
            total_time += (now - s)  # 반환시간 = 작업완료시간 - 요청시간
        else:
            now = jobs[0][0] # 작업이 없다면 다음 작업 요청시간까지 시간이 흐름
    
    return total_time // N