'''
-Medium-



You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:


Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
Each node has a unique value.
A node with a value of start exists in the tree.


'''
from typing import Optional
from BinaryTree import TreeNode

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs1(node):
            if not node: return None
            if node.val == start:
                return node
            return dfs1(node.left) or dfs1(node.right)
        
        st = dfs1(root) # start node
        def dfs2(node):
            if not node: return 0
            l = dfs2(node.left) 
            r = dfs2(node.right)
            return 1+max(l, r)
        d1 = dfs2(st)-1 # max distance/depth from start node down
        d2 = 0 # max distance from start to the other side
        def dfs3(node):
            nonlocal d2
            if not node: return (0, -1)
            if node.val == start:
                return (0, 1)
            l1, l2 = dfs3(node.left) 
            r1, r2 = dfs3(node.right)
            if l2 == 1 or r2 == 1:
                d2 = max(d2, l1+1+r1)
                return (l1+1 if l2 == 1 else r1+1, 1)
            else:
                return (max(l1, r1)+1, -1)
        dfs3(root)
        return max(d2, d1)
        