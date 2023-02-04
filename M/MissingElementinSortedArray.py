'''

-Medium-
*Binary Search*

Given a sorted array A of unique numbers, find the K-th missing number starting from the 
leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,…], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,…], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8


'''

from typing import List

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0

        diff = nums[-1] - nums[0] + 1 # complete length
        missing = diff - len(nums) # complete length - real length
        if k > missing: # if k is larger than the number of mssing words in sequence
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing # KEY: move left forward, we need to minus the missing words of this range
            else:
                right = mid
                
        return nums[left] + k # k should be between left and right index in the end
    
    
    
    
if __name__ == "__main__":
    print(Solution().missingElement([4,7,9,10], 1))
    print(Solution().missingElement([4,7,9,10], 3))
        
