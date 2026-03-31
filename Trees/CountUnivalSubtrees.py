# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/count-univalue-subtrees/editorial/
# T(C) - o(n), S(C) - o(n)
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def helper (node):
            if not node:
                return True

            leftUnival = helper (node.left)
            rightUnival = helper (node.right)

            if leftUnival and rightUnival:
                if node.left and node.val!= node.left.val:
                    return False
                if node.right and node.val!= node.right.val:
                    return False
                self.count += 1
                return True

            return False    

        helper (root)
        return self.count        
