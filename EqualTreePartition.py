'''
-Medium-

Given a binary tree with n nodes, your task is to check if it's possible to 
partition the tree to two trees which have the equal sum of values after 
removing exactly one edge on the original tree.

Example 1:

Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
 

Example 2:

Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after 
removing exactly one edge on the tree.
 

Note:

The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000

'''

from BinaryTree import (null, constructBinaryTree, TreeNode)
from collections import defaultdict

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        m = defaultdict(int)
        def helper(node):
            # recursively compute sum of the node's val and its subtree
            if not node: return 0                        
            left = helper(node.left)
            right = helper(node.right)            
            cur = node.val + left + right
            m[cur] += 1
            return cur
        sm = helper(root)
        if sm == 0: return m[0] > 1
        # if one subtree has ever had a sum = 1/2 of the total (total is an even number)
        # we can split this subtree from its parent to statisfy the requirement   
        return sm % 2 == 0 and sm//2 in m 


if __name__=="__main__":
    root = constructBinaryTree([5, 10, 10, null, null, 2, 3])
    root.prettyPrint()
    print(Solution().checkEqualTree(root))
    root = constructBinaryTree([1, 2, 10, null, null, 2, 20])
    root.prettyPrint()
    print(Solution().checkEqualTree(root))
    root = constructBinaryTree([0, 1, -1])
    root.prettyPrint()
    print(Solution().checkEqualTree(root))
