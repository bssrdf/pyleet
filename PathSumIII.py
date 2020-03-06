
'''

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must 
go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range 
-1,000,000 to 1,000,000.



'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):

    result = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)    
        
    
    def dfs(self, root, target):
        if not root:
            return 0
        return (1 if root.val == target else 0) + \
               self.dfs(root.left, target - root.val) + \
               self.dfs(root.right, target - root.val)

    def pathSumOpt(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result 

    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache) 
            self.helper(root.right, target, so_far+root.val, cache) 
            cache[so_far+root.val] -= 1
        return

node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node1.left = node2
node1.right = node3
node10 = TreeNode(3)
node4 = TreeNode(2)
node5 = TreeNode(11)
node2.left = node10
node3.right = node5
node2.right = node4
node6 = TreeNode(3)
node7 = TreeNode(-2)
node8 = TreeNode(1)

node10.left = node6
node10.right = node7

node4.right = node8

print(Solution().pathSum(node1, 8))
print(Solution().pathSumOpt(node1, 8))



