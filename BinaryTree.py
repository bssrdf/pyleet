from copy import deepcopy as deepcopy
from collections import deque
import sys

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    def getHeight(self):
        return TreeNode.getHeightHelper(self)

    @staticmethod
    def getHeightHelper(node):
        if not node:
            return 0
        else:
            return max(TreeNode.getHeightHelper(node.left), 
                       TreeNode.getHeightHelper(node.right)) + 1
    
    def fillTree(self, height):
        TreeNode.fillTreeHelper(self, height)

    @staticmethod
    def fillTreeHelper(node, height):
        if height <= 1:
            return
        if node:
            if not node.left: node.left = TreeNode(' ')
            if not node.right: node.right = TreeNode(' ')
            TreeNode.fillTreeHelper(node.left, height - 1)
            TreeNode.fillTreeHelper(node.right, height - 1)

    def prettyPrint(self):
        """
        """
        # get height of tree
        total_layers = self.getHeight()

        tree = deepcopy(self)

        tree.fillTree(total_layers)
        # start a queue for BFS
        queue = deque()
        # add root to queue
        queue.append(tree) # self = root
        # index for 'generation' or 'layer' of tree
        gen = 1 
        # BFS main
        while queue:
        # copy queue
        # 
            copy = deque()
            while queue:
                copy.append(queue.pop())
        # 
        # end copy queue 

            first_item_in_layer = True
            edges_string = ""
            extra_spaces_next_node = False

            # modified BFS, layer by layer (gen by gen)
            while copy:

                node = copy.pop()

                # -----------------------------
                # init spacing
                spaces_front = pow(2, total_layers - gen + 1) - 2
                spaces_mid   = pow(2, total_layers - gen + 2) - 2
                dash_count   = pow(2, total_layers - gen) - 2
                if dash_count < 0:
                    dash_count = 0
                spaces_mid = spaces_mid - (dash_count*2)
                spaces_front = spaces_front - dash_count
                init_padding = 2
                spaces_front += init_padding
                if first_item_in_layer:
                    edges_string += " " * init_padding
                # ----------------------------->

                # -----------------------------
                # construct edges layer
                edge_sym = "/" if node.left and node.left.val is not " " else " "
                if first_item_in_layer:
                    edges_string += " " * (pow(2, total_layers - gen) - 1) + edge_sym
                else:
                    edges_string += " " * (pow(2, total_layers - gen + 1) + 1) + edge_sym
                edge_sym = "\\" if node.right and node.right.val is not " " else " "
                edges_string += " " * (pow(2, total_layers - gen + 1) - 3) + edge_sym
                # ----------------------------->

                # -----------------------------
                # conditions for dashes
                if node.left and node.left.val == " ":
                    dash_left = " "
                else:
                    dash_left = "_"

                if node.right and node.right.val == " ":
                    dash_right = " "
                else:
                    dash_right = "_"
                # ----------------------------->

                # -----------------------------
                # handle condition for extra spaces when node lengths don't match or are even:
                if extra_spaces_next_node:
                    extra_spaces = 1
                    extra_spaces_next_node = False
                else:
                    extra_spaces = 0
                # ----------------------------->
                
                # -----------------------------
                # account for longer data
                data_length = len(str(node.val))
                if data_length > 1:
                    if data_length % 2 == 1: # odd
                        if dash_count > 0:
                            dash_count -= int(((data_length - 1)/2))
                        else:
                            spaces_mid -= int((data_length - 1)/2)
                            spaces_front -= int((data_length - 1)/2)
                            if data_length is not 1: 
                                extra_spaces_next_node = True 
                    else: # even
                        if dash_count > 0:
                            dash_count -= int(((data_length)/2) - 1)
                            extra_spaces_next_node = True
                    # dash_count += 1
                        else:
                            spaces_mid -= int((data_length - 1))
                            spaces_front -= int((data_length - 1))
                # ----------------------------->
                
                # -----------------------------
                # print node with/without dashes
                if first_item_in_layer:                    
                    print (" " * spaces_front + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count), end = ' ')
                    first_item_in_layer = False
                else:                    
                    print (" " * (spaces_mid-extra_spaces) + (dash_left * dash_count) + str(node.val) + (dash_right * dash_count), end = " ")
                # ----------------------------->

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            # print the fun squiggly lines
            if queue:
                print("\n" + edges_string)

            # increase layer index
            gen += 1

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
      
    #arr = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    
    #root = constructBinaryTree(arr)
    #inOrder(root)

    root = constructBinaryTree([6,2,7,1,4,null,9,null, null, 3,5, null, null, 8, null])    
    
    #inOrder(root)
    #preOrder(root)
    root.prettyPrint()


        
    
