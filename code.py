class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        return helper(root, -inf, inf)


'''
set a range (at first we set it to (-infinity, infinity)
see if every node is in their own range
'''
