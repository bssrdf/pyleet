'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node 
to any node in the tree along the parent-child connections. The path must contain 
at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42

'''
import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        这道求二叉树的最大路径和是一道蛮有难度的题，难就难在起始位置和结束位置可以为任意位置，
        博主当然是又不会了，于是上网看看大神们的解法，像这种类似树的遍历的题，一般来说都需要
        用 DFS 来求解，先来看一个简单的例子：

 

    4
   / \
  11 13
 / \
7   2
 

        由于这是一个很简单的例子，很容易就能找到最长路径为 7->11->4->13，那么怎么用递归来找出正确
        的路径和呢？根据以往的经验，树的递归解法一般都是递归到叶节点，然后开始边处理边回溯到根节点。
        这里就假设此时已经递归到结点7了，其没有左右子节点，如果以结点7为根结点的子树最大路径和就是7。
        然后回溯到结点 11，如果以结点 11 为根结点的子树，最大路径和为 7+11+2=20。但是当回溯到结点
        4的时候，对于结点 11 来说，就不能同时取两条路径了，只能取左路径，或者是右路径，所以当根结
        点是4的时候，那么结点 11 只能取其左子结点7，因为7大于2。所以，对于每个结点来说，要知道经
        过其左子结点的 path 之和大还是经过右子节点的 path 之和大。递归函数返回值就可以定义为以当
        前结点为根结点，到叶节点的最大路径之和，然后全局路径最大值放在参数中，用结果 res 来表示。

        在递归函数中，如果当前结点不存在，直接返回0。否则就分别对其左右子节点调用递归函数，由于路
        径和有可能为负数，这里当然不希望加上负的路径和，所以和0相比，取较大的那个，就是要么不加，
        加就要加正数。然后来更新全局最大值结果 res，就是以左子结点为终点的最大 path 之和加上以右
        子结点为终点的最大 path 之和，还要加上当前结点值，这样就组成了一个条完整的路径。而返回值
        是取 left 和 right 中的较大值加上当前结点值，因为返回值的定义是以当前结点为终点的 path 
        之和，所以只能取 left 和 right 中较大的那个值，而不是两个都要

        """
        res = [-sys.maxsize]
        def dfs(node):
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val+left+right) 
            return max(left, right) + node.val
        dfs(root)
        return res[0]