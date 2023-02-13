'''
-Medium-
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow 
a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according 
to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 10^5].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
p != q
p and q will exist in the tree.

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
    