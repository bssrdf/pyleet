'''
-Easy-

Given a non-empty binary search tree and a target value, find the value in the BST that is 
closest to the target.

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Example1

Input: root = {5,4,9,2,#,8,10} and target = 6.124780
Output: 5
Explanation：
Binary tree {5,4,9,2,#,8,10},  denote the following structure:
        5
       / \
     4    9
    /    / \
   2    8  10
Example2

Input: root = {3,2,4,1} and target = 4.142857
Output: 4
Explanation：
Binary tree {3,2,4,1},  denote the following structure:
     3
    / \
  2    4
 /
1

'''
from BinaryTree import (null, TreeNode, constructBinaryTree)
import sys

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        a = root.val
        t = root.left if target < a else root.right
        if not t: return a
        b = self.closestValue(t, target)
        return a if abs(a - target) < abs(b - target)  b;
        '''
        def helper(node, mi, mx):
            if not node:
                if float(mi) < target < float(mx): 
                    return mi if target-float(mi) <= float(mx) - target else mx
                elif float(mi) < target: return mi
                else: return mx

            if float(node.val) <= target:
                return helper(node.right, node.val, mx)
            if float(node.val) > target:
                return helper(node.left, mi, node.val)
        return helper(root, sys.maxsize, -sys.maxsize)
        '''

if __name__ == "__main__":
    '''
    root = constructBinaryTree([5,4,9,2,null,8,10])
    root.prettyPrint()
    print(Solution().closestValue(root, 6.124780))
    root = constructBinaryTree([4,2,5,1,3])
    root.prettyPrint()
    print(Solution().closestValue(root, 3.124780))
    '''
    root = constructBinaryTree([2,1])
    root.prettyPrint()
    print(Solution().closestValue(root, 2147483647.0))

