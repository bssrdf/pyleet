
'''

-Medium-

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must 
go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range 
-1,000,000 to 1,000,000.

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11


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
        return self.dfs(root, sum) +  \
               self.pathSum(root.left, sum) + \
               self.pathSum(root.right, sum)    
        
    
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
        # cache initialized to {0:1} so it can work in cases
        # when there is only one root node, and its val = sum
        self.helper(root, sum, 0, {0:1})
        return self.result 
    '''
    compute prefix sum starting from root down to a particular node
    along this path, if there is a sum = target, it can be detected
    by checking whether (prefixSum+node.val - target) is in the cache
    '''
    def helper(self, root, target, preSum, cache):
        if root:
            curVal = preSum + root.val
            complement = curVal - target
            if complement in cache:
                print(root.val, curVal, complement, target, cache)
                self.result += cache[complement]
            cache.setdefault(curVal, 0)
            cache[curVal] += 1
            self.helper(root.left,  target, curVal, cache) 
            self.helper(root.right, target, curVal, cache) 
            cache[curVal] -= 1 # backtracking
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



