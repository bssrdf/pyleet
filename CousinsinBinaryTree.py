'''
-Easy-

Given the root of a binary tree with unique values and the values of two different nodes 
of the tree x and y, return true if the nodes corresponding to the values x and y in 
the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k 
node are at the depth k + 1.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.

'''

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        px, py = [None], [None]
        hx, hy = [0], [0]
        def helper(node, par, h, v, p, ht):
            if not node: return
            if node.val == v:
                p[0] = par; ht[0] = h  
                return
            helper(node.left, node, h+1, v, p, ht)
            helper(node.right, node, h+1, v, p, ht)
        helper(root, None, 1, x, px, hx)
        helper(root, None, 1, y, py, hy)
        return hx[0] == hy[0] and px[0] != py[0]