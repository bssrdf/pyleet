'''

-Medium-

*Binary Tree*

Given a binary tree where node values are digits from 1 to 9. A path in the 
binary tree is said to be pseudo-palindromic if at least one permutation of 
the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to 
leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are 
three paths going from the root node to leaf nodes: the red path [2,3,3], 
the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are 
three paths going from the root node to leaf nodes: the green path [2,1,1], 
the path [2,1,3,1], and the path [2,1]. Among these paths only the green 
path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] 
(palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The given binary tree will have between 1 and 10^5 nodes.
Node values are digits from 1 to 9.


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (constructBinaryTree, TreeNode, null)

class Solution(object):
    def pseudoPalindromicPaths (self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(root, m):
            if root.val in m: m[root.val] += 1
            else: m[root.val] = 1
            if not root.left and not root.right:                
                odd = 0
                for k in m.values():                    
                    if k%2 != 0: odd +=1
                if odd <= 1: self.res += 1                
                m[root.val] -= 1
                if m[root.val] == 0: m.pop(root.val)
                return            
            if root.left:  helper(root.left, m)
            if root.right: helper(root.right, m) 
            # dict is mutable, so when backtracking, need to 
            # erase the current node's value
            m[root.val] -= 1
            if m[root.val] == 0: m.pop(root.val)
            return
             
        helper(root, {})
        return self.res

if __name__ == "__main__":
    root = constructBinaryTree([2,3,1,3,1,null,1])
    root.prettyPrint()
    print(Solution().pseudoPalindromicPaths(root))