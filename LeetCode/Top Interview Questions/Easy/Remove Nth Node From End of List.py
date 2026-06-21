# Remove Nth Node From End of List
#
# 연결 리스트의 head가 주어졌을 때, 끝에서 n번째 노드를 제거하고 head를 반환하라.
#
# 예제 1:
# 입력: head = [1,2,3,4,5], n = 2
# 출력: [1,2,3,5]
#
# 예제 2:
# 입력: head = [1], n = 1
# 출력: []
#
# 예제 3:
# 입력: head = [1,2], n = 1
# 출력: [1]
#
# 제약 조건:
# - 리스트의 노드 수는 sz이다.
# - 1 <= sz <= 30
# - 0 <= Node.val <= 100
# - 1 <= n <= sz
#
# 후속 질문: 한 번의 순회로 해결할 수 있는가?
#
# 힌트: 두 개의 포인터를 유지하고, 하나를 n 스텝만큼 지연시켜 업데이트하라.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(next=head)
        nth_node = dummy_node # nth_node를 head를 가리키는 더미 노드로 초기화시켜두고
        cur_node = head
        
        # 먼저 cur_node를 n만큼 이동시켜 nth_node가 cur_node로부터 n만큼 떨어져있게 한다.
        for i in range(n - 1):
            cur_node = cur_node.next
            
        # 이제 nth_node와 cur_node를 동시에 이동시키면서
        # cur_node가 tail이 될 때까지 이동시킨다.
        while cur_node.next:
            nth_node = nth_node.next
            cur_node = cur_node.next
        
        # cur_node가 tail이 되었다면 nth_node를 삭제한다.
        nth_node.next = nth_node.next.next

        return dummy_node.next