# # https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/

# 단일 연결 리스트 head가 있고, 그 안의 특정 노드 node를 삭제하려고 합니다.

# 당신에게는 삭제할 노드 node만 주어집니다.
# 즉, 연결 리스트의 첫 번째 노드인 head에는 접근할 수 없습니다.

# 연결 리스트의 모든 값은 서로 다르며, 주어진 노드 node는 마지막 노드가 아님이 보장됩니다.

# 주어진 노드를 삭제하세요.

# 여기서 노드를 삭제한다는 것은 메모리에서 제거한다는 뜻이 아닙니다.
# 다음 조건을 만족하도록 연결 리스트를 수정하라는 뜻입니다.

# 주어진 노드의 값이 연결 리스트에 더 이상 존재하지 않아야 합니다.
# 연결 리스트의 노드 개수가 1개 줄어들어야 합니다.
# node 이전에 있던 값들은 기존 순서를 유지해야 합니다.
# node 이후에 있던 값들도 기존 순서를 유지해야 합니다.

# 커스텀 테스트
# 입력으로는 전체 연결 리스트 head와 삭제할 노드 node를 제공합니다.
# node는 리스트의 마지막 노드가 아니어야 하며, 실제로 리스트 안에 존재하는 노드여야 합니다.
# 테스트 시스템은 연결 리스트를 만든 뒤, 해당 node를 당신의 함수에 전달합니다.
# 출력은 당신의 함수를 호출한 뒤의 전체 연결 리스트입니다.

# 예제 1
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# 설명
# 값이 5인 두 번째 노드가 주어집니다.
# 함수를 호출한 뒤 연결 리스트는 다음과 같아야 합니다.
# 4 -> 1 -> 9

# 예제 2
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# 설명
# 값이 1인 세 번째 노드가 주어집니다.
# 함수를 호출한 뒤 연결 리스트는 다음과 같아야 합니다.
# 4 -> 5 -> 9

# 제약 조건
# 주어진 리스트의 노드 개수는 2 이상 1000 이하입니다.
# -1000 <= Node.val <= 1000
# 연결 리스트의 각 노드 값은 모두 고유합니다.
# 삭제할 노드는 리스트 안에 존재하며, 마지막 노드가 아닙니다.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # print('node', node)
        # node ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
        # 현재 노드를 삭제하는 법
        # d - a - b - c에서 b를 삭제해야한다면 a의 next를 c로 바꿔야 함
        # 근데 linked list의 head를 모르면 a를 찾을 수 없음
        # 이때 b를 c로 바꾸고, b의 next를 c의 next로 바꾸면 된다.
        node.val = node.next.val
        node.next = node.next.next
