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

        print(graph)
        # [{}, {}, {1: 1, 3: 1}, {4: 1}, {}]

        # distance = k로부터 모든 노드까지의 거리
        distance = [-1] * (n + 1) # 1-based

        # 시작점 초기화
        q = [(k, 0)]
        distance[k] = 0
        distance[0] = 0

        while q:
            print(q)
            cur, dist = heapq.heappop(q) # 가장 거리가 가까운 노드부터 탐색하도록 최소 힙 사용
            print(cur, dist)
            
            for nxt, nxt_dist in graph[cur].items():
                # if distance[nxt] == -1: # 첫 방문이 최소 거리이므로
                #         heapq.heappush(q, (nxt, dist + nxt_dist))
                #         distance[nxt] = dist + nxt_dist
                # X -> 첫 방문이 최소 거리가 아닐 수 있다. 1 -(4)-> 3 보다 1 -(1)-> 2 -(2)->3 이 더 싸다. 

                # 첫 방문인 경우 무조건 탐색하고, 아니면 기존 distance보다 작은 경우에만 탐색
                acc_dist = dist + nxt_dist
                if distance[nxt] == -1 or acc_dist < distance[nxt]:
                    heapq.heappush(q, (nxt, acc_dist))
                    distance[nxt] = acc_dist

        print(distance)
        return -1 if -1 in distance else max(distance)