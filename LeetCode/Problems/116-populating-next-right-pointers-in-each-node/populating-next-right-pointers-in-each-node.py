# 포화 이진트리가 주어질 때 트리의 각 노드에 next 정보를 추가하여 반환한다.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
            
        # BFS로 레벨별로 순회한다.
        # 같은 레벨에 있는 노드끼리 next로 연결한다.
        
        q = deque([root])
        while q:
            size = len(q)
            children = []

            for i in range(size):
                cur = q.popleft()
                cur.next = q[0] if q else None

                if cur.left and cur.right:
                    children.extend([cur.left, cur.right])
            
            # 자식 모아서 추가
            q.extend(children)

        return root

        