'''
-Hard-
*Trie*


Given a (0-indexed) integer array nums and two integers low and high, return the number of nice pairs.

A nice pair is a pair (i, j) where 0 <= i < j < nums.length and low <= (nums[i] XOR nums[j]) <= high.

 

Example 1:

Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
Explanation: All nice pairs (i, j) are as follows:
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
Example 2:

Input: nums = [9,8,4,2,1], low = 5, high = 14
Output: 8
Explanation: All nice pairs (i, j) are as follows:
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 2 * 104
1 <= low <= high <= 2 * 104


'''

from typing import List

class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node
    def increase(self, number, d):
        cur = self
        for i in range(15, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += d
    def find(self, number, k):
        cur, ans = self, 0
        for i in range(15, -1, -1):
            if not cur: break
            bitx = (number >> i) & 1
            bitk = (k >> i) & 1
            # if bitk == 0, we know all nodes that have different bit value as 
            # "number" will result something larger so we can ignore all those and 
            # only traverse the sub-trie that has the same value as "bitx" (which,
            # after xor, will result this digit to be zero)
            if bitk == 0: 
                cur = cur.child.get(bitx, None)
                continue
            # if bitk == 1, then we know that all nodes having the same bit value as "number" 
            # will result this digit to be 0 after xor, which are guaranteed to 
            # be smaller than "k", so we can add all of those nodes and move 
            # onto the sub-trie that have different value than "bitx" (1^bit is 
            # just a fancier way to say "change 0 to 1 and change 1 to 0")
            if bitx in cur.child:
                ans += cur.child[bitx].go
            cur = cur.child.get(1-bitx, None)
        return ans


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trieNode = TrieNode()
        ans = 0
        for x in nums:
            print('x',x)
            ans += trieNode.find(x, high+1) - trieNode.find(x, low)
            trieNode.increase(x, 1)
        return ans

        
    
if __name__ == "__main__":
    print(Solution().countPairs(nums = [1,4,2,7], low = 2, high = 6))