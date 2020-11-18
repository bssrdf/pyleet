'''

*Morris Traversal*

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''
from BinaryTree import (TreeNode, constructBinaryTree, inOrder, null) 

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        '''
        For Morris traversal, see 
        https://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html   
     
        '''


        x, y, pny = None, None, None
        pre = None
        while root:
            if root.left:
                pnt = root.left
                while pnt.right and pnt.right.val != root.val:
                    pnt = pnt.right
                if pnt.right is None:
                    pnt.right = root
                    root = root.left
                else:
                    if pre and pre.val > root.val:
                        y = root
                        if x is None:
                            x = pre
                    pre = root
                    pnt.right = None
                    root = root.right
            else:
                if pre and pre.val > root.val:
                    y = root
                    if x is None:
                        x = pre
                pre = root
                root = root.right
        #print('x,y: ',x.val, y.val)
        x.val, y.val = y.val, x.val




   
if __name__ == '__main__':
   root = constructBinaryTree([3,1,4,null,null,2,null])    
   print(root.val) 
   Solution().recoverTree(root)
   print(root.val) 
   root = constructBinaryTree([5,2,6,1,8,null,3])    
   inOrder(root) 
   Solution().recoverTree(root)
   inOrder(root) 
   #print(root.left.right.right.val)
