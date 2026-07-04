# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/

# 이진 트리의 루트가 주어질 때, 이 트리가 자기 자신을 중심으로 좌우 대칭인지
# (즉, 가운데를 기준으로 거울에 비친 것처럼 대칭인지) 확인하세요.

# 예시 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# 예시 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

# 제약 조건:
# 트리의 노드 개수는 [1, 1000] 범위입니다.
# -100 <= Node.val <= 100

# 심화:
# 재귀와 반복 두 가지 방법 모두로 풀 수 있나요?

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_q = deque([root])
        right_q = deque([root])
        
        while left_q and right_q:
            left = left_q.popleft()
            right = right_q.popleft()
            
            # 둘다 None인 경우 큐에 넣지 X
            if left is None and right is None:
                continue
                
            # 둘 중 하나가 None이여서 비대칭인 경우 return False
            if left is None or right is None:
                return False
            
            # 같은 위치의 두 노드의 값이 다르면 return False
            if left.val != right.val:
                return False
                
            left_q.append(left.left)
            left_q.append(left.right)

            right_q.append(right.right) # 대칭이려면 반대 순서로 넣어줘야 함
            right_q.append(right.left)
        
        return True