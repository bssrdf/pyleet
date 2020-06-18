class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

null = None  

def constructBinaryTree(arr):
    root = None
    root = insertLevelOrder(arr, root, 0, len(arr))
    return root

def insertLevelOrder(arr, root, i, n):

    # Base case for recursion  
    
    if i < n:
      
        if arr[i] is None:
            return None
       
        temp = TreeNode(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = insertLevelOrder(arr, root.left, 
                                     2*i+1, n)  
  
        # insert right child  
        root.right = insertLevelOrder(arr, root.right, 
                                      2*i+2, n) 
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
      
    arr = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    
    root = constructBinaryTree(arr)
    inOrder(root)
       


        
    
