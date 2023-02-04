'''

-Medium-
$$$
*Monotonic Stack*
*Recursion*

You are given a 0-indexed integer array order of length n, a permutation of integers from 1 to n representing the order of insertion into a binary search tree.

A binary search tree is defined as follows:

<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>

<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>

<li>Both the left and right subtrees must also be binary search trees.</li>
The binary search tree is constructed as follows:

<li><code>order[0]</code> will be the <strong>root</strong> of the binary search tree.</li>

<li>All subsequent elements are inserted as the <strong>child</strong> of <strong>any</strong> existing node such that the binary search tree properties hold.</li>
Return the depth of the binary search tree.

A binary tree's depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
Input: order = [2,1,4,3]

Output: 3

Explanation: The binary search tree has a depth of 3 with path 2->3->4.

Example 2:

Input: order = [2,1,3,4]

Output: 3

Explanation: The binary search tree has a depth of 3 with path 2->3->4.


Input: order = [1,2,3,4]

Output: 4

Explanation: The binary search tree has a depth of 4 with path 1->2->3->4.

 

Constraints:

<li><code>n == order.length</code></li>

<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>

<li><code>order</code> is a permutation of integers between <code>1</code> and <code>n</code>.</li>
'''

from typing import List
from sortedcontainers import SortedDict
import math

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        if not order: return 0
        if len(order) == 1: return 1
        i = 1
        while i < len(order) and order[i] < order[0]:
            i += 1 
        return 1+max(self.maxDepthBST(order[1:i]), self.maxDepthBST(order[i:]))     
    

    def maxDepthBST2(self, order: List[int]) -> int:
        n, stack = len(order), []
        firstGreaterRight = [n]*n
        for i in range(n):
            while stack and order[stack[-1]] < order[i]:
                firstGreaterRight[stack[-1]] = i
                stack.pop()
            stack.append(i)
        # print(firstGreaterRight)
        def helper(i, j):
            if i > j: return 0
            if i == j: return 1
            return 1+max(helper(i+1, firstGreaterRight[i]-1),
                         helper(firstGreaterRight[i], j))

        return helper(0, n-1)   

    def maxDepthBST3(self, order: List[int]) -> int:
        
        sd = SortedDict({0: 0, math.inf: 0, order[0]: 1})
        ans = 1
        for v in order[1:]:
            lower = sd.bisect_left(v) - 1
            higher = lower + 1
            depth = 1 + max(sd.values()[lower], sd.values()[higher])
            ans = max(ans, depth)
            sd[v] = depth
        return ans 

        

from random import randint
import time

if __name__ == '__main__':   
    print(Solution().maxDepthBST(order = [2,1,4,3]))
    print(Solution().maxDepthBST2(order = [2,1,4,3]))
    print(Solution().maxDepthBST(order = [2,1,3,4]))
    print(Solution().maxDepthBST2(order = [2,1,3,4]))
    print(Solution().maxDepthBST(order = [1,2,3,4]))
    print(Solution().maxDepthBST2(order = [1,2,3,4]))
    N = 80000
    order = []
    def generate(i, j):
        if i > j : return 
        k = randint(i, j)
        order.append(k)
        generate(i, k-1)
        generate(k+1, j)
    generate(1, N)
    print('len', len(order))
    assert len(order) == N
    starttime = time.time()
    print(Solution().maxDepthBST(order = order))
    print("elapsed {}s".format(time.time()-starttime))
    starttime = time.time()
    print(Solution().maxDepthBST2(order = order))
    print("elapsed {}s".format(time.time()-starttime))
    starttime = time.time()
    print(Solution().maxDepthBST3(order = order))
    print("elapsed {}s".format(time.time()-starttime))
