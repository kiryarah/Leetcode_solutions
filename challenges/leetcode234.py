'''
    https://leetcode.com/problems/palindrome-linked-list/
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next

        return True


head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(Solution().isPalindrome(head))
