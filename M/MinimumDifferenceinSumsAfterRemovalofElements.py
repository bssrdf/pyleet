'''

-Hard-

You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

 

Example 1:

Input: nums = [3,1,2]
Output: -1
Explanation: Here, nums has 3 elements, so n = 1. 
Thus we have to remove 1 element from nums and divide the array into two equal parts.
- If we remove nums[0] = 3, the array will be [1,2]. The difference in sums of the two parts will be 1 - 2 = -1.
- If we remove nums[1] = 1, the array will be [3,2]. The difference in sums of the two parts will be 3 - 2 = 1.
- If we remove nums[2] = 2, the array will be [3,1]. The difference in sums of the two parts will be 3 - 1 = 2.
The minimum difference between sums of the two parts is min(-1,1,2) = -1. 
Example 2:

Input: nums = [7,9,5,8,1,3]
Output: 1
Explanation: Here n = 2. So we must remove 2 elements and divide the remaining array into two parts containing two elements each.
If we remove nums[2] = 5 and nums[3] = 8, the resultant array will be [7,9,1,3]. The difference in sums will be (7+9) - (1+3) = 12.
To obtain the minimum difference, we should remove nums[1] = 9 and nums[4] = 1. The resultant array becomes [7,5,8,3]. The difference in sums of the two parts is (7+5) - (8+3) = 1.
It can be shown that it is not possible to obtain a difference smaller than 1.
 

Constraints:

nums.length == 3 * n
1 <= n <= 105
1 <= nums[i] <= 105



'''

from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        A, n = nums, len(nums)//3
        first, second, middle = [], [], []
        sum1, sum2, ans = 0, 0, float('inf')
        ref = {}
        for i in range(n):
            heapq.heappush(first, -A[i])
            sum1 += A[i]
        for i in range(n, 3*n):
            ref[i] = [A[i], i, False]
            heapq.heappush(second, ref[i])
            sum2 += A[i]
            if len(second) > n:
                x, j, _ = heapq.heappop(second)
                sum2 -= x
                ref[j] = [-x, j, False]
                heapq.heappush(middle, ref[j])               

        ans = min(ans, sum1-sum2)
        for i in range(n):  
            val = A[i+n]          
            if val < -first[0]:
                x = heapq.heappushpop(first, -val)
                sum1 += x + val
            ref[i+n][2] = True                      
            if val >= second[0][0]:                
                sum2 -= val
                x, j, t = heapq.heappop(middle)
                ref[j] = [-x, j, t]
                heapq.heappush(second, ref[j])
                sum2 += -x
            while second and second[0][2]:
                heapq.heappop(second) 
            while middle and middle[0][2]:
                heapq.heappop(middle)     
            ans = min(ans, sum1-sum2)
        return ans

    def minimumDifference2(self, nums: List[int]) -> int:
        A = nums
        n = len(A) // 3
        
        # Build pre_min using min-heap.
        pre_min, cur_min = [sum(A[:n])], sum(A[:n])
        pre_hp = [-x for x in A[:n]]
        heapq.heapify(pre_hp)
        for i in range(n, 2 * n):
            cur_pop = -heapq.heappop(pre_hp)
            cur_min -= cur_pop
            cur_min += min(cur_pop, A[i])
            pre_min.append(cur_min)
            heapq.heappush(pre_hp, -min(cur_pop, A[i]))          
        
        # Build suf_max.
        suf_max, cur_max = [sum(A[2*n:])], sum(A[2*n:])
        suf_hp = [x for x in A[2*n:]]
        heapq.heapify(suf_hp)        
        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heapq.heappop(suf_hp)
            cur_max -= cur_pop
            cur_max += max(cur_pop, A[i])
            suf_max.append(cur_max)
            heapq.heappush(suf_hp, max(cur_pop, A[i]))
        suf_max = suf_max[::-1]
        
        # Iterate over pre_min and suf_max and get the minimum difference.
        ans = float('inf')
        for a, b in zip(pre_min, suf_max):
            ans = min(ans, a - b)
        return ans 
                







    
if __name__ == "__main__":
    print(Solution().minimumDifference(nums = [3,1,2]))
    print(Solution().minimumDifference(nums = [7,9,5,8,1,3]))
    nums = [28,48,48,50,33,29,30,46,44,35,42,39,44,29,49,49,45,38,3,11,36,22,44,17,18,20,38,19,43,8,29,9,36,39,15,9,38,5,38,35,6,17,32,35,45,11,46,38]
    print(Solution().minimumDifference(nums = nums))
        