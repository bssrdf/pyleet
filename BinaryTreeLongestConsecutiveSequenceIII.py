'''
-Medium-


描述
It's follow up problem for Binary Tree Longest Consecutive Sequence II

Given a k-ary tree, find the length of the longest consecutive sequence path.
The path could be start and end at any node in the tree

样例
Example 1:

Input:
5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>
Output:
5
Explanation:
     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 31

return 5, // 3-4-5-6-7
Example 2:

Input:
1<>
Output:
1

'''

"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""

class ResultType:
    def __init__(self, globalMax, maxUp, maxDown):
        self.globalMax = globalMax
        self.maxUp = maxUp
        self.maxDown = maxDown


class Solution:

    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        return self.helper(root).globalMax
    
    def helper(self, root):
        
        if not root:
            return ResultType(0, 0, 0)
        
        maxUp = 0
        maxDown = 0
        mx = -float('inf')

        for child in root.children:
            
            if not child: continue
            
            childResult = self.helper(child)
            if child.val + 1 == root.val:
                maxDown = max(maxDown, childResult.maxDown + 1)
            
            if child.val - 1 == root.val:
                maxUp = max(maxUp, childResult.maxUp + 1)
            
            mx = max(mx, childResult.globalMax, maxUp + maxDown + 1)
        
        return ResultType(mx, maxUp, maxDown)
