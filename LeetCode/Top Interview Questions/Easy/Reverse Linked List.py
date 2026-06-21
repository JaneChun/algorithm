# Reverse Linked List
#
# 단일 연결 리스트의 head가 주어졌을 때, 리스트를 뒤집고 뒤집은 리스트를 반환하라.
#
# 예제 1:
# 입력: head = [1,2,3,4,5]
# 출력: [5,4,3,2,1]
#
# 예제 2:
# 입력: head = [1,2]
# 출력: [2,1]
#
# 예제 3:
# 입력: head = []
# 출력: []
#
# 제약 조건:
# - 리스트의 노드 수는 [0, 5000] 범위이다.
# - -5000 <= Node.val <= 5000
#
# 후속 질문: 연결 리스트는 반복적으로 또는 재귀적으로 뒤집을 수 있다. 둘 다 구현할 수 있는가?

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head에서 tail로 이동하며 next에 cur.next를 저장해두고 cur.next를 prev으로 바꾼다? -> O(N)
        # 원본:  1 → 2 → 3 → 4 → 5 → None
        # 결과:  None ← 1 ← 2 ← 3 ← 4 ← 5
        
        # 빈 리스트이거나 노드가 1개인 경우 그대로 리턴
        if not head or not head.next:
            return head
        
        prev_node = None
        cur_node = head
        next_node = head.next
        
        while cur_node: # None이 되면 종료
            next_node = cur_node.next # 1. 다음 노드를 저장해두고
            cur_node.next = prev_node # 2. 현재 노드가 이전 노드를 가리키게 업데이트
            prev_node = cur_node # 3. 현재 노드를 이전 노드로 저장하고
            cur_node = next_node # 다음 노드로 이동
            
        return prev_node