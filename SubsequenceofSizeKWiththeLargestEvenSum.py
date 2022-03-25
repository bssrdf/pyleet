'''

-Medium-
*Sorting*

You are given an integer array nums and an integer k. Find the largest 
even sum of any subsequence of nums that has a length of k.

Return this sum, or -1 if such a sum does not exist.

A subsequence is an array that can be derived from another array by 
deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,1,5,3,1], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,5,3]. It has 
a sum of 4 + 5 + 3 = 12.
Example 2:

Input: nums = [4,6,2], k = 3
Output: 12
Explanation:
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.
Example 3:

Input: nums = [1,3,5], k = 1
Output: -1
Explanation:
No subsequence of nums with length 1 has an even sum.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= k <= nums.length


'''

from typing import List

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        ans, even, odd = 0, 0, 0

        if k == 1: 
            ans = -float('inf')
            for i in nums:
                if i % 2 == 0:
                    ans = max(ans, i)
            return ans if ans != -float('inf') else -1

        maxEvenEven, maxOddEven = -1, -1
        maxEvenOdd,  maxOddOdd = -1, -1
        sm = sum(nums[:k-1])
        even = sm if sm % 2 == 0 else 0
        odd = sm if sm % 2 == 1 else 0        
        for i in range(k-1):
            if nums[i] % 2 == 1: 
                if sm == odd:
                    maxOddOdd = max(maxOddOdd, nums[i])
                else:
                    maxOddEven = max(maxOddEven, nums[i])
            else:
                if sm == odd:
                    maxEvenOdd = max(maxEvenOdd, nums[i])
                else:
                    maxEvenEven = max(maxEvenEven, nums[i])
        # print(odd, even, maxOddOdd, maxOddEven, maxEvenEven, maxEvenOdd)
        l = 0
        for i in range(k-1, len(nums)):
            l = (odd + nums[i]) if nums[i] % 2 == 1 else even + nums[i]
            ans = max(ans, l)
            #print(i, nums[i], l, ans) 
            if nums[i] % 2 == 1:
                if maxOddEven != -1 and nums[i] > maxOddEven:
                   even += nums[i] - maxOddEven     
                   maxOddEven = nums[i]
                if maxOddOdd != -1 and nums[i] > maxOddOdd:
                   odd += nums[i] - maxOddOdd     
                   maxOddOdd = nums[i]   
            else:
                if maxEvenEven != -1 and nums[i] > maxEvenEven:
                   even += nums[i] - maxEvenEven     
                   maxEvenEven = nums[i]
                if maxEvenOdd != -1 and nums[i] > maxEvenOdd:
                   odd += nums[i] - maxEvenOdd     
                   maxEvenOdd = nums[i]   
        return ans
            
    def largestEvenSum2(self, nums: List[int], k: int) -> int:
        nums.sort()
        summ = sum(nums[-k:])
        if summ % 2 == 0:
            return summ

        minOdd = -1
        minEven = -1
        maxOdd = -1
        maxEven = -1

        for i in range(len(nums) - 1, len(nums) - k - 1, -1):
            if nums[i] & 1:
                minOdd = nums[i]
            else:
                minEven = nums[i]

        for i in range(len(nums) - k):
            if nums[i] & 1:
                maxOdd = nums[i]
            else:
                maxEven = nums[i]

        ans = -1

        if maxEven >= 0 and minOdd >= 0:
            ans = max(ans, summ + maxEven - minOdd)
        if maxOdd >= 0 and minEven >= 0:
            ans = max(ans, summ + maxOdd - minEven)
        return ans










if __name__ == "__main__":
    print(Solution().largestEvenSum(nums = [4,1,5,3,1], k = 3))
    print(Solution().largestEvenSum(nums = [4,6,2], k = 3))
    print(Solution().largestEvenSum(nums = [1,3,5], k = 1))
    print(Solution().largestEvenSum(nums = [4,1,10,5,7,4,20], k = 3))
    print('******************************')
    print(Solution().largestEvenSum2(nums = [4,1,5,3,1], k = 3))
    print(Solution().largestEvenSum2(nums = [4,6,2], k = 3))
    print(Solution().largestEvenSum2(nums = [1,3,5], k = 1))
    print(Solution().largestEvenSum2(nums = [4,1,10,5,7,4,20], k = 3))