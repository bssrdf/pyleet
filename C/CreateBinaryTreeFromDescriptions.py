'''
-Medium-
*Hash Table*

You are given a 2D integer array descriptions where descriptions[i] = 
[parenti, childi, isLefti] indicates that parenti is the parent of childi 
in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.


'''

from typing import List, Optional
from BinaryTree import (null, TreeNode)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        m, roots = {}, set()
        def conn_child(par, chi, left):
            if left == 0: par.right = chi
            else: par.left = chi
        for vpar,vchi,left in descriptions:
            if vpar in m:                
                if vchi not in m:
                    m[vchi] = TreeNode(vchi)
            elif vchi in m:
                m[vpar] = TreeNode(vpar)
            else:
                m[vchi] = TreeNode(vchi)
                m[vpar] = TreeNode(vpar)                                
            conn_child(m[vpar], m[vchi], left)
            roots.add(vchi)
        for vpar,_,_ in descriptions:
            if vpar not in roots:
                return m[vpar]
        return None
                 




        
if __name__=="__main__":
    root = Solution().createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
    root.prettyPrint()
    root = Solution().createBinaryTree([[1,2,1],[2,3,0],[3,4,1]])
    root.prettyPrint()
    root = Solution().createBinaryTree([[85,82,1],[74,85,1],[39,70,0],[82,38,1],[74,39,0],[39,13,1]])
    root.prettyPrint()
    