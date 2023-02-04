'''
-Easy-

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and return the root node of this tree.

The size of the given array will be in the range of [1,1000].

样例
Example 1:

Input: {3,2,1,6,0,5}
Output: Return the tree root node representing the following tree:
     6
   /   \
  3     5
   \   / 
    2 0   
     \
      1
Example 2:

Input: {1,2,3,4}
Output: Return the tree root node representing the following tree:
        4
       /
      3
     /
    2
   /
  1    
标签
企业
Microsoft


'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from BinaryTree import (null, TreeNode)
from collections import deque
class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        if not nums: return None
        mx, idx = 0, 0
        for i in range(len(nums)):
            if nums[i] > mx:
                mx = nums[i]
                idx = i 
        root = TreeNode(nums[idx])
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root
    


if __name__ == "__main__":
    root = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
    root.prettyPrint()
    root = Solution().constructMaximumBinaryTree([1,2,3,4])
    root.prettyPrint()
            
        



