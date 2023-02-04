'''

-Hard-
*DFS*

You are given the root of a binary tree with n nodes. Each node is assigned a unique value from 1 to n. You are also given an array queries of size m.

You have to perform m independent queries on the tree where in the ith query you do the following:

Remove the subtree rooted at the node with the value queries[i] from the tree. It is guaranteed that queries[i] will not be equal to the value of the root.
Return an array answer of size m where answer[i] is the height of the tree after performing the ith query.

Note:

The queries are independent, so the tree returns to its initial state after each query.
The height of a tree is the number of edges in the longest simple path from the root to some node in the tree.
 

Example 1:


Input: root = [1,3,4,2,null,6,5,null,null,null,null,null,7], queries = [4]
Output: [2]
Explanation: The diagram above shows the tree after removing the subtree rooted at node with value 4.
The height of the tree is 2 (The path 1 -> 3 -> 2).
Example 2:


Input: root = [5,8,9,2,1,3,7,4,6], queries = [3,2,4,8]
Output: [3,2,3,2]
Explanation: We have the following queries:
- Removing the subtree rooted at node with value 3. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 4).
- Removing the subtree rooted at node with value 2. The height of the tree becomes 2 (The path 5 -> 8 -> 1).
- Removing the subtree rooted at node with value 4. The height of the tree becomes 3 (The path 5 -> 8 -> 2 -> 6).
- Removing the subtree rooted at node with value 8. The height of the tree becomes 2 (The path 5 -> 9 -> 3).
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
m == queries.length
1 <= m <= min(n, 104)
1 <= queries[i] <= n
queries[i] != root.val



'''

from typing import Optional, List
from BinaryTree import (TreeNode, constructBinaryTree, null)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        dp, height = {}, {}
        # def postorder(node, depth):
        #     if not node: return 0
        #     left = postorder(node.left, depth+1)
        #     right = postorder(node.right, depth+1)
        #     if node.left:
        #         dp[node.left.val] = max(depth, right)
        #     if node.right:   
        #         dp[node.right.val] = max(depth, left)
        #     height[node.val] = max(left, right)
        #     return max(left, right)+1

        def postorder(node, depth):
            if not node: return 0
            left = postorder(node.left, depth+1)
            right = postorder(node.right, depth+1)            
            height[node.val] = max(left, right)
            return max(left, right)+1
        
        postorder(root, 0)
        # print(dp) 
        dp[root.val] = 0
        if root.left:
            dp[root.left.val] = (height[root.right.val] + 1) if root.right else 0
        if root.right:
            dp[root.right.val] = (height[root.left.val] + 1) if root.left else 0

        def preorder(node, depth):
            if not node: return
            if node.left:
                dp[node.left.val] = max(depth + ((1 + height[node.right.val]) if node.right else 0), dp[node.val])
            if node.right:
                dp[node.right.val] = max(depth + ((1 + height[node.left.val]) if node.left else 0), dp[node.val])
            preorder(node.left, depth+1)
            preorder(node.right, depth+1)
        # preorder(root.left, 1)
        # preorder(root.right, 1)
        preorder(root, 0)

        # print(dp) 
        # print(height)

          
        return [dp[q] for q in queries]


if __name__ == "__main__":   
    root = constructBinaryTree([1,3,4,2,null,6,5,null, null,null,null,null,null,null,7])  
    root.prettyPrint()
    print(Solution().treeQueries(root, queries = [4]))
    root = constructBinaryTree([5,8,9,2,1,3,7,4,6])  
    root.prettyPrint()
    print(Solution().treeQueries(root, queries = [3,2,4,8]))
    root = constructBinaryTree([1,null,5,null,null,3,null, null, null, null,null, 2,4])  
    root.prettyPrint()
    print(Solution().treeQueries(root, queries = [3,5,4,2,4]))
    root = constructBinaryTree([2,1,4,null,null,3])  
    root.prettyPrint()
    print(Solution().treeQueries(root, queries = [1,4,3,4]))