'''

-Medium-


Implement the BSTIterator class that represents an iterator over the in-order 
traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
The root of the BST is given as part of the constructor. The pointer should be 
initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to 
the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, 
the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be 
at least a next number in the in-order traversal when next() is called.

 

Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", 
"hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 10^5 calls will be made to hasNext, and next.

Follow up:

Could you implement next() and hasNext() to run in average O(1) time and 
use O(h) memory, where h is the height of the tree?

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.st = []
        while root:
            self.st.append(root)
            root = root.left
        
        

    def next(self):
        """
        :rtype: int
        """
        node = self.st.pop()
        res = node.val
        if node.right:
            node = node.right 
            while node:
                self.st.append(node)
                node = node.left
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.st) > 0

if __name__ == "__main__":     
    root = TreeNode(7)
    root3 = TreeNode(3)
    root15 = TreeNode(15)
    root9 = TreeNode(9)  
    root20 = TreeNode(20)  
    root.left = root3
    root.right = root15
    root15.left = root9
    root15.right = root20

    bSTIterator = BSTIterator(root)
    print(bSTIterator.next())     # return 3
    print(bSTIterator.next())     # return 7
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())     # return 9
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())     # return 15
    print(bSTIterator.hasNext())  # return True
    print(bSTIterator.next())    # return 20
    print(bSTIterator.hasNext())  # return False