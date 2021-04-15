'''

-Medium-

Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next 
node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, TreeNode, constructBinaryTree)

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node.left and not node.right:
                return node            
            elif not node.left:
                right = helper(node.right)                
                return right
            elif not node.right:
                left = helper(node.left)
                node.right = node.left
                node.left = None
                return left 
            left = helper(node.left)
            right = helper(node.right)
            left.right = node.right
            node.right = node.left
            node.left = None
            return right
        if not root: return None
        helper(root)
        return root

    def flattenClean(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 93% 
        def helper(node):
            if not node: return None
            left = helper(node.left)
            right = helper(node.right)
            if not left and not right:
                return node
            elif not left:                 
                return right
            elif not right:
                node.right = node.left
                node.left = None
                return left
            left.right = node.right
            node.right = node.left
            node.left = None
            return right
        helper(root)
        return root



if __name__ == "__main__":
    root = constructBinaryTree([1,2,5,3,4,null,6])
    root.prettyPrint()
    #node = Solution().flatten(root)
    node = Solution().flattenClean(root)
    while node:
        assert node.left is None
        print(node.val,'->', end='')
        node = node.right
    print()