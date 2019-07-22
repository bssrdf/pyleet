# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 23:08:59 2017
The thief has found himself a new place for his thievery again. There is only 
one entrance to this area, called the "root." Besides the root, each house has
 one and only one parent house. After a tour, the smart thief realized that 
 "all houses in this place forms a binary tree". It will automatically contact 
 the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without 
alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.

Step I

At first glance, the problem exhibits the feature of "optimal substructure": if we want to rob maximum amount of money 
from current binary tree (rooted at root), we surely hope that we can do the same to its left and right subtrees.

So going along this line, let's define the function rob(root) which will return the maximum amount of money that we 
can rob for the binary tree rooted at root; the key now is to construct the solution to the original problem from 
solutions to its subproblems, i.e., how to get rob(root) from rob(root.left), rob(root.right), ... etc.

Apparently the analyses above suggest a recursive solution. And for recursion, it's always worthwhile figuring out
the following two properties:

Termination condition: when do we know the answer to rob(root) without any calculation? Of course when the tree is 
empty -- we've got nothing to rob so the amount of money is zero.

Recurrence relation: i.e., how to get rob(root) from rob(root.left), rob(root.right), ... etc. From the point of view 
of the tree root, there are only two scenarios at the end: root is robbed or is not. If it is, due to the constraint 
that "we cannot rob any two directly-linked houses", the next level of subtrees that are available would be the four 
"grandchild-subtrees" (root.left.left, root.left.right, root.right.left, root.right.right). However if root is not 
robbed, the next level of available subtrees would just be the two "child-subtrees" (root.left, root.right). We only 
need to choose the scenario which yields the larger amount of money.

Here is the program for the ideas above:

Step II

In step I, we only considered the aspect of "optimal substructure", but think little about the possibilities of 
overlapping of the subproblems. For example, to obtain rob(root), we need rob(root.left), rob(root.right), 
rob(root.left.left), rob(root.left.right), rob(root.right.left), rob(root.right.right); but to get rob(root.left), 
we also need rob(root.left.left), rob(root.left.right), similarly for rob(root.right). The naive solution above 
computed these subproblems repeatedly, which resulted in bad time performance. Now if you recall the two conditions 
for dynamic programming: "optimal substructure" + "overlapping of subproblems", we actually have a DP problem. 
A naive way to implement DP here is to use a hash map to record the results for visited subtrees.

And here is the improved solution:

Step III -- Think one step back

In step I, we defined our problem as rob(root), which will yield the maximum amount of money 
that can be robbed of the binary tree rooted at root. This leads to the DP problem summarized 
in step II.

Now let's take one step back and ask why we have overlapping subproblems. If you trace all 
the way back to the beginning, you'll find the answer lies in the way how we have defined 
rob(root). As I mentioned, for each tree root, there are two scenarios: it is robbed or is 
not. rob(root) does not distinguish between these two cases, so "information is lost as the 
recursion goes deeper and deeper", which results in repeated subproblems.

If we were able to maintain the information about the two scenarios for each tree root, let's
see how it plays out. Redefine rob(root) as a new function which will return an array of 
two elements, the first element of which denotes the maximum amount of money that can be 
robbed if root is not robbed, while the second element signifies the maximum amount of money 
robbed if it is robbed.

Let's relate rob(root) to rob(root.left) and rob(root.right)..., etc. For the 1st element of 
rob(root), we only need to sum up the larger elements of rob(root.left) and rob(root.right), 
respectively, since root is not robbed and we are free to rob its left and right subtrees. 
For the 2nd element of rob(root), however, we only need to add up the 1st elements of 
rob(root.left) and rob(root.right), respectively, plus the value robbed from root itself, 
since in this case it's guaranteed that we cannot rob the nodes of root.left and root.right.

As you can see, by keeping track of the information of both scenarios, we decoupled the 
subproblems and the solution essentially boiled down to a greedy one. Here is the program:

@author: merli
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        #ans = self.dp(root, {})
        #return ans
        ans = self.dpFast(root)
        return max(ans[0],ans[1])
        
    def dp(self, root, robtree):
        if not root:
            return 0
        if root in robtree:
            return robtree[root]
        val = 0
        if root.left:
            val += self.dp(root.left.left, robtree) + self.dp(root.left.right,robtree)
        if root.right:
            val += self.dp(root.right.left, robtree) + self.dp(root.right.right,robtree)
        val = max(val+root.val, self.dp(root.left,robtree)+self.dp(root.right,robtree))
        robtree[root] = val
        return val
        
    def dpFast(self, root):
        if not root:
            return 0,0
        l0,l1 = self.dpFast(root.left)
        r0,r1 = self.dpFast(root.right)
        res0,res1 = 0,0
        res0 = max(l0, l1) + max(r0,r1)
        res1 = root.val+l0+r0
        # for a leaf node,if it is not robbed, res0 is 0
        # if it is robbed, res1 is its value
        return res0,res1
            
if __name__ == "__main__":
    root = TreeNode(3)    
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    
#==============================================================================
#     root.left = TreeNode(2)
#     root.right = TreeNode(3)
#     root.left.right = TreeNode(3)
#     root.right.right = TreeNode(1)
#==============================================================================
    print(Solution().rob(root))
    