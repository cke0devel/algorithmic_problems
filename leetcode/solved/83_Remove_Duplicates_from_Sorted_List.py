# difficulty: Easy
# Runtime: 44 ms, faster than 87.23% of Python3 online submissions for Remove Duplicates from Sorted List.
# Memory Usage: 13.9 MB, less than 81.40% of Python3 online submissions for Remove Duplicates from Sorted List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

