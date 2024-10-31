# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        stack = []
        while current:
            stack.append(current.val)
            current = current.next
        current = head
        while current:
            data = stack.pop()
            if current.val != data:
                return False
            current = current.next
        return True