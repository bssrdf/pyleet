'''
-Medium-

Given two binary search trees, return True if and only if there is a node in the first tree and 
a node in the second tree whose values sum up to a given integer target.

 

Example 1:



Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:



Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false
 

Constraints:

Each tree has at most 5000 nodes.
-10^9 <= target, node.val <= 10^9

Hints

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (null, constructBinaryTree, TreeNode)

class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        s = set()
        def helper(node):
            if not node: return
            s.add(node.val)
            helper(node.left)
            helper(node.right)
        def check(node):
            if not node: return False
            if target - node.val in s: return True
            return check(node.left) or check(node.right)
        helper(root1)
        return check(root2)

    def twoSumBSTsIterative(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        stack = []
        s = set()
        while stack or root1:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            s.add(target - root1.val)
            root1 = root1.right
        while stack or root2:
            while root2:
                stack.append(root2)
                root2 = root2.left                
            root2 = stack.pop()
            if root2.val in s: return True
            root2 = root2.right
        return False
                    

            




if __name__ == "__main__":
    root1 = constructBinaryTree([2,1,4])
    root2 = constructBinaryTree([1,0,3])
    print(Solution().twoSumBSTs(root1, root2, 5))
    print(Solution().twoSumBSTsIterative(root1, root2, 5))
    root1 = constructBinaryTree([0,-10,10])
    root2 = constructBinaryTree([5,1,7,0,2])
    print(Solution().twoSumBSTs(root1, root2, 18))
    print(Solution().twoSumBSTsIterative(root1, root2, 18))
