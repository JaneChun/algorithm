# Merge Two Sorted Lists
#
# 두 개의 정렬된 연결 리스트 list1과 list2의 head가 주어진다.
#
# 두 리스트를 하나의 정렬된 리스트로 병합하라.
# 리스트는 두 리스트의 노드를 이어 붙여서 만들어야 한다.
#
# 병합된 연결 리스트의 head를 반환하라.
#
# 예제 1:
# 입력: list1 = [1,2,4], list2 = [1,3,4]
# 출력: [1,1,2,3,4,4]
#
# 예제 2:
# 입력: list1 = [], list2 = []
# 출력: []
#
# 예제 3:
# 입력: list1 = [], list2 = [0]
# 출력: [0]
#
# 제약 조건:
# - 두 리스트의 노드 수는 [0, 50] 범위이다.
# - -100 <= Node.val <= 100
# - list1과 list2 모두 오름차순으로 정렬되어 있다.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode() # 정렬된 값을 저장할 새 리스트의 시작 노드(head)
        cur_node = dummy_node

        while list1 and list2: # list1, list2가 None이 될 때까지 반복(리스트의 끝까지 갈 때까지)
            if list1.val <= list2.val: # list1이 더 작은 경우
                cur_node.next = list1 # cur_node에 list1을 이어붙이고
                list1 = list1.next # list1 포인터를 다음 노드로 이동
            else: # list2가 더 작은 경우
                cur_node.next = list2
                list2 = list2.next
            
            cur_node = cur_node.next # cur_node의 포인터도 다음 노드로 이동

        # 남은 리스트 이어붙이기
        if list1:
            cur_node.next = list1
            
        if list2:
            cur_node.next = list2

        return dummy_node.next