'''

-Medium-

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and 
all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes 
inclusive at the last level h.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and 
all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, constructBinaryTree, TreeNode)
from collections import deque

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = deque([root])
        lev = 0
        while q:
            nxt = deque()
            filled = True
            n = len(q)            
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    if not filled: return False
                    nxt.append(node.left)
                else:
                    filled = False
                if node.right:
                    if not filled: return False
                    nxt.append(node.right)
                else:
                    filled = False
            if nxt and n != 2**lev: return False 
            q = nxt
            lev += 1
        return True

    def isCompleteTreeAC(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        '''
        for j in range(len(bfs)):
            if j >= i: 
                print('##', j, bfs[j])
            else:
                print('  ', j, bfs[j])
        '''    
        return not any(bfs[i:])
        
                
                
                 

if __name__ == "__main__":
    root = constructBinaryTree([1,2,3,4,5])
    root.prettyPrint()
    print(Solution().isCompleteTree(root))
    print(Solution().isCompleteTreeAC(root))
    root = constructBinaryTree([1,2,3,4,null,null,7])
    root.prettyPrint()
    print(Solution().isCompleteTree(root))
    root = constructBinaryTree([1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15])
    root.prettyPrint()
    print(Solution().isCompleteTree(root))
    print(Solution().isCompleteTreeAC(root))

