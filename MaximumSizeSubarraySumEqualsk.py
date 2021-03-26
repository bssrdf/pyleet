'''
-Medium-

*Prefix Sum*

*Hash Table*

Given an array nums and a target value k, find the maximum length of a 
subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit 
signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?

'''
from collections import defaultdict

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        """
        Note:
        this question is different from sliding window problem which we use 
        two pointers to solve
        sliding window: all elements > 0 && find range >=s
        this problem: find exactly value ---> hash map
        """
        n = len(nums)       
        dic = {}
        ans, sums = 0, 0               
        for i in range(n):
            sums += nums[i]
            if sums == k: ans = i+1
            elif sums-k in dic:                
                ans = max(ans, i-dic[sums-k])
            elif sums not in dic:
                dic[sums] = i # for duplicated sums, only record the first occurance   
                              # because the longest dist will be from it  
        return ans

if __name__ == "__main__":
    print(Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3))
    print(Solution().maxSubArrayLen([-2, -1, 2, 1], 1))
