'''
-Medium-

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. 
If either node p or q does not exist in the tree, return null. All values of the nodes in the 
tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p 
and q in a binary tree T is the lowest node that has both p and q as descendants (where we 
allow a node to be a descendant of itself)". A descendant of a node x is a node y that 
is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q


'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, p, q):
        # write your code here
        if not self.traverse(root, p) or not self.traverse(root, q):
            return None
        return self.helper(root, p, q)
    
    def helper(self, node, p, q):
        if node == None or node == p or node == q:
            return node
        
        left = self.helper(node.left, p, q)
        right = self.helper(node.right, p, q)
        
        if left != None and right != None:
            return node
        
        if left != None:
            return left
        
        if right != None:
            return right
        
        return None
        
    def traverse(self, node, p):
        if not node:
            return False
            
        if node == p:
            return True
            
        left = self.traverse(node.left, p)
        right = self.traverse(node.right, p)
        return left or right
        

