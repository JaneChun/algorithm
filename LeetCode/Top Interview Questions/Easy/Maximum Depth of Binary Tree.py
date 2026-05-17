# https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

# 이진 트리의 루트 root가 주어졌을 때, 이진 트리의 최대 깊이를 반환하세요.
# 이진 트리의 최대 깊이란, 루트 노드에서 가장 먼 리프 노드까지 내려가는 가장 긴 경로에 포함된 노드의 개수를 의미합니다.
# 예를 들어 루트에서 리프까지 경로가 다음과 같다면:
# root → child → leaf
# 노드가 3개이므로 최대 깊이는 3입니다.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, depth: int) -> int:
            if not node:
                return 0

            if not node.left and not node.right:
                return depth

            max_depth = 0
            if node.left:
                max_depth = max(max_depth, dfs(node.left, depth + 1))
            if node.right:
                max_depth = max(max_depth, dfs(node.right, depth + 1))

            return max_depth

        return dfs(root, 1)
