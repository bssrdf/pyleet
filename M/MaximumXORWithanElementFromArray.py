'''

-Hard-

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].

The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.

Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

 

Example 1:

Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]
Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.
Example 2:

Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
 

Constraints:

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109


'''

from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node
    def increase(self, number, d):
        cur = self
        for i in range(30, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += d
    def findMax(self, number):
        cur, ans = self, 0
        for i in range(30, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child and cur.child[1-bit].go > 0:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            else:
                cur = cur.child[bit]
        return ans

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]
                
    def query(self, num):
        if not self.root: 
            return -1
        p, ans = self.root, 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                ans |= (1 << i)
            else:
                p = p[cur]
        return ans

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        # q = [(x[1],x[0],i) for i,x in enumerate(queries)]
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        # q.sort()

        j = 0
        root = TrieNode()
        ans = [0]*len(queries)
        for i,(x,m) in queries:
            while j < len(nums) and nums[j] <= m:
                root.increase(nums[j], 1)
                j += 1
            # print(j, m, x, i)
            if j == 0:
               ans[i] = -1
            else:
               ans[i] = root.findMax(x)
        return ans
    
    def maximizeXor2(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        ans = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            ans[i] = trie.query(x)
        return ans
            





if __name__ == "__main__":
    print(Solution().maximizeXor(nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]))
    print(Solution().maximizeXor(nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]))