'''
-Hard-
*Inorder Traversal*

Given a non-empty binary search tree and a target value, find  k  values in the BST 
that are closest to the target.

Note:

Given target value is a floating point.
You may assume  k  is always valid, that is:  k ≤ total nodes.
You are guaranteed to have only one unique set of  k  values in the BST that are closest 
to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and _k_ = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than  O ( n ) runtime 
(where  n  = total nodes)?

'''
from BinaryTree import (null, TreeNode, constructBinaryTree)
from collections import deque
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        #res = []
        res = deque()
        def inorder(root):
            if not root: return
            inorder(root.left)
            if len(res) < k: res.append(root.val)
            elif abs(root.val - target) < abs(res[0]-target):
                res.popleft()
                res.append(root.val)
            else: return # if the current node is further away, its right 
                         # subtree will be ever further, so no need to go down
            inorder(root.right)
        inorder(root)
        return res

if __name__ == "__main__":
    root = constructBinaryTree([4,2,5,1,3])
    root.prettyPrint()
    print(Solution().closestKValues(root, 3.710, 2))