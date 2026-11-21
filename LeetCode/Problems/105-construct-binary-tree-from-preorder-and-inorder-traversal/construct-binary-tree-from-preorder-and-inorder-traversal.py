# preorder: root -> left -> right
# inorder : left -> root -> right
# preorder(전위순회), inorder(중위순회) 결과 배열이 주어질 때 원본 트리를 반환하라

# preorder = [3, 9, 20, 15, 7]
#             R [9] [20, 15, 7]
#               왼쪽  오른쪽 서브트리

# inorder = [9, 3, 15, 20, 7]
#           [9] R [15, 20, 7]
#           왼쪽    오른쪽 서브트리

# Inorder에서 구한 노드 개수를 Preorder의 구간을 나누는 기준으로 사용
# preorder의 0번째 노드는 루트
# 이 루트로 inorder에서 루트를 찾고, 루트 기준으로 왼쪽, 오른쪽 서브트리를 구한다.
# 여기서 구한 각 서브트리의 노드 개수로 preorder에서도 왼쪽, 오른쪽 서브트리를 구할 수 있다.
# 각 서브트리에 대해 위 과정을 재귀적으로 반복한다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def get_subtree(root, tree):
            if len(tree) == 0: # 재귀 종료 조건
                return

            root_idx = tree.index(root.val)
            left_tree = tree[0:root_idx]      # [9]
            right_tree = tree[root_idx + 1:]  # [15, 20, 7]

            if left_tree:
                # preorder에서 루트 찾기
                left_root = preorder[preorder.index(root.val) + 1] # 9
                root.left = TreeNode(left_root)
                # 서브트리로 재귀호출
                get_subtree(root.left, left_tree)
            
            if right_tree:
                right_root = preorder[preorder.index(root.val) + len(left_tree) + 1] # 20
                root.right = TreeNode(right_root)
                get_subtree(root.right, right_tree)

        root = TreeNode(preorder[0])
        get_subtree(root, inorder)

        return root