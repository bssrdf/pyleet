'''

-Hard-

*Greedy*

Given a binary tree, we install cameras on the nodes of the tree. 

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, constructBinaryTree, TreeNode)
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        # Return 0 if leaf, 1 if parent of leaf with camera on this node, 
        # 2 if covered without camera on this node.
        self.res = 0
        def helper(node):
            if not node: return 2 # null node, return 2 to mark 
            left = helper(node.left)
            right = helper(node.right)
            if left == 0 or right == 0: # one or both of childdren are leafs, put a camera
                self.res += 1
                return 1
            return 2 if left == 1 or right == 1 else 0 # this node is covered by one 
                                                       # of children having the camera
                                                       # or this node is a leaf (left=2, right=2)
        return (1 if helper(root) < 1 else 0) + self.res # if root is also a leaf, put one camera
    

if __name__ == "__main__":
    root = constructBinaryTree([0,0,null,0,null,null,null,0,null,null,null,null, null,null,null,null,0])
    root.prettyPrint()
    print(Solution().minCameraCover(root))

