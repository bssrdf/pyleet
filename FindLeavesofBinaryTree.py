'''

-Medium-

Given a binary tree, collect a tree's nodes as if you were doing this: 
Collect and remove all leaves, repeat until the tree is empty.

Example:
Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]

Explanation:
1. Removing the leaves [4,5,3] would result in this tree:
          1
         / 
        2          

2. Now removing the leaf [2] would result in this tree:
          1          

3. Now removing the leaf [1] would result in the empty tree:
          []         

'''

from BinaryTree import (null, TreeNode, constructBinaryTree)

class Solution(object):
    def findLeaves(self, root):
        """
        type root: TreeNode
        rtype: List[List[int]]
        """
        res = []
        def helper(root, leaves):
            if not root: return None
            if not root.left and not root.right:
                leaves.append(root.val)
                return None
            root.left = helper(root.left, leaves)
            root.right = helper(root.right, leaves)
            return root
        while root:
            leaves = []
            root = helper(root, leaves)
            res.append(leaves)
        return res


if __name__ == "__main__":
    root = constructBinaryTree([1,2,3,4,5])
    root.prettyPrint()    
    print(Solution().findLeaves(root))
