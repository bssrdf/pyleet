'''

-Medium-

You are given a 0-indexed integer array nums.

We say that an integer x is expressible from nums if there exist some integers 0 <= index1 < index2 < ... < indexk < nums.length for which nums[index1] | nums[index2] | ... | nums[indexk] = x. In other words, an integer is expressible if it can be written as the bitwise OR of some subsequence of nums.

Return the minimum positive non-zero integer that is not expressible from nums.

 

Example 1:

Input: nums = [2,1]
Output: 4
Explanation: 1 and 2 are already present in the array. We know that 3 is expressible, since nums[0] | nums[1] = 2 | 1 = 3. Since 4 is not expressible, we return 4.
Example 2:

Input: nums = [5,3,2]
Output: 1
Explanation: We can show that 1 is the smallest number that is not expressible.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109


'''

from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        '''
        If 1 not in A,
        we return 1,
        otherwise we can have x = 1.

        If 2 not in A,
        we return 2.
        otherwise we can have x = 2.

        Since we can have x = 1 and x = 2,
        then we can have x = 1 | 2 = 3.

        If 4 not in A,
        we return 4,
        otherwise we have x = 4

        Since we can have x = 1 and x = 4, then we can have x = 1 | 4 = 5.
        Since we can have x = 2 and x = 4, then we can have x = 2 | 4 = 6.
        Since we can have x = 1,2,4, then we can have x = 1 | 2 | 4 = 7.

        So we can find the rule here,
        find out the minimum pow of 2,
        which is not in A.

        The process of prove is same as above.

        
        '''
        st = set(nums)
        ans = 1
        while True:
            if ans not in st:
                return ans
            ans *= 2


