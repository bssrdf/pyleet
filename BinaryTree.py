class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def constructBinaryTree(arr, root, i, n):

    # Base case for recursion  
    if i < n: 
        if not arr[i]:
            return None
        #if i == 3:
         #   print('None')
        print(arr[i])
        temp = TreeNode(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = constructBinaryTree(arr, root.left, 
                                     2 * i + 1, n)  
  
        # insert right child  
        root.right = constructBinaryTree(arr, root.right, 
                                      2 * i + 2, n) 
    return root 
  
def inOrder(root): 
    if root != None: 
        inOrder(root.left)  
        print(root.val, end=" ")  
        inOrder(root.right)  

def preOrder(root): 
    if root != None: 
        print(root.val, end=" ")  
        preOrder(root.left)        
        preOrder(root.right)  

if __name__ == "__main__":
    null = None    
    arr = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    root = None
    root = constructBinaryTree(arr, root, 0, len(arr))
    preOrder(root)
       


        
    
