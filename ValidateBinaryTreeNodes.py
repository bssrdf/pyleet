'''
-Medium-

You have n binary tree nodes numbered from 0 to n - 1 where node i has 
two children leftChild[i] and rightChild[i], return true if and only if 
all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly 
for the right child.

Note that the nodes have no values and that we only use the node 
numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
Example 4:


Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false
 

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1

'''


from typing import List

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        L, R = leftChild, rightChild
        parent = [-1]*n
        for i in range(n):
            if L[i] != -1:
                if parent[L[i]] == -1:
                    if parent[i] == L[i]: return False                     
                    parent[L[i]] = i 
                else:
                    return False
            if R[i] != -1:
                if parent[R[i]] == -1:
                    if parent[i] == R[i]: return False                     
                    parent[R[i]] = i 
                else:
                    return False
        #print(parent)
        root = -1            
        for i in range(n):
            if parent[i] == -1:
                if root == -1:
                    root = i
                else: 
                    return False            
        if root == -1: return False
        def dfs(root):
            if root == -1: return 0
            return 1 + dfs(L[root]) + dfs(R[root])
        return dfs(root) == n
      
if __name__ == "__main__":
    print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]))
    print(Solution().validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]))
    print(Solution().validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1]))
    print(Solution().validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]))
    print(Solution().validateBinaryTreeNodes(4, [1,2,0,-1], [-1,-1,-1,-1]))