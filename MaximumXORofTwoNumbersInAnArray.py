'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''



class Solution(object):
    def findMaximumXOR(self, nums):
        Trie = {}
        for x in nums:
            cur = Trie
            for bit in format(x, '032b'):
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
            cur[''] = x
            if x == 10:
                print(Trie)
             
        def matchMaxXOR(x):
            cur = Trie
            for bit in format(x, '032b'):
                rev = '0' if bit == '1' else '1'
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]
            return cur['']
         
        res = 0
        for x in nums:
            res = max(res, x ^ matchMaxXOR(x))
         
        return res

if __name__ == "__main__":
    print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))
