'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
ans = 0
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def depth(p):
          if not p: return 0
          left, right = depth(p.left), depth(p.right)
          self.ans = max(self.ans, left+right)
          return 1 + max(left, right)
                                                                                    
        depth(root)
        return self.ans

    def diameterOfBinaryTree2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def depth(p):
            global ans
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            #ans = max(ans, left+right)
            if ans < left+right:
                ans = left + right
            return 1 + max(left, right)
                                                                                    
        depth(root)
        return ans

if __name__ == "__main__":
    root=TreeNode(2)
    root.left = TreeNode(4)
    root.left.right = TreeNode(7)
    root.left.right.right = TreeNode(9)
    root.left.right.right.left = TreeNode(10)
    root.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(6)    
    print(Solution().diameterOfBinaryTree(root))
    print(Solution().diameterOfBinaryTree2(root))
    
