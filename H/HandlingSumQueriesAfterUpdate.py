'''
-Hard-
*Segment Tree*
*Lazy Propagation*
You are given two 0-indexed arrays nums1 and nums2 and a 2D array queries of queries. There are three types of queries:

For a query of type 1, queries[i] = [1, l, r]. Flip the values from 0 to 1 and from 1 to 0 in nums1 from index l to index r. Both l and r are 0-indexed.
For a query of type 2, queries[i] = [2, p, 0]. For every index 0 <= i < n, set nums2[i] = nums2[i] + nums1[i] * p.
For a query of type 3, queries[i] = [3, 0, 0]. Find the sum of the elements in nums2.
Return an array containing all the answers to the third type queries.

 

Example 1:

Input: nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
Output: [3]
Explanation: After the first query nums1 becomes [1,1,1]. After the second query, nums2 becomes [1,1,1], so the answer to the third query is 3. Thus, [3] is returned.
Example 2:

Input: nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
Output: [5]
Explanation: After the first query, nums2 remains [5], so the answer to the second query is 5. Thus, [5] is returned.
 

Constraints:

1 <= nums1.length,nums2.length <= 105
nums1.length = nums2.length
1 <= queries.length <= 105
queries[i].length = 3
0 <= l <= r <= nums1.length - 1
0 <= p <= 106
0 <= nums1[i] <= 1
0 <= nums2[i] <= 109

'''

from typing import List
# from collections import defaultdict

class segtree():
    def __init__(self, n, nums):
        # self.lazy = defaultdict(int)
        # self.len = defaultdict(int)
        # self.tree = defaultdict(int)
        self.lazy = [0]*(4*n)
        self.len = [0]*(4*n)
        self.tree = [0]*(4*n)
        # initial length and summation
        self.init_len(1, 0, n, nums)
        self.init_num(1, 0, n, nums)
        
    def init_len(self, ind, cl, cr, num):
        if cr < cl or cl >= len(num):
            return 
        if cr == cl:
            self.len[ind] = 1
            return 
        mid = (cl + cr) // 2
        # if cl != cr:
        self.init_len(ind*2, cl, mid, num)
        self.init_len(ind*2+1, mid+1, cr, num)
        self.len[ind] = self.len[ind*2] + self.len[ind*2+1]
    
    def init_num(self, ind, cl, cr, num):
        if cr < cl or cl >= len(num):
            return
        if cl == cr:
            self.tree[ind] = num[cl]
            return
        mid = (cl + cr) // 2
        # if cl != cr:
        self.init_num(ind*2, cl, mid, num)
        self.init_num(ind*2+1, mid+1, cr, num)
        
        self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
        
    
    def proplazy(self, ind):
        # if the parent node has the notation to flip, then we update all summation of children nodes.
        if self.lazy[ind]:
            self.lazy[ind*2] ^= self.lazy[ind]
            self.tree[ind*2] = self.len[ind*2] - self.tree[ind*2]
            self.lazy[ind*2 + 1] ^= self.lazy[ind]
            self.tree[ind*2 + 1] = self.len[ind*2+1] - self.tree[ind*2 + 1]
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
            self.lazy[ind] = 0
        
    def update(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 
        if ul <= cl and cr <= ur:
            # mark to flip
            self.lazy[ind] ^= 1
            self.tree[ind] = self.len[ind] - self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            self.update(ind*2, ul, ur, cl, mid)
            self.update(ind*2+1, ul, ur, mid+1, cr)
            self.tree[ind] = self.tree[ind*2] + self.tree[ind*2+1]
           
    def query(self, ind, ul, ur, cl, cr):
        if cl > ur or cr < ul:
            return 0
        if ul <= cl and cr <= ur:
            return self.tree[ind]
        else:
            mid = (cl + cr) // 2
            self.proplazy(ind)
            return self.query(ind*2, ul, ur, cl, mid) + self.query(ind*2+1, ul, ur, mid+1, cr)
         
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        seg = segtree(n, nums1)
        ans = []
        sums = sum(nums2)        
        for i, j, k in queries:
            if i == 1:
                seg.update(1, j, k, 0, n)
            if i == 2:
                sums += seg.tree[1] * j
            if i == 3:
                ans.append(sums)
        return ans
       



if __name__ == '__main__':
    # print(Solution().handleQuery(nums1 = [1,0,1], nums2 = [0,0,0], 
    #      queries = [[1,1,1],[2,1,0],[3,0,0]]))
    nums1 = [0,0,0,0,1,0,1,1,1]
    nums2 = [35,29,21,34,8,48,22,43,37]
    queries = [[1,4,7],[3,0,0],[2,27,0],[3,0,0],[1,0,3],[3,0,0],[2,6,0],[1,3,8],[2,13,0],[3,0,0],[3,0,0],[3,0,0],[2,2,0],[2,28,0],[3,0,0],[3,0,0],[2,25,0],[3,0,0],[3,0,0],[1,2,5]]
    print(Solution().handleQuery(nums1 = nums1, nums2 = nums2, 
         queries = queries))
    