'''
-Medium-
*Recursion*

Given an integer n, generate all structurally unique BST's 
(binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (TreeNode, null)

class Solution(object):



    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 1:
            return [TreeNode(n)]
        ans = []
        subtrees = self.generateTrees(n-1)
        def copy(root):
            if not root:
                return None
            node = TreeNode(root.val)            
            if root.left:
                node.left = copy(root.left)
            if root.right:
                node.right = copy(root.right)            
            return node
        #print(n, len(subtrees))
        for st in subtrees:
            # current n as root with subtree as left child
            root = TreeNode(n)
            root.left = copy(st)
            ans.append(root)
        
            # current n as far right leaf child
            root = copy(st)
            node = root
            while node.right:
                node = node.right
            node.right = TreeNode(n)                
            ans.append(root)
             
           
            node = st.right            
            lev = 1
            while node:    
                root = copy(st)
                newnode = root
                cur = 1
                while cur < lev:
                   newnode = newnode.right
                   cur += 1
                newleft = newnode.right         
                newnode.right = TreeNode(n)
                newnode.right.left = newleft                
                ans.append(root)
                node = node.right
                lev += 1
            
        return ans
    
    def generateTreesSimpleSolution(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        '''
        I start by noting that 1..n is the in-order traversal for any BST with 
        nodes 1 to n. So if I pick i-th node as my root, the left subtree will 
        contain elements 1 to (i-1), and the right subtree will contain elements 
        (i+1) to n. I use recursive calls to get back all possible trees for 
        left and right subtrees and combine them in all possible ways with the 
        root.
        '''
        def genTreeList(l, r):
            tlis = []
            if l > r:
                tlis.append(None)
                return tlis
            if l == r:
                tlis.append(TreeNode(l))
                return tlis
            for i in range(l, r+1):
                left = genTreeList(l, i-1)
                right = genTreeList(i+1, r)
                for lnode in left:
                    for rnode in right:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        tlis.append(root)
            return tlis
        return genTreeList(1, n)



if __name__ == "__main__":
    bsts = Solution().generateTrees(4)
    print(len(bsts))
    for bst in bsts:
        bst.prettyPrint()
    bsts = Solution().generateTreesSimpleSolution(4)
    print(len(bsts))
    for bst in bsts:
        bst.prettyPrint()
    #for t in bsts:
    #    preOrder(t)
    #    print('')
