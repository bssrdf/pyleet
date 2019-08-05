'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.val)
    
def traverse(root):
    current_level = [root]
    while current_level:
        print(' '.join(str(node) for node in current_level))
        next_level = list()
        for n in current_level:
            if n.left:
                next_level.append(n.left)
            if n.right:
                next_level.append(n.right)
            current_level = next_level

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None, p, q): return root
        (left, right) = (self.lowestCommonAncestor(root.left, p, q),
                         self.lowestCommonAncestor(root.right, p, q))
        return root if left and right else left or right
                                                                                    

if __name__ == "__main__":
    root=TreeNode(2)
    root.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.left.right.right = TreeNode(9)
    root.left.right.right.left = TreeNode(10)
    p = root.left.right.right.left
    root.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(6)    
    q = root.left.left.left 
    traverse(root)
    print(Solution().lowestCommonAncestor(root,p,q).val)
    
