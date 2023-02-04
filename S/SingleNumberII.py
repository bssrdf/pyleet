'''
-Medium-

Given an integer array nums where every element appears three times except for one, 
which appears exactly once. Find the single element and return it.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.

'''

class Solution(object):
    def singleNumberSlow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
            sm = 0
            for j in nums:
                sm += (j >> i) & 1
            ans |= (sm % 3) << i
        return ans-2**32 if ans >= 2**31 else ans

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0; two = 0; three = 0
        for i in range(len(nums)):
            two |= one & nums[i]
            one ^= nums[i]
            three = one & two
            one &= ~three
            two &= ~three
        return one
    def singleNumberGeneral(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 3
        bitCount = [0]*32     
        for j in range(len(nums)):
            n = nums[j]
            for i in range(32): 
                hasBit = (n & (1 << i)) != 0
                if hasBit:
                    bitCount[i] = (bitCount[i] + 1) % k
        exept = 0
        for i in range(32): 
            if bitCount[i] > 0:
                exept |= (1 << i)
        return exept-2**32 if exept >= 2**31 else exept
            

if __name__ == "__main__":
    print(Solution().singleNumberSlow([0,1,0,1,0,1,99]))
    print(Solution().singleNumberSlow([-2,-2,1,1,4,1,4,4,-4,-2]))
    print(Solution().singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))
    print(Solution().singleNumberGeneral([-2,-2,1,1,4,1,4,4,-4,-2]))
