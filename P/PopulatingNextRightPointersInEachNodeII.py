'''
-Medium-

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next 
right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does 
not count as extra space for this problem.
 

Example 1:



Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function 
should populate each next pointer to point to its next right node, 
just like in Figure B. The serialized output is in level order as 
connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100

'''
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

#from BinaryTree import (TreeNode, constructBinaryTree, null)

class Solution(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def helper(root):            
            if root:
                if root.left and root.right:
                   root.left.next = root.right
                pre = root
                cur = pre.next                  
                while pre and cur:   
                    #print(pre.val, '(',pre.next.val,')', cur.val)                
                    if pre.right:
                        if cur.left:
                            pre.right.next = cur.left    
                            if cur.right and not cur.left.next:
                                cur.left.next = cur.right
                            pre, cur = cur, cur.next
                        elif cur.right:
                            pre.right.next = cur.right
                            pre, cur = cur, cur.next
                        else:
                            cur = cur.next    
                    elif pre.left:
                        if cur.left:
                            pre.left.next = cur.left
                            if cur.right and not cur.left.next:
                                cur.left.next = cur.right
                            pre, cur = cur, cur.next    
                        elif cur.right:
                            pre.left.next = cur.right
                            pre, cur = cur, cur.next       
                        else:
                            cur = cur.next
                    else:
                        pre, cur = cur, cur.next           
                helper(root.left)
                helper(root.right)
        helper(root)
        return root

    def connectLevelOrder(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        node = root
        while node:
            tempChild = Node(0)
            cur = tempChild
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next  
                node = node.next
            node = tempChild.next  
        return root


if __name__ == "__main__":
    root = Node(2)
    node2 = Node(1)
    node3 = Node(3)
    node4 = Node(0)
    node5 = Node(7)
    node6 = Node(9)
    node7 = Node(1)
    node8 = Node(8)
    node9 = Node(2)     
    node10 = Node(1)     
    node11 = Node(0)     
    node12 = Node(8)     
    node13 = Node(8)     
    node14 = Node(7)     
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node9
    node5.left = node10
    node5.right = node11
    node7.left = node12
    node7.right = node13
    node11.left = node14
    #root = Solution().connect(root)
    root = Solution().connectLevelOrder(root)
    cur = root
    while cur:
        pre = cur        
        while pre:
            print(pre.val, end='')
            pre = pre.next
        print("#", end='')
        cur = cur.left
    
         