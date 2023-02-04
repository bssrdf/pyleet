'''
-Medium-

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. 
There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may 
be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
Example 3:


Input: root = [1,0,2]
Output: 2
Example 4:


Input: root = [1,0,0,null,3]
Output: 4
 

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, TreeNode, constructBinaryTree)

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        We traverse childs first (post-order traversal), and return the ballance of coins. For example, 
        if we get '+3' from the left child, that means that the left subtree has 3 extra coins to move out. 
        If we get '-1' from the right child, we need to move 1 coin in. So, we increase the number of moves 
        by 4 (3 moves out left + 1 moves in right). We then return the final ballance: 
        r->val (coins in the root) + 3 (left) + (-1) (right) - 1 (keep one coin for the root).
        """
        res = [0]
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] += abs(left) + abs(right)
            return left+right+node.val-1
        dfs(root)
        return res[0]
if __name__ == "__main__": 
    root = constructBinaryTree([3,0,0])
    print(Solution().distributeCoins(root))
    root = constructBinaryTree([1,0,0,null,3])
    root.prettyPrint()
    print(Solution().distributeCoins(root))
    root = constructBinaryTree([2,0,0,null,3,null,0])
    root.prettyPrint()
    print(Solution().distributeCoins(root))
