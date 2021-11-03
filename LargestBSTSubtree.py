'''

-Medium-

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), 
where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10
   / \
  5  15
 / \   \
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?

'''


from BinaryTree import (null, TreeNode, constructBinaryTree)

class Solution:
    """
    @param root: the root
    @return: the largest subtree's size which is a Binary Search Tree
    """
    def largestBSTSubtree(self, root):
        # Write your code here
        MIN, MAX = -float('inf'), float('inf')
        res = [0]
        def helper(node):
            if not node: return (MAX, MIN, 0, True)
            lmin, lmax, lnum, lis = helper(node.left)
            rmin, rmax, rnum, ris = helper(node.right)
            if lmax <= node.val <= rmin and lis and ris:
                res[0] = max(res[0], lnum+rnum+1)
                return (min(node.val, lmin, rmin), max(node.val, lmax, rmax), lnum+rnum+1, True)
            else:
                return (min(node.val, lmin, rmin), max(node.val, lmax, rmax), lnum+rnum+1, False)
        helper(root)
        return res[0]




if __name__ == "__main__":
    root = constructBinaryTree([10,5,15,1,8,null,7])
    root.prettyPrint()
    print(Solution().largestBSTSubtree(root))
