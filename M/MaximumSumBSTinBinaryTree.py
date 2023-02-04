'''

-Hard-

Given a binary tree root, return the maximum sum of all keys of any sub-tree 
which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104

'''
from BinaryTree import(null, TreeNode, constructBinaryTree)
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        MIN, MAX = -4*10**4-1, 4*10**4+1 
        ans = [0]
        def dfs(node):
            if not node.left and not node.right:
                ans[0] = max(ans[0], node.val)
                return [True, node.val, node.val, node.val]
            if node.left:
                lbst, lmin, lmax, lsum = dfs(node.left)
            else:
                lbst, lmin, lmax, lsum = True, MAX, MIN, 0 
            if node.right:    
                rbst, rmin, rmax, rsum = dfs(node.right)
            else:
                rbst, rmin, rmax, rsum = True, MAX, MIN, 0 
            sums = lsum + rsum + node.val              
            if lbst and rbst and lmax < node.val < rmin:                               
                ans[0] = max(ans[0], sums)
                if lmin == MAX: lmin = node.val                    
                if rmax == MIN: rmax = node.val                    
                return [True, lmin, rmax, sums]
            else:
                return [False, lmin, rmax, sums]            
        dfs(root) 
        return ans[0]


if __name__ == "__main__":
    root = constructBinaryTree([1,4,3,2,4,2,5,null,null,null,null,null,null,4,6])
    root.prettyPrint()
    print(Solution().maxSumBST(root))
    root = constructBinaryTree([4,3,null,1,2])
    root.prettyPrint()
    print(Solution().maxSumBST(root))
    root = constructBinaryTree([-4,-2,-5])
    root.prettyPrint()
    print(Solution().maxSumBST(root))
    root = constructBinaryTree([8,9,8,null,9,null,1, null, null, null, null, null,null,-3,5,null, null, null, null, null, null, null, null, null, null, null, null, null,-2,null,6])
    root.prettyPrint()
    print(Solution().maxSumBST(root))


