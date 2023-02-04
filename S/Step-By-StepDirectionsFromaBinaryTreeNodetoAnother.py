'''
-Medium-

*DFS*


You are given the root of a binary tree with n nodes. Each node is uniquely assigned 
a value from 1 to n. You are also given an integer startValue representing the value 
of the start node s, and a different integer destValue representing the value of the 
destination node t.

Find the shortest path starting from node s and ending at node t. Generate 
step-by-step directions of such path as a string consisting of only the uppercase 
letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue


'''

from typing import Optional
from BinaryTree import (null, TreeNode, constructBinaryTree)
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, target, dir):
            if not node: return ''
            if node.val == target: 
                return dir
            lret = dfs(node.left, target, 'L')
            if lret: return dir+lret
            rret = dfs(node.right, target, 'R')
            if rret: return dir+rret            
            return ''
        start = dfs(root, startValue, '')
        dest = dfs(root, destValue, '')
        # print(start, '#', dest)
        i, j = 0, 0
        while i < len(start) and j < len(dest):            
            if start[i] != dest[j]:
                break
            i += 1
            j += 1
        return  'U'*(len(start)-i)+dest[j:]
    
    def getDirections2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, dir):
            if not node: return False, False, dir
            ls, ld, lpath = dfs(node.left, 'L')
            rs, rd, rpath = dfs(node.right, 'R')
            if node.val == startValue:
                if ld: return True, True, lpath 
                if rd: return True, True, rpath 
                return True, False, dir
            if node.val == destValue:
                if ls: return True, True, 'U'*len(lpath)
                if rs: return True, True, 'U'*len(rpath)
                return False, True, dir           
            if ls and ld: return ls, ld, lpath
            if rs and rd: return rs, rd, rpath
            if ls and rd: return ls, rd, 'U'*len(lpath)+rpath
            if rs and ld: return rs, ld, 'U'*len(rpath)+lpath
            if ls or ld: return ls, ld, dir+lpath
            if rs or rd: return rs, rd, dir+rpath
            return False, False, dir
        _, _, path = dfs(root, '')
        return path
            

        


        

        

if __name__=="__main__":
    root = constructBinaryTree([5,1,2,3,null,6,4])
    root.prettyPrint()
    print(Solution().getDirections(root, startValue = 3, destValue = 6))
    print(Solution().getDirections2(root, startValue = 3, destValue = 6))
    root = constructBinaryTree([2,1])
    print(Solution().getDirections(root, startValue = 2, destValue = 1))
    print(Solution().getDirections2(root, startValue = 2, destValue = 1))
    root = constructBinaryTree([1,2])
    print(Solution().getDirections(root, startValue = 2, destValue = 1))
    print(Solution().getDirections2(root, startValue = 2, destValue = 1))
    