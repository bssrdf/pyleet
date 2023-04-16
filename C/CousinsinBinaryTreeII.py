'''

-Medium-
*BFS*

Given the root of a binary tree, replace the value of each node in the tree with the sum of all its cousins' values.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Return the root of the modified tree.

Note that the depth of a node is the number of edges in the path from the root node to it.

 

Example 1:


Input: root = [5,4,9,1,10,null,7]
Output: [0,0,0,7,7,null,11]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 5 does not have any cousins so its sum is 0.
- Node with value 4 does not have any cousins so its sum is 0.
- Node with value 9 does not have any cousins so its sum is 0.
- Node with value 1 has a cousin with value 7 so its sum is 7.
- Node with value 10 has a cousin with value 7 so its sum is 7.
- Node with value 7 has cousins with values 1 and 10 so its sum is 11.
Example 2:


Input: root = [3,1,2]
Output: [0,0,0]
Explanation: The diagram above shows the initial binary tree and the binary tree after changing the value of each node.
- Node with value 3 does not have any cousins so its sum is 0.
- Node with value 1 does not have any cousins so its sum is 0.
- Node with value 2 does not have any cousins so its sum is 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 104



'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        que = [root]
        sums = []
        while que:
            nq = deque()
            t = 0
            for _ in range(len(que)):
                node = que.popleft()
                t += node.val
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            sums.append(t)
            que = nq
        que = [root]
        l = 1
        while que:
            nq = deque()
            for _ in range(len(que)):
                node = que.popleft()
                s += node.left.val if node.left else 0
                s += node.right.val if node.right else 0
                if node.left: 
                    node.left.val = sums[l] - s
                    nq.append(node.left)
                if node.right: 
                    node.right.val = sums[l] - s
                    nq.append(node.right)
            l += 1
            que = nq
        return root

                





        





        
