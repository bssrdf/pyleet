'''
-Medium-

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in 
a complete binary tree, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 10^4].
0 <= Node.val <= 5 * 10^4
The tree is guaranteed to be complete.



'''

from BinaryTree import (null, constructBinaryTree, TreeNode)

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def height(node):
            if not node: return 0
            return 1+height(node.left)
        cnt = [0]            
        ht = height(root)
        def count(node, h):
            if not node: return
            if h == ht: 
                cnt[0] += 1
                return
            count(node.left, h+1)
            count(node.right, h+1)
        count(root, 1)        
        return cnt[0]+ sum(1<<h for h in range(ht-1))
    
    def countNodesBinary(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(node):
            if not node: return -1
            return 1+height(node.left)
        res, h  = 0,  height(root)
        if h < 0: return 0
        print('total height =', h)
        if height(root.right) == h - 1: 
            print('A')
            # 若返回值为 h-1，说明左子树是一棵完美二叉树，
            # 则左子树的结点个数是 2^h-1 个，再加上当前结点，总共是 2^h 个，即 1<<h，
            # 此时再加上对右子结点调用递归函数的返回值即可。
            return (1 << h) + self.countNodesBinary(root.right)
        # 若对右子结点调用 getHeight 函数的返回值不为 h-1，说明右子树一定是完美树，
        # 且高度为 h-1，则总结点个数为 2^(h-1)-1，加上当前结点为 2^(h-1)，即 1<<(h-1)，
        # 然后再加上对左子结点调用递归函数的返回值即可。            
        return (1 << (h - 1)) + self.countNodesBinary(root.left)

if __name__ == "__main__":  
    root = constructBinaryTree([1,2,3,4,5,6])
    root.prettyPrint()
    #print(Solution().countNodes(root))
    print(Solution().countNodesBinary(root))
    root = constructBinaryTree([1,2,3,4,5])
    root.prettyPrint()
    print(Solution().countNodesBinary(root))
    #print(Solution().countNodes(None))
    #root = constructBinaryTree([1])
    #print(Solution().countNodes(root))

