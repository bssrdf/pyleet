'''
-Medium-

You are given an array of positive integers nums and want to erase a subarray 
containing unique elements. The score you get by erasing the subarray is equal 
to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence 
of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^4

'''

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        n = len(nums)
        m = set()
        curSum = 0
        left, right = 0, 0
        while right < n:
            while nums[right] in m:
                m.remove(nums[left])
                curSum -= nums[left]
                left += 1
            m.add(nums[right])
            curSum += nums[right]
            ans = max(ans, curSum) 
            right += 1
        return ans
        
if __name__ == "__main__":
    print(Solution().maximumUniqueSubarray([4,2,4,5,6]))
    print(Solution().maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))