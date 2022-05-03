# difficulty: Medium
# Runtime: 53 ms, faster than 32.52% of Python3 online submissions for Remove Nth Node From End of List.
# Memory Usage: 13.8 MB, less than 98.34% of Python3 online submissions for Remove Nth Node From End of List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        l = 0

        while head:
            l += 1
            head = head.next

        return l


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = self.getLength(head)

        prev = None
        node = head
        for _ in range(l-n):
            prev = node
            node = node.next

        if prev == None:
            if head.next == None:
                return None
            else:
                return head.next

        prev.next = node.next

        return head

