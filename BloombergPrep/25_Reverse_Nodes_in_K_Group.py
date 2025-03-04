"""
25. Reverse Nodes in k-Group
Hard

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

- The number of nodes in the list is n.
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start, temp = head, head

        def reverseList(root: Optional[ListNode], end: Optional[ListNode]):
            prev, curr, next = end, root, None


            while curr != end:
                next = curr.next
                curr.next = prev
                prev, curr = curr, next
            

            return prev

        head_replaced = False

        while temp:
            tail = start
            if head_replaced:
                start = start.next
            for i in range(k):
                if not temp:
                    return head
                temp = temp.next
            
            new_head = reverseList(start, temp)
            
            if not head_replaced:
                head = new_head
                head_replaced = True
            else:
                tail.next = new_head

        return head
