'''

-Medium-

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a 
forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the 
result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from BinaryTree import null, TreeNode, constructBinaryTree

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        dels = set(to_delete)
        def delete(node, parent, branch):
            if not node: return
            if node.val in dels:
                if parent:
                    if branch < 0: parent.left = None
                    elif branch > 0: parent.right = None
                if node.left and node.left.val not in dels:
                    res.append(node.left)
                if node.right and node.right.val not in dels:
                    res.append(node.right)    
            delete(node.left, node, -1)
            delete(node.right, node, 1)
        if root.val not in dels: res.append(root)
        delete(root, None, 0)
        return res        



if __name__ == "__main__":
    root = constructBinaryTree([1,2,3,4,5,6,7])
    root.prettyPrint()
    forests = Solution().delNodes(root, [3,5])
    for f in forests:
        print(f.val)

        