'''
-Medium-

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, 
column by column).

If two nodes are in the same row and column, the order should be from left to right.

样例
Example1

Inpurt:  {3,9,20,#,#,15,7}
Output: [[9],[3,15],[20],[7]]
Explanation:
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
Example2

Input: {3,9,8,4,0,1,7}
Output: [[4],[9],[3,0,1],[8],[7]]
Explanation:
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7


'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from BinaryTree import (null, TreeNode, constructBinaryTree)

from collections import (defaultdict, deque)

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        vPosToVals = defaultdict(list)

        leftMost  = 0   # the known minimum vertical position
        rightMost = -1  # the known maximum vertical position

        queue = deque() # each item is a pair (node, verticalPosition)
        if root:
            queue.append( (root,0) )
            leftMost = 0
            rightMost = 0

        while queue:
            node, vPos = queue.popleft()
            vPosToVals[vPos].append( node.val )

            if node.left:
                queue.append( (node.left, vPos-1) )
                leftMost = min(leftMost, vPos-1)
            if node.right:
                queue.append( (node.right, vPos+1) )
                rightMost = max(rightMost, vPos+1)

        ret = []
        for pos in range(leftMost, rightMost+1):
            ret.append( vPosToVals[pos] )

        return ret

if __name__=="__main__":
    root = constructBinaryTree([3,9,20,null,null,15,7])
    root.prettyPrint()
    print(Solution().verticalOrder(root))