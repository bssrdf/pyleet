'''

-Hard-
*Trie*



You are given a 0-indexed integer array nums. A pair of integers x and y is called a strong pair if it satisfies the condition:

|x - y| <= min(x, y)
You need to select two integers from nums such that they form a strong pair and their bitwise XOR is the maximum among all strong pairs in the array.

Return the maximum XOR value out of all possible strong pairs in the array nums.

Note that you can pick the same integer twice to form a pair.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: 7
Explanation: There are 11 strong pairs in the array nums: (1, 1), (1, 2), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (3, 5), (4, 4), (4, 5) and (5, 5).
The maximum XOR possible from these pairs is 3 XOR 4 = 7.
Example 2:

Input: nums = [10,100]
Output: 0
Explanation: There are 2 strong pairs in the array nums: (10, 10) and (100, 100).
The maximum XOR possible from these pairs is 10 XOR 10 = 0 since the pair (100, 100) also gives 100 XOR 100 = 0.
Example 3:

Input: nums = [500,520,2500,3000]
Output: 1020
Explanation: There are 6 strong pairs in the array nums: (500, 500), (500, 520), (520, 520), (2500, 2500), (2500, 3000) and (3000, 3000).
The maximum XOR possible from these pairs is 500 XOR 520 = 1020 since the only other non-zero XOR value is 2500 XOR 3000 = 636.
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 220 - 1



'''


from typing import List

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, value):
        self.traverse_and_apply(value, 1)
    
    def delete(self, value):
        self.traverse_and_apply(value, -1)
        
    def traverse_and_apply(self, value, increment):
        bit_string = self.convert(value)
        curr_node = self.root
        for bit in bit_string:
            bit = int(bit)

            if curr_node.children[bit] is None:
                curr_node.children[bit] = TrieNode()
            
            curr_node = curr_node.children[bit]
            curr_node.count += increment
    
    def find_max(self, value):
        bit_string = self.convert(value)
        curr_node = self.root
        result = 0
        for bit in bit_string:
            bit = int(bit)
            complement = curr_node.children[1 - bit]
            if complement != None and complement.count > 0:
                curr_node = complement
                result = 2 * result + 1
            elif curr_node.children[bit] != None and curr_node.children[bit].count > 0:
                curr_node = curr_node.children[bit]
                result = 2 * result
        return result
    
    def convert(self, value):
        # bit_string = bin(value)[2:]
        # if len(bit_string) < 20:
        #     bit_string = "0" * (20 - len(bit_string)) + bit_string
        # return bit_string
        return format(value, '020b')

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        A = nums
        res = 0
        for i in range(20, -1, -1):
            # 0011 -> 00110 Shift left
            res <<= 1
            pref, pref2 = {}, {}
            for a in A:
                p = a >> i
                if p not in pref:
                    pref[p] = pref2[p] = a
                pref[p] = min(pref[p], a)
                pref2[p] = max(pref2[p], a)
            for x in pref:
                # greedy guess
                y = res ^ 1 ^ x
                if x >= y and y in pref and pref[x] <= pref2[y] * 2:
                    # 00110 -> 00111 Add one to last bit
                    res |= 1
                    break
        return res
    
    def maximumStrongPairXor2(self, nums: List[int]) -> int:
        nums.sort()
        i = j = result = 0
        trie = Trie()
        for j in range(len(nums)):
            trie.insert(nums[j])
            while i < j and nums[j] - nums[i] > nums[i]:
                trie.delete(nums[i])
                i += 1
            result = max(result, trie.find_max(nums[j]))
        return result



if __name__ == "__main__":
    print(Solution().maximumStrongPairXor(nums = [1,2,3,4,5]))