'''

-Medium-

You are given an integer array nums and an integer k. Append k unique positive integers 
that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

 

Example 1:

Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 108



'''


from typing import List
class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted({0} | set(nums))
        n = len(nums)
        # print(nums)
        ans = 0        
        def sums(a,b):
            return (b*(b+1) - a*(a-1))>>1
        for i in range(1, n):
            if nums[i] - nums[i-1] <= 1: continue
            # if nums[i] != i:
            m = nums[i] - nums[i-1] - 1
            if m <= k:
                k -= m                    
                a, b = nums[i-1]+1, nums[i]-1
                ans += sums(a, b)
                if k == 0: return ans
            else: #m > k
                a, b = nums[i-1]+1, nums[i-1]+k 
                ans += sums(a, b)
                return ans
        a, b = nums[-1]+1, nums[-1]+k 
        ans += sums(a, b)
        return ans

if __name__ == "__main__":
    print(Solution().minimalKSum(nums = [1,4,25,10,25], k = 2))
    print(Solution().minimalKSum(nums = [5,6], k = 6))
    print(Solution().minimalKSum(nums = [53,41,90,33,84,26,50,32,63,47,66,43,29,88,71,28,83], k=76))
    print(Solution().minimalKSum([96,44,99,25,61,84,88,18,19,33,60,86,52,19,32,47,35,50,94,17,29,98,22,21,72,100,40,84], 35))
    print(Solution().minimalKSum([21,63,1,98,10,77,58,10,21,99,40,27,5,67,90,29,56,16,34,25,26,17,8,3,4,17,14,32,12,17,37,81,18,49,59,23,63,39,64,7,18,35,89,11,42,30,6,15,81,52,24,39,48,9,19,34,24,2,28,13,53,4,22,20,42,2,5,58,36,31,60,38,33], 20))