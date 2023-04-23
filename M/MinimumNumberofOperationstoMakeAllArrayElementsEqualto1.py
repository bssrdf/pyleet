'''
-Medium-
*BFS*

You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.
 

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106


'''

from typing import List
from math import gcd, inf
from collections import deque,Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        que = deque([(nums,0)])
        visited = {tuple(nums)}
        while que:
            cur, steps = que.popleft()
            cnt = Counter(cur)            
            if cnt[1] > 0: return steps + n - cnt[1] 
            for i in range(n-1):
                if cur[i] == cur[i+1]: continue
                g = gcd(cur[i], cur[i+1])
                nxt = list(cur)
                nxt[i] = g
                nxttp = tuple(nxt)
                if nxttp not in visited:
                    visited.add(nxttp)
                    que.append((nxt, steps+1))
                nxt = list(cur)
                nxt[i+1] = g
                nxttp = tuple(nxt)
                if nxttp not in visited:
                    visited.add(nxttp)
                    que.append((nxt, steps+1))
        return -1



    def minOperations2(self, nums: List[int]) -> int:
        n = len(nums)
        ones = Counter(nums)
        if ones[1] > 0: return n - ones[1]
        ans = inf
        for i in range(n):
            g = nums[i]
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    ans = min(ans, j-i+n-1)
        return ans if ans != inf else -1 

        




    
                

        



if __name__ == '__main__':
    print(Solution().minOperations(nums = [2,6,3,4]))
    print(Solution().minOperations(nums = [2,10,6,14]))
    # print(Solution().minOperations(nums = [2,10,6,14]))
    nums = [811340,393975,627577,26811,209797,500958,637753,592871,449081,216228,498803,730546,937075,122352,610619,921594,47754,242342,726157]
    print(Solution().minOperations(nums = nums))
    print(Solution().minOperations2(nums = nums))