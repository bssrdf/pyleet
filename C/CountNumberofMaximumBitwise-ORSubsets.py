'''

-Medium-

Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 

Constraints:

1 <= nums.length <= 16
1 <= nums[i] <= 105



'''

from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        A = nums
        n = len(A)        
        res = [[], [0]]
        for i in range(1,n):
            tmp = []
            for j in range(1<<(i-1)):
                tmp.append(res[-(j+1)][:-1]+[i])
                tmp.append(res[-(j+1)]+[i])
            res += tmp   
        ans, mx = 0, 0 
        for i in range(1, len(res)):
            subs = res[i]
            sm = A[subs[0]]
            for j in range(1, len(subs)):
                sm = sm | A[subs[j]] 
            if sm > mx:
                mx, ans = sm, 1
            elif sm == mx:
                ans += 1
        return ans
                

    
if __name__ == "__main__":
    print(Solution().countMaxOrSubsets(nums = [3,2,1,5]))
        
