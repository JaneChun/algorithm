# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder(1) -> 2 -> 4(x) -> 2(x) ->
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        answer = []

        def inorder(node: TreeNode):
            # 더 이상 노드가 없으면 재귀 함수 종료
            if node is None:
                return

            # 노드가 있으면 왼, 나, 오 순으로 탐색 처리
            inorder(node.left)
            answer.append(node.val)
            inorder(node.right)

        inorder(root)

        return answer
        