# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/

# 이진 트리의 루트가 주어질 때, 이 트리가 유효한 이진 탐색 트리인지 확인하세요.
#
# 유효한 이진 탐색 트리는 다음 조건을 만족합니다.
# 어떤 노드의 왼쪽 서브트리에 있는 모든 노드의 값은 현재 노드의 값보다 작아야 합니다.
# 어떤 노드의 오른쪽 서브트리에 있는 모든 노드의 값은 현재 노드의 값보다 커야 합니다.
# 왼쪽 서브트리와 오른쪽 서브트리도 각각 이진 탐색 트리여야 합니다.

# 예시 1:
# Input: root = [2,1,3]
# Output: true

# 예시 2:
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# 설명: 루트 노드의 값은 5이지만, 오른쪽 자식 노드의 값이 4입니다.

# 제약 조건:
# 트리의 노드 개수는 [1, 10^4] 범위입니다.
# -2^31 <= Node.val <= 2^31 - 1

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 유효한 이진트리의 조건:
# 어떤 노드의 왼쪽 서브트리에 있는 모든 노드의 값은 현재 노드의 값보다 작아야 함
# 어떤 노드의 오른쪽 서브트리에 있는 모든 노드의 값은 현재 노드의 값보다 커야 함
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, -float('inf'), float('inf'))]) # [노드, lower, upper]
        # 각 노드와 함께 그 노드 값이 만족해야 하는 범위(lower, upper)를 저장한다.
        # lower < node.val < upper 여야 한다.
        
        #     4
        #    / \
        #   2   6
        #  / \ / \
        # 1  3 5  7
        
        # 루트 4의 범위: -inf < 4 < inf
            # 2는 4의 왼쪽 자식이니까: -inf < 2 < 4
                # 1은 2의 왼쪽 자식이니까: -inf < 1 < 2
                # 3은 2의 오른쪽 자식이니까 : 2 < 3 < 4
            # 6은 4의 오른쪽 자식이니까: 4 < 6 < inf
                # 5는 6의 왼쪽 자식이니까 4 < 5 < 6
                # 7은 6의 오른쪽 자식이니까 6 < 7 < inf
        
        while q:
            cur, lower, upper = q.popleft()
            
            if not lower < cur.val < upper:
                return False
            
            if cur.left: 
                q.append((cur.left, lower, cur.val))
            
            if cur.right: 
                q.append((cur.right, cur.val, upper))
                
        return True