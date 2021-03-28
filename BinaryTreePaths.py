# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def helper(node, path):
            if (not node.left) and (not node.right):
                res.append(path+str(node.val))
                return
            if node.left:
                helper(node.left, path+str(node.val)+'->')
            if node.right:
                helper(node.right, path+str(node.val)+'->')
        helper(root, '') 
        return res