'''

-Hard-
*Prefix Sum*

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 109 + 7.

The floor() function returns the integer part of the division.

 

Example 1:

Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
Example 2:

Input: nums = [7,7,7,7,7,7,7]
Output: 49
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105


'''

from typing import List
from collections import Counter
from itertools import accumulate

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        incs, counter=[0]*(max(nums)+1), Counter(nums)            # To store all the quotients increases; counter
        for num in counter:                                       # Loop over all the divisors
            for j in range(num, len(incs), num):                  # Loop over all the possible dividends where the quotient increases
                incs[j] += counter[num]                           # Increment the increases in quotients
        quots=list(accumulate(incs))                              # Accumulate the increases to get the sum of quotients
        print(incs, quots)
        return sum([quots[num] for num in nums]) % 1_000_000_007  # Sum up all the quotients for all the numbers in the list.


if __name__ == "__main__":
    print(Solution().sumOfFlooredPairs(nums = [2,5,9]))