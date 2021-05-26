'''

-Medium-

Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.

 

Example 1:

Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]
 

Note:

1 <= pre.length == post.length <= 30
pre[] and post[] are both permutations of 1, 2, ..., pre.length.
It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
Accepted

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (TreeNode)

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0: return None        
        node = TreeNode(pre[0])
        if len(pre) == 1: return node        
        if pre[1] != post[-2]:
            i = post.index(pre[1])
            j = pre.index(post[-2])      
            node.left = self.constructFromPrePost(pre[1:j], post[:i+1])
            node.right = self.constructFromPrePost(pre[j:], post[i+1:-1])
        else:
            node.left = self.constructFromPrePost(pre[1:], post[:-1])
            node.right = None  
        return node      

if __name__ == '__main__':
    root = Solution().constructFromPrePost(pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1])
    root.prettyPrint()
    root = Solution().constructFromPrePost(pre = [2,1,3], post = [3,1,2])
    root.prettyPrint()
  