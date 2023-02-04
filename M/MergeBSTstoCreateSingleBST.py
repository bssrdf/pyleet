'''

-Hard-

You are given n BST (binary search tree) root nodes for n separate BSTs stored in an array trees (0-indexed). Each BST in trees has at most 3 nodes, and no two roots have the same value. In one operation, you can:

Select two distinct indices i and j such that the value stored at one of the leaves of trees[i] is equal to the root value of trees[j].
Replace the leaf node in trees[i] with trees[j].
Remove trees[j] from trees.
Return the root of the resulting BST if it is possible to form a valid BST after performing n - 1 operations, or null if it is impossible to create a valid BST.

A BST (binary search tree) is a binary tree where each node satisfies the following property:

Every node in the node's left subtree has a value strictly less than the node's value.
Every node in the node's right subtree has a value strictly greater than the node's value.
A leaf is a node that has no children.

 

Example 1:


Input: trees = [[2,1],[3,2,5],[5,4]]
Output: [3,2,5,1,null,4]
Explanation:
In the first operation, pick i=1 and j=0, and merge trees[0] into trees[1].
Delete trees[0], so trees = [[3,2,5,1],[5,4]].

In the second operation, pick i=0 and j=1, and merge trees[1] into trees[0].
Delete trees[1], so trees = [[3,2,5,1,null,4]].

The resulting tree, shown above, is a valid BST, so return its root.
Example 2:


Input: trees = [[5,3,8],[3,2,6]]
Output: []
Explanation:
Pick i=0 and j=1 and merge trees[1] into trees[0].
Delete trees[1], so trees = [[5,3,8,2,6]].

The resulting tree is shown above. This is the only valid operation that can be performed, but the resulting tree is not a valid BST, so return null.
Example 3:


Input: trees = [[5,4],[3]]
Output: []
Explanation: It is impossible to perform any operations.
 

Constraints:

n == trees.length
1 <= n <= 5 * 104
The number of nodes in each tree is in the range [1, 3].
Each node in the input may have children but no grandchildren.
No two roots of trees have the same value.
All the trees in the input are valid BSTs.
1 <= TreeNode.val <= 5 * 104.


'''

from collections import Counter
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        n = len(trees)
        ids = list(range(n))
        def find(u):
            while u != ids[u]:
                ids[u] = ids[ids[u]]
                u = ids[u] 
            return u 
        leaves = {}
        def getLeaf(t, i, m):
            if t.left:
                m[t.left.val] = (i, -1, t)
            if t.right:
                m[t.right.val] = (i, 1, t)                
            return
        for i,t in enumerate(trees):
            getLeaf(t, i, leaves)
        for i, r in enumerate(trees):
            val = r.val
            if val in leaves:
                j, d, p = leaves[val]
                px, py = find(i), find(j)
                if px == py:
                    return None
                ids[px] = py               
                if d < 0: 
                    p.left = r
                else:
                    p.right = r
                leaves.pop(val)    
        root = []
        for i in range(n):
            if ids[i] == i:
                root.append(trees[i])
        if len(root) != 1: return None
        def checkBST(root, mi, mx):
            if not root: return True
            if root.val >= mx or root.val <= mi:
                return False
            return checkBST(root.left, mi, root.val) and checkBST(root.right, root.val, mx)

        return root[0] if checkBST(root[0], 0, 10**5) else None
    
    def canMerge2(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        
        roots = {}
        cnt = Counter()
        for t in trees:
            roots[t.val] = t
            cnt[t.val] += 1
            if t.left:
               cnt[t.left.val] += 1
            if t.right:
               cnt[t.right.val] += 1
         
                
        def traverse(root, roots, mi, mx):
            if not root: return True
            if root.val >= mx or root.val <= mi:
                return False
            if root.left == root.right: # root has no children
                if root.val in roots and root != roots[root.val]:
                    root.left = roots[root.val].left
                    root.right = roots[root.val].right
                    roots.pop(root.val)

            return traverse(root.left, roots, mi, root.val) and traverse(root.right, roots, root.val, mx)
        for t in trees:
            if cnt[t.val] == 1:
                return t if traverse(t, roots) and len(roots) == 1 else None
        return None          



        