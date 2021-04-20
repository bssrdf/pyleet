
'''

Given a binary tree and a sum, find all root-to-leaf paths where each 
path's sum equals the given sum.

Note: A leaf is a node with no children.
'''

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(root, sum, [], ret)     
        return ret
    
    def dfs(self, root, target, path, ret):
        path.append(root.val)
        if root.left is None and root.right is None:
            if target == root.val:
                ret.append(path[:])
        if root.left:
           self.dfs(root.left, target - root.val, path, ret)
        if root.right:   
           self.dfs(root.right, target - root.val, path, ret)
        path.pop()


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node1.left = node2
node1.right = node3
node10 = TreeNode(11)
node4 = TreeNode(13)
node5 = TreeNode(4)
node2.left = node10
node3.left = node4
node3.right = node5
node6 = TreeNode(7)
node7 = TreeNode(2)
node8 = TreeNode(5)
node9 = TreeNode(1)
node10.left = node6
node10.right = node7
node5.left = node8
node5.right = node9

print(Solution().pathSum(node1, 22))



