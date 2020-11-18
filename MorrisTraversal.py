
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

        A key element of the Moriss traversal is that for a given node 'cur', 
        it visits its inorder predecessor twice: see 1) and 2) below 
     
        '''

        x, y, pre = None, None, None
        #pre = None
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right.val != root.val:
                    pre = pre.right
                if pre.right is None:
                    # 1) the first visit of its predecessor 'pre'
                    # node is threaded towards its in-order predecessor 
                    pre.right = root
                    root = root.left
                else:                    
                    #pre = root
                    if root.val == 6:
                        print(pre.val, pre.right.val)
                    # 2) the second visit of its predecessor 'pre'
                    # break the thread towards pre to restore the original
                    # tree structure
                    # NOTE: the condition that leads to here is
                    # root.val == pre.right.val     
                    pre.right = None
                    #print(' ', root.val,'->',end='')
                    root = root.right
            else:                
                #pre = root
                if root.val == 6:
                    print(root.right.val)
                #print(' ',root.val,'->', end='')
                root = root.right
        #print('x,y: ',x.val, y.val)
        print('')
        #x.val, y.val = y.val, x.val




   
if __name__ == '__main__':   
   root = constructBinaryTree([6,2,7,1,4,null,9,null, null, 3,5, null, null, 8, null])    
   #inOrder(root) 
   Solution().recoverTree(root)
   #inOrder(root) 
   #print(root.left.right.right.val)
