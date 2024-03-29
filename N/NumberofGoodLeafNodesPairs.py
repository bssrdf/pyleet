'''
-Medium-

Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary 
tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between 
them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
Example 4:

Input: root = [100], distance = 1
Output: 0
Example 5:

Input: root = [1,1,1], distance = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 2^10].
Each node's value is between [1, 100].
1 <= distance <= 10


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        leafs = set()
        graph = defaultdict(list)
        def helper(root):
            if not root: return
            if not root.left and not root.right:
                leafs.add(root)
            if root.left:
                graph[root].append(root.left)
                graph[root.left].append(root)
            if root.right:
                graph[root].append(root.right)
                graph[root.right].append(root)
            helper(root.left)
            helper(root.right)
        helper(root)
        self. res = 0
        def dfs(node, start, depth, visited):
            if depth > distance: return
            if node in leafs and node != start:    
                self.res += 1
                return
            for neib in graph[node]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib, start, depth+1, visited)
        for leaf in leafs:
            dfs(leaf, leaf, 0, {leaf})            

        return self.res // 2 

    def countPairsPostTraversal(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        d = distance
        self.res = 0
        def dfs(node):
            if not node: return [0]*(d+1)
            if not node.left and not node.right:
                arr = [0]*(d+1)
                arr[1] = 1
                return arr
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(1, d):
                for j in range(1, d):
                    if i+j <= d: self.res += left[i] * right[j]
            arr = [0]*(d+1)
            for i in range(d, 0, -1):
                arr[i] = left[i-1]+right[i-1]
            return arr
        dfs(root)
        return self.res                
