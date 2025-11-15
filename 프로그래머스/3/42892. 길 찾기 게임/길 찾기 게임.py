# nodeinfo: i + 1 번 노드의 위치: [x, y]
# 부모 노드의 y > 자식 노드의 y
# 부모 노드의 x > 왼쪽 서브 트리의 모든 노드의 x
# 부모 노드의 x < 오른쪽 서브 트리의 모든 노드의 x
# [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

# result: [전위 순회한 결과, 후위 순회한 결과]
# 전위 순회: 자신 -> 왼 -> 오른
# 후위 순회: 왼 -> 오른 -> 자신
# [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

import sys
sys.setrecursionlimit(2000)
# 파이썬의 재귀 호출 최대 깊이는 1000인데, 트리의 깊이가 1000이므로 전위/후위 순회 시 2000번 정도 발생하므로 최대 호출 깊이 늘려줌

class Node:
    def __init__(self, node, x, y):
        self.node = node 
        self.x = x
        self.y = y
        self.left = None
        self.right = None

def pre_order(node, result):
    if node is None: # 탐색 끝나면 재귀 함수 종료
        return
    
    result.append(node.node)
    pre_order(node.left, result)
    pre_order(node.right, result)

def post_order(node, result):
    if node is None:
        return
    
    post_order(node.left, result)
    post_order(node.right, result)
    result.append(node.node)

def solution(nodeinfo):
    answer = [[], []]
    
    # y 기준 내림차순 정렬하면 y가 가장 큰 노드가 루트 노드가 됨
    nodeinfo = [(i + 1, coord) for i, coord in enumerate(nodeinfo)]
    nodeinfo.sort(key=lambda x: -x[1][1])
    
    # 루트 노드
    node, [x, y] = nodeinfo.pop(0)
    root_node = Node(node, x, y)
    
    for child in nodeinfo:
        node, [x, y] = child
        cur = root_node # 삽입할 위치를 찾기 위해 루트 노드부터 탐색 시작
            
        while True:
            if cur.x > x:
                if cur.left is None: # 현재 노드의 왼쪽이 비었다면
                    cur.left = Node(node, x, y) # 현재 노드의 왼쪽에 child를 연결
                    break # 위치 찾은 후 반복문 종료
                else:
                    cur = cur.left # 현재 노드의 왼쪽에 자식 노드가 이미 있다면, 
                    # 더 내려가서 탐색해야 하므로 현재 노드를 자식 노드로 갱신
            else:
                if cur.right is None:
                    cur.right = Node(node, x, y)
                    break
                else:
                    cur = cur.right
                    
    pre_order(root_node, answer[0])
    post_order(root_node, answer[1])
    
    return answer
