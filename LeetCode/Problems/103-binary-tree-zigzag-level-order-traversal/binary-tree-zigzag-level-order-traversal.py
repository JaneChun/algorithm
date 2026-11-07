# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
           return []

        answer = []
        q = deque([root])
        reverse = False

        while q:
            # 같은 depth의 요소들의 개수
            level_size = len(q)
            level = []

            for _ in range(level_size):
                cur = q.popleft()
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if reverse:
                level.reverse()

            answer.append(level)
            reverse = not reverse
        
        return answer