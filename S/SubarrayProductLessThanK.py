'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product 
of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: 
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not 
strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.


'''

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = right = 0
        ans, prod = 0, 1                
        while right < n:            
            prod *= nums[right]        
            # check left < n since left is moving
            while prod >= k and left < n:
                prod /= nums[left]
                left += 1                
            if left <= right:
                ans += right-left+1   
            right += 1              
        return ans

if __name__ == "__main__":
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(Solution().numSubarrayProductLessThanK([1,2,3], 0))


