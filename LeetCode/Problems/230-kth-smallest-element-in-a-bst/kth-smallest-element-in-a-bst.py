# 이진탐색트리에서 k번째 작은 값의 index를 반환 (1 based)
# 이진탐색트리: 왼쪽 서브트리의 모든 값 < 루트 < 오른쪽 서브트리의 모든 값
# 이진탐색트리는 중위순회(left - root - right)를 하면 오름차순으로 정렬된다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        # 중위순회해서 k번째 탐색된 노드의 값을 반환
        count = 0

        def inorder(root):
            nonlocal count

            # left 탐색
            if root.left:
                found = inorder(root.left)
                if found is not None: 
                    return found
            
            # root 탐색
            count += 1
            if count == k:
                return root.val
            
            # right 탐색
            if root.right:
                return inorder(root.right)

        return inorder(root)
