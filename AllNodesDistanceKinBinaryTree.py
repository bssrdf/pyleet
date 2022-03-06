'''
-Medium-
*BFS*
*DFS*

Given the root of a binary tree, the value of a target node target, 
and an integer k, return an array of the values of all nodes that 
have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000


'''

from BinaryTree import (TreeNode, null, constructBinaryTree)
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict 

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        conn = defaultdict(list)
        def connection(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                connection(child, child.left)
            if child.right:
                connection(child, child.right)
        connection(None, root)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(k):
            new_bfs = []
            for node_val in bfs:
                for n_node_val in conn[node_val]:
                    if n_node_val not in seen:
                        new_bfs.append(n_node_val)
            bfs = new_bfs
            seen |= set(bfs)
        return bfs            
        



if __name__ == "__main__":
    root =  constructBinaryTree([3,5,1,6,2,0,8,null,null,7,4])
    root.prettyPrint()
    def findTarget(node, t):
        if not node:
           return None
        if node.val == t:
            return node
        return findTarget(node.left, t) or \
               findTarget(node.right, t)
    target = findTarget(root, 5)
    print(Solution().distanceK(root, target, 2))