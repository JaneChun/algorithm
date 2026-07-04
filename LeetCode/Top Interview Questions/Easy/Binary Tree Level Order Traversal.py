# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/

# 이진 트리의 루트가 주어질 때, 각 노드의 값을 레벨 순서(level order)로 반환하세요.
# 즉, 왼쪽에서 오른쪽으로, 레벨별로 묶어서 반환합니다.

# 예시 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# 예시 2:
# Input: root = [1]
# Output: [[1]]

# 예시 3:
# Input: root = []
# Output: []

# 제약 조건:
# 트리의 노드 개수는 [0, 2000] 범위입니다.
# -1000 <= Node.val <= 1000

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # root부터 시작해서 left, right을 탐색
        # 같은 레벨의 노드들을 한번에 탐색해서 배열에 담아 answer에 append
        answer = []
        
        if root is None:
            return answer
        
        q = deque([root])
        
        while q:
        # 현재 큐에 들어있는 노드 수만큼 처리하면 한 레벨이 된다.
        # 반복 중 추가되는 자식 노드들은 다음 레벨에서 처리된다.
            level_size = len(q)
            nodes = []
            
            for i in range(level_size):
                cur = q.popleft()
                nodes.append(cur.val)
                
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            
            answer.append(nodes)
        
        return answer
            
        
        
        