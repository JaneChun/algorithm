# n개의 노드가 있는 네트워크 (노드는 1 ~ n)
# 단방향, 가중치 간선
# 노드 k에서 시그널을 보낼 때, 모든 노드에 시그널이 도착하는 최소시간을 구하라
# 모든 노드에 시그널이 도달할 수 없는 경우 -1을 리턴하라
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 그래프 만들기
        graph = [{} for _ in range(n + 1)] # 1-based

        for source, target, time in times:
            graph[source][target] = time

        # distance = k로부터 모든 노드까지의 거리
        distance = [float('inf')] * (n + 1) # 1-based

        # 시작점 초기화
        q = [(0, k)] # (거리, 노드번호)로 넣어야 거리 순으로 정렬됨
        distance[k] = 0
        distance[0] = 0

        while q:
            # 최소힙에서 노드를 꺼내는 순간: 최단거리가 보장된다.
            dist, cur = heapq.heappop(q) # 가장 거리가 가까운 노드부터 탐색하도록 최소 힙 사용
            
            for nxt, nxt_dist in graph[cur].items():
                acc_dist = dist + nxt_dist
                
                if acc_dist < distance[nxt]: # 처음 발견했거나, 이미 발견했지만 더 짧은 경로를 발견한 경우
                    heapq.heappush(q, (acc_dist, nxt))
                    distance[nxt] = acc_dist

        return -1 if float('inf')in distance else max(filter(lambda x: x != float('inf'), distance))