class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.bal = 0
         self.left = left
         self.right = right



class Solution(object):

    def computeFactor(self, root):
        if not root:
            return 0
        hl = self.computeFactor(root.left)
        hr = self.computeFactor(root.right)
        root.bal = hl - hr
        return max(hl,hr)+1


    def printFactor(self, root):
        if root:
            print(str(root.val)+'/'+str(root.bal))
            self.printFactor(root.left)
            self.printFactor(root.right)

if __name__ == "__main__":
    root = TreeNode(10)
    node1 = TreeNode(7)
    node2 = TreeNode(8)
    node3 = TreeNode(6)
    node4 = TreeNode(5)
    node5 = TreeNode(4)
    node6 = TreeNode(2)
    node7 = TreeNode(3)
    node8 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.right = node5
    node3.left = node6
    node4.right = node7
    node5.left = node8
    Solution().computeFactor(root)    
    Solution().printFactor(root)        