# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 포인터A는 listA 끝까지 순회한 후 listB의 시작점으로 이동
# 포인터B는 listB 끝까지 순회한 후 listA의 시작점으로 이동
# -> 둘의 길이가 맞춰지며 같은 intersect node를 가리키게 된다.

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB: # 같은 노드를 찾거나 둘다 None이 될 때까지 반복
            # 아니면 포인터 이동
            pointerA = pointerA.next if pointerA else headB # None이면 상대리스트 헤드로 이동
            pointerB = pointerB.next if pointerB else headA

        return pointerA
        