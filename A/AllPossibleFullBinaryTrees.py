'''

-Medium-

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20




'''
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def clone(self, tree: TreeNode) -> TreeNode:
        if not tree:
            return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        elif n == 1:
            return [TreeNode(0)]
        ret = []
        for i in range(2, n + 1, 2):
            left_branch = self.allPossibleFBT(i - 1)
            right_branch = self.allPossibleFBT(n - i)
            for left_count, left in enumerate(left_branch, 1):
                for right_count, right in enumerate(right_branch, 1):
                    tree = TreeNode(0)
                
                    # If we're using the last right branch, then this will be the last time this left branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.left = self.clone(left) if right_count < len(right_branch) else left
                    
                    # If we're using the last left branch, then this will be the last time this right branch is used and can hence
                    # be shallow copied, otherwise the tree will have to be cloned
                    tree.right = self.clone(right) if left_count < len(left_branch) else right
                    
                    ret.append(tree)
        return ret
        
        


        

if __name__ == "__main__":
    roots = Solution().allPossibleFBT(7)