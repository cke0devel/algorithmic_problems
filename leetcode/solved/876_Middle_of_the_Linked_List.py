# difficulty: Easy
# Runtime: 30 ms, faster than 88.33% of Python3 online submissions for Middle of the Linked List.
# Memory Usage: 13.8 MB, less than 57.14% of Python3 online submissions for Middle of the Linked List.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oneStep, twoStep = head, head

        while twoStep and twoStep.next:
            oneStep = oneStep.next
            twoStep = twoStep.next
            if twoStep:
                twoStep = twoStep.next

        return oneStep
