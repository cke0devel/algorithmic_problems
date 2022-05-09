# difficulty: Easy
# Runtime: 54 ms, faster than 42.70% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 13.9 MB, less than 33.49% of Python3 online submissions for Merge Two Sorted Lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        node = head

        while list1 or list2:
            if (list1 and not list2) or (list1 and list1.val <= list2.val):
                node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                list2 = list2.next

            node = node.next

        return head.next

