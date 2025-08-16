# 크루스칼(Kruskal) 알고리즘
# 1. 모든 다리를 비용 순으로 정렬
# 2. 가장 싼 다리부터 연결
# 3. 연결할 때 사이클이 생기면 건너뜀
# 4. 반복 → 모든 섬이 연결될 때까지
# 5. 선택된 다리 비용 합 = MST 비용

def solution(n, costs):
    answer = 0
    
    # 1. 모든 다리를 비용 순으로 정렬
    costs.sort(key = lambda x: x[2])
    
    parent  = [i for i in range(n)]
    
    # x가 속한 그룹(대표 노드, 루트)을 찾는 함수
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) # 경로 압축
        return parent[x]
    
    # x가 속한 그룹과 y가 속한 그룹을 합치는 함수
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        
        if x_root != y_root:
            parent[y_root] = x_root # 그룹 합치기
        
    
    # 2. 가장 싼 다리부터 연결
    for a, b, cost in costs:
        if find(a) != find(b): # 사이클이 없다면
            union(a, b) # 연결
            answer += cost
    
    return answer
    