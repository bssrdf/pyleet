'''

-Medium-
*Greedy*
*Binary Search*

You are given a 0-indexed integer array nums and an integer p. Find p pairs of indices of nums such that the maximum difference amongst all the pairs is minimized. Also, ensure no index appears more than once amongst the p pairs.

Note that for a pair of elements at the index i and j, the difference of this pair is |nums[i] - nums[j]|, where |x| represents the absolute value of x.

Return the minimum maximum difference among all p pairs.

 

Example 1:

Input: nums = [10,1,2,7,1,3], p = 2
Output: 1
Explanation: The first pair is formed from the indices 1 and 4, and the second pair is formed from the indices 2 and 5. 
The maximum difference is max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1. Therefore, we return 1.
Example 2:

Input: nums = [4,2,1,2], p = 1
Output: 0
Explanation: Let the indices 1 and 3 form a pair. The difference of that pair is |2 - 2| = 0, which is the minimum we can attain.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= p <= (nums.length)/2


'''
from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # To solve mini-max problem,
        # we can apply binary search.
        A, n = nums, len(nums)
        A.sort()
        l, r = 0, A[-1]-A[0]+1
        def possible(m):
            t, i = 0, 1
            while i < n:
                # once we determined a threshold m, we can greedily pair A[i] and A[i-1] 
                # if their diff is <= m, a new pair is found  
                
                # Why being greedy works?

                # Imagine you have [a,b,c,d], abcd are just sorted numbers

                # Greedy tells us if b - a < the threshold we set, we just pick it. 
                # The cost of doing this is if c - b < threshold as well, you can never 
                # pick bc pair anymore because b has been paired with a.

                # Will this cause any problems?

                # The answer is no

                # Because if you pick ab pair, you will have one pair now. If you pick 
                # bc pair, you also have one pair, however, if you pick bc now 
                # what's left is [a, d]. Because we have sorted abcd, d - a is likely 
                # to be bigger so it is more likely to exceed the threshold we set.
                # On the other hand, if we greedily pick ab pair, what's left is [c,d] 
                # and d - c is guaranteed to be smaller or equal to d - a, so d-c is 
                # more likely to be a pair that we can pick as well -> being greedy 
                # (pick a and b) is more likely to let us have more pairs then not 
                # being greedy (pick b and c). Hence for this problem, greedy works

                if A[i]-A[i-1] <= m:
                    t += 1
                    i += 2
                else:
                    i += 1
            return t >= p  
            
        while l < r:
            mid = l + (r-l)//2
            if possible(mid):
                r = mid
            else:
                l = mid + 1
        return l



if __name__ == '__main__':
    print(Solution().minimizeMax(nums = [10,1,2,7,1,3], p = 2))
    print(Solution().minimizeMax(nums = [4,2,1,2], p = 1))
    print(Solution().minimizeMax(nums = [3,4,2,3,2,1,2], p = 3))