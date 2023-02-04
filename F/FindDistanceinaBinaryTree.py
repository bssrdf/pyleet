'''

-Medium-

Given the root of a binary tree and two integers p and q, return the distance between the nodes of 
value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

Example 1:

Image text

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 0

Output: 3

Explanation: There are 3 edges between 5 and 0: 5-3-1-0.

Example 2:

Image text

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 7

Output: 2

Explanation: There are 2 edges between 5 and 7: 5-2-7.

Example 3:

Image text

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 5

Output: 0

Explanation: The distance between a node and itself is 0.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^9
All Node.val are unique.
p and q are values in the tree.


'''


from BinaryTree import (null, constructBinaryTree, TreeNode)
class Solution(object):
    def findDistance(self, root, p,  q):
        def LCA(node, p, q):
            if not node: return None
            if node.val == p or node.val == q: return node
            (left, right) = (LCA(node.left, p, q),
                            LCA(node.right, p, q))
            return root if left and right else left or right
        def distance(root, v):
            if not root: return -1
            if root.val == v: return 0
            left = distance(root.left, v)
            right = distance(root.right, v)
            if left >= 0: return left + 1
            if right >= 0: return right + 1
            return -1
        lca = LCA(root, p, q)
        #return distance(root, p) + distance(root, q) - 2 * distance(root, lca.val)
        return distance(lca, p) + distance(lca, q) 

if __name__ == "__main__":
    root = constructBinaryTree([3,5,1,6,2,0,8,null,null,7,4])    
    root.prettyPrint()
    print(Solution().findDistance(root, 5, 0))
    print(Solution().findDistance(root, 5, 7))
    print(Solution().findDistance(root, 5, 5))
    
    