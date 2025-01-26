"""
199. Binary Tree Right Side View
Medium
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([(root, 0)])

        ret = []

        curr_level = 0

        while queue:
            curr, level = queue.popleft()

            if level == curr_level:
                ret.append(curr.val)
                curr_level += 1

            if curr.right:
                queue.append((curr.right, level + 1))
            if curr.left:
                queue.append((curr.left, level + 1))
            
        return ret
