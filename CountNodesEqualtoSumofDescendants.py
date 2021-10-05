'''

-Medium-

Given the root of a binary tree, return the number of nodes where the value of the node is 
equal to the sum of the values of its descendants.

A descendant of a node x is any node that is on the path from node x to some leaf node. The sum 
is considered to be 0 if the node has no descendants.

Example 1:

Image text

Input: root = [10,3,4,2,1]

Output: 2

Explanation:

For the node with value 10: The sum of its descendants is 3+4+2+1 = 10.

For the node with value 3: The sum of its descendants is 2+1 = 3.

Example 2:

Image text

Input: root = [2,3,null,2,null]

Output: 0

Explanation:

No node has a value that is equal to the sum of its descendants.

Example 3:

Image text

Input: root = [0]

Output: 1

For the node with value 0: The sum of its descendants is 0 since it has no descendants.

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
0 <= Node.val <= 10^5


'''


from BinaryTree import (null, TreeNode, constructBinaryTree)

class Solution(object):
    def numofNodes(self, root):
        res = [0]
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            if node.val == l + r:
                res[0] += 1
            return l+r+node.val
        helper(root)
        return res[0]


if __name__=="__main__":
    root = constructBinaryTree([10,3,4,2,1])
    root.prettyPrint()
    print(Solution().numofNodes(root))
    root = constructBinaryTree([2,3,null,2])
    root.prettyPrint()
    print(Solution().numofNodes(root))
    root = constructBinaryTree([0])
    root.prettyPrint()
    print(Solution().numofNodes(root))
     