#

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        def toInteger(node: ListNode):
            cur_node = node
            result = 0
            place_value = 1

            while cur_node.next:
                result += cur_node.val * place_value
                place_value *= 10
                cur_node = cur_node.next
            
            result += cur_node.val * place_value # 마지막 노드 처리
            
            return result
        
        sum = toInteger(l1) + toInteger(l2)
        arr = [int(x) for x in str(sum)]
        prev = ListNode((arr[0]))

        for i in range(1, len(arr)):
            val = arr[i]
            prev = ListNode(val, prev)

        return prev


