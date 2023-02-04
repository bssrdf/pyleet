'''
-Medium-

Given an array of integers nums and an integer k. A continuous subarray is called nice if 
there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length


'''

from typing import List

from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        def atMostK(m):
            ret = 0
            left, right = 0, 0
            cnt = 0
            while right < n:
                if nums[right] % 2:
                    cnt += 1
                right += 1
                while left < right and cnt > m:
                    if nums[left] % 2:
                        cnt -= 1
                    left += 1
                ret += left
            return ret
        #i, j = atMostK(k), atMostK(k-1)   
        #print(i,j) 
        #return j-i
        return atMostK(k-1) - atMostK(k)
            
            

    
if __name__ == "__main__":    
    print(Solution().numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
    print(Solution().numberOfSubarrays(nums = [2,4,6], k = 1))
    print(Solution().numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))