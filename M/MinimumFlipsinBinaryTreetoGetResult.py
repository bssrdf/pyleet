'''

-Hard-



You are given the root of a binary tree with the following properties:

Leaf nodes have either the value 0 or 1, representing false and true respectively.
Non-leaf nodes have either the value 2, 3, 4, or 5, representing the boolean operations OR, AND, XOR, and NOT, respectively.
You are also given a boolean result, which is the desired result of the evaluation of the root node.

The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. true or false.
Otherwise, evaluate the node's children and apply the boolean operation of its value with the children's evaluations.
In one operation, you can flip a leaf node, which causes a false node to become true, and a true node to become false.

Return the minimum number of operations that need to be performed such that the evaluation of root yields result. It can be shown that there is always a way to achieve result.

A leaf node is a node that has zero children.

Note: NOT nodes have either a left child or a right child, but other non-leaf nodes have both a left child and a right child.

 

Example 1:



Input: root = [3,5,4,2,null,1,1,1,0], result = true
Output: 2
Explanation:
It can be shown that a minimum of 2 nodes have to be flipped to make the root of the tree
evaluate to true. One way to achieve this is shown in the diagram above.
Example 2:

Input: root = [0], result = false
Output: 0
Explanation:
The root of the tree already evaluates to false, so 0 nodes have to be flipped.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 5
OR, AND, and XOR nodes have 2 children.
NOT nodes have 1 child.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2, 3, 4, or 5.



'''

from typing import Optional
from BinaryTree import (TreeNode, null, constructBinaryTree)

class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:

        def dfs(node, target):
            if not node: return 10**5
            if node.val <= 1: # leaf node 
                if node.val != target: return 1                
                else: return 0 
            if node.val == 2: # |   
                if target == 1:
                    return min( dfs(node.left, 1)+dfs(node.right, 1),
                                dfs(node.left, 1)+dfs(node.right, 0),
                                dfs(node.left, 0)+dfs(node.right, 1) )
                else:
                    return dfs(node.left, 0)+dfs(node.right, 0)

            elif node.val == 3: # &
                if target == 1:
                    return dfs(node.left, target)+dfs(node.right, target)                    
                else:
                    return min( dfs(node.left, 0)+dfs(node.right, 1),
                                dfs(node.left, 1)+dfs(node.right, 0),
                                dfs(node.left, 0)+dfs(node.right, 0) )
            elif node.val == 4: # ^
                if target == 1:
                    return min( dfs(node.left, 1)+dfs(node.right, 0), 
                                dfs(node.left, 0)+dfs(node.right, 1)) 
                else:
                    return min( dfs(node.left, 1)+dfs(node.right, 1), 
                                dfs(node.left, 0)+dfs(node.right, 0)) 
            elif node.val == 5: # not
                if target == 1:
                    return min(dfs(node.left, 0), dfs(node.right, 0))
                else:
                    return min(dfs(node.left, 1), dfs(node.right, 1))
                    

        return dfs(root, 1 if result else 0)                  

if __name__ == "__main__":
    root = constructBinaryTree([3,5,4,2,null,1,1,1,0])
    print(Solution().minimumFlips(root, True))
    root = constructBinaryTree([0])
    print(Solution().minimumFlips(root, False))

