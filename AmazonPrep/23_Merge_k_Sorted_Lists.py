"""
23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if not node:
                continue
            heapq.heappush(heap, (node.val, i))

        def getSmallestNode():
            if not heap:
                return -1
            smallest = heapq.heappop(heap)
            return smallest[1] if smallest else -1

        def attachNode(curr: ListNode, index: int) -> ListNode:
            if index == -1:
                return None
            node = lists[index]
            next_node = curr.next
            if node and node.next:
                lists[index] = node.next
                heapq.heappush(heap, (node.next.val, index))
            if node: 
                node.next = next_node
            curr.next = node

            return node
        
        dummy_head = ListNode()
        curr = dummy_head
        
        while lists:
            curr = attachNode(curr, getSmallestNode())
            if not curr:
                return dummy_head.next

        return dummy_head.next
