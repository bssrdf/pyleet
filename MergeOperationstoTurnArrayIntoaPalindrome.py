'''

-Medium-
$$$
*Two Pointers*
*Greedy*

You are given an array nums consisting of positive integers.

You can perform the following operation on the array any number of times:

Choose any two adjacent elements and replace them with their sum.
For example, if nums = [1,2,3,1], you can apply one operation to make it [1,5,1].
Return the minimum number of operations needed to turn the array into a palindrome.

 

Example 1:

Input: nums = [4,3,2,1,2,3,1]
Output: 2
Explanation: We can turn the array into a palindrome in 2 operations as follows:
- Apply the operation on the fourth and fifth element of the array, nums becomes equal to [4,3,2,3,3,1].
- Apply the operation on the fifth and sixth element of the array, nums becomes equal to [4,3,2,3,4].
The array [4,3,2,3,4] is a palindrome.
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We do the operation 3 times in any position, we obtain the array [10] at the end which is a palindrome.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106


'''

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        A, n = nums, len(nums)
        i, j, ans = 0, n-1, 0
        a, b = A[i], A[j]
        while i < j:
            if a == b:
                i += 1
                j -= 1
                a, b = A[i], A[j]
            elif a < b:
                i += 1
                a += A[i]
                ans += 1
            else:
                j -=1 
                b += A[j]
                ans += 1

        return ans





if __name__ == "__main__":
    print(Solution().minimumOperations(nums = [4,3,2,1,2,3,1]))
    print(Solution().minimumOperations(nums = [4,3,2,1]))

