# difficulty: Medium
# Runtime: 1982 ms, faster than 74.57% of Python3 online submissions for Delete the Middle Node of a Linked List.
# Memory Usage: 60.6 MB, less than 86.32% of Python3 online submissions for Delete the Middle Node of a Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oneStep, twoStep = head, head
        prevNode = None

        while twoStep and twoStep.next:
            prevNode = oneStep
            oneStep = oneStep.next
            twoStep = twoStep.next
            if twoStep:
                twoStep = twoStep.next

        if prevNode == None:
            return None

        prevNode.next = oneStep.next

        return head
