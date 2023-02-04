'''
-Medium-

You have a binary tree with a small defect. There is exactly one invalid node where its 
right child incorrectly points to another node at the same depth but to the invalid 
node's right.

Given the root of the binary tree with this defect, root, return the root of the binary 
tree after removing this invalid node and every node underneath it (minus the node 
it incorrectly points to).

Custom testing:

The test input is read as 3 lines:

TreeNode root
int fromNode (not available to correctBinaryTree)
int toNode (not available to correctBinaryTree)
After the binary tree rooted at root is parsed, the TreeNode with value of fromNode 
will have its right child pointer pointing to the TreeNode with a value of toNode. 
Then, root is passed to correctBinaryTree.

 

Example 1:



Input: root = [1,2,3], fromNode = 2, toNode = 3
Output: [1,null,3]
Explanation: The node with value 2 is invalid, so remove it.
Example 2:



Input: root = [8,3,1,7,null,9,4,2,null,null,null,5,6], fromNode = 7, toNode = 4
Output: [8,3,1,null,null,9,4,null,null,5,6]
Explanation: The node with value 7 is invalid, so remove it and the node underneath it, node 2.
 

Constraints:

The number of nodes in the tree is in the range [3, 10^4].
-10^9 <= Node.val <= 10^9
All Node.val are unique.
fromNode != toNode
fromNode and toNode will exist in the tree and will be on the same depth.
toNode is to the right of fromNode.
fromNode.right is null in the initial tree from the test data.

'''
from BinaryTree import (null, TreeNode, constructBinaryTree)
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def correctBinaryTreeLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        Q = deque([root])
        remove = None
        while Q:                        
            nxt = deque()
            n = len(Q)
            m = {}
            for i in range(n):
                node = Q.popleft()
                if node.left:
                   nxt.append(node.left)
                if node.right:
                   nxt.append(node.right)                   
            #if len(nxt) > 1:
            for i in range(len(nxt)):
                if nxt[i] in m: 
                    remove = m[nxt[i]]
                    break
                m[nxt[i].right] = nxt[i]
            Q = nxt
            if remove: break

        def sever(root, delete):
            if not root: return
            if root.left == delete:
                root.left.right = None
                root.left = None
            if root.right == delete:
                root.right.right = None
                root.right = None
            sever(root.left, delete)
            sever(root.right, delete)
        print(remove.val)
        sever(root, remove)
        return root
    
    def __init__(self):
        self.visited = set() 

    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if root.right and root.right.val in self.visited: return None
        self.visited.add(root.val)
        root.right = self.correctBinaryTree(root.right)
        root.left = self.correctBinaryTree(root.left)
        return root
                


if __name__=="__main__":
    root = constructBinaryTree([8,3,1,7,null,9,4,2,null,null,null,null,null,5,6])
    root.prettyPrint()
    seven, four = None, None
    def helper(root, val):
        if not root: return None
        if root.val == val: 
            return root         
        return helper(root.left, val) or helper(root.right, val)
        
    seven = helper(root, 7)
    four = helper(root, 4)
    seven.right = four
    root = Solution().correctBinaryTree(root)
    root.prettyPrint()


