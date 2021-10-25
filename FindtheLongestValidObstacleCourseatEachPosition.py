'''

-Hard-

You want to build some obstacle courses. You are given a 0-indexed integer array 
obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest 
obstacle course in obstacles such that:

You choose any number of obstacles between 0 and i inclusive.
You must include the ith obstacle in the course.
You must put the chosen obstacles in the same order as they appear in obstacles.
Every obstacle (except the first) is taller than or the same height as the obstacle 
immediately before it.
Return an array ans of length n, where ans[i] is the length of the longest obstacle 
course for index i as described above.

 

Example 1:

Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.
Example 2:

Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.
Example 3:

Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.
 

Constraints:

n == obstacles.length
1 <= n <= 10^5
1 <= obstacles[i] <= 10&7


'''

from typing import List
import bisect

class MaxBIT:  # One-based indexing
    def __init__(self, size):
        self.bit = [0] * (size + 1)
    def get(self, idx):
        ans = 0
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & (-idx)
        return ans
    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & (-idx)


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        nums = obstacles
        lis = []
        for i, x in enumerate(nums):
            if len(lis) == 0 or lis[-1] <= x:  # Append to LIS if new element is >= last element in LIS
                lis.append(x)
                nums[i] = len(lis)
            else:
                idx = bisect.bisect_right(lis, x)  # Find the index of the smallest number > x
                lis[idx] = x  # Replace that number with x
                nums[i] = idx + 1
        return nums

    def longestObstacleCourseAtEachPosition2(self, nums: List[int]) -> List[int]:
        def compress(arr):  # For example: arr = [1, 9999, 20, 10, 20]
            uniqueSorted = sorted(set(arr))
            for i in range(len(arr)): 
                arr[i] = bisect.bisect_left(uniqueSorted, arr[i]) + 1  # Result: arr = [1, 4, 3, 2, 3]
            return len(uniqueSorted)
        
        nUnique = compress(nums)
        bit = MaxBIT(nUnique)
        for i, x in enumerate(nums):
            nums[i] = bit.get(x) + 1
            bit.update(x, nums[i])
        return nums

if __name__ == "__main__":
    print(Solution().longestObstacleCourseAtEachPosition([3,1,5,6,4,2]))