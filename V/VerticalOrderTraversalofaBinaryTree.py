'''
-Hard-
*DFS*
*Hash Table*

Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions 
(x - 1, y - 1) and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each 
unique x-coordinate from left to right. Each report is a list of all nodes at a given 
x-coordinate. The report should be primarily sorted by y-coordinate from highest 
y-coordinate to lowest. If any two nodes have the same y-coordinate in the report, the 
node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).
Example 2:


Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position 
according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (constructBinaryTree, null, TreeNode)
import heapq
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        The general idea is to traverse the tree and assign a coordinate (x, y) to 
        each node (there may be nodes who all have the same coordinate). The key is 
        to use a 2D hash table (or hashtable of hashtable) to record these (x, y) pairs
        This is sort of like a sparse 2D matrix structure. 
        So x is the key of a hashtable, the value is another hashtable with key = y and 
        value is a priority queue which stores node values in ascending order
        once the traversal is done, we gather the results using a list of list and go
        through keys of the hashtable, first x (in default sort order) then y in 
        reversed sort order). for each priority queue, pop it until it is empty.

        """
        m = {}
        res = []
        def dfs(root, x, y):
            if not root: return
            heapq.heappush(m.setdefault(x, {}).setdefault(y, []), root.val)
            dfs(root.left,  x-1, y-1)
            dfs(root.right, x+1, y-1)
        dfs(root, 0, 0)
        for x in sorted(m.keys()):
            cur = []
            for y in sorted(m[x].keys(), reverse=True):
                while m[x][y]:
                    cur.append(heapq.heappop(m[x][y]))
            res.append(cur)
        return res



if __name__ == "__main__":
    root = constructBinaryTree([3,9,20,null,null,15,7])
    root.prettyPrint()
    print(Solution().verticalTraversal(root))
    
    root = constructBinaryTree([1,2,3,4,5,6,7])
    root.prettyPrint()
    print(Solution().verticalTraversal(root))