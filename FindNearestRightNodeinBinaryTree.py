'''

-Medium-
*BFS*


Given the root of a binary tree and a node u in the tree, return the nearest node on the same level that is to the right of u, or return null if u is the rightmost node in its level.

 

Example 1:



Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.
Example 2:



Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All values in the tree are distinct.
u is a node in the binary tree rooted at root.

'''

from typing import Optional
from BinaryTree import (TreeNode, constructBinaryTree, null) 
from collections import deque
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        que = deque([root])
        while que:
            nq = deque()
            see = False
            for i in range(len(que)):
                node = que.popleft()
                if node == u:
                    if i == len(que)-1:
                        return None
                    see = True
                elif see:
                    return node
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            que = nq
        return None


if __name__ == "__main__":   
    root = constructBinaryTree([1,2,3,null,4,5,6])
    u = root.left.right
    ret = Solution().findNearestRightNode(root, u)
    print(ret.val)
    u = root.right.left
    ret = Solution().findNearestRightNode(root, u)
    if ret:
        print(ret.val)
    else:
        print('Null')
    u = root.right.right
    ret = Solution().findNearestRightNode(root, u)
    if ret:
        print(ret.val)
    else:
        print('Null')