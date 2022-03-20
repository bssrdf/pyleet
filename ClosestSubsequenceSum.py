'''

-Hard-
*DP*
*Bitmask*
*Two Pointers*


You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements 
is the closest possible to goal. That is, if the sum of the subsequence's 
elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements 
(possibly all or none) of the original array.

 

Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
Example 2:

Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
Example 3:

Input: nums = [1,2,3], goal = -7
Output: 7
 

Constraints:

1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109


'''

from typing import List
import bisect

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        # function that generates all possible sums of sebsequences
        def dfs(i,cur,arr,sums):
            if i==len(arr):
                sums.add(cur)
                return
            dfs(i+1,cur,arr,sums)
            dfs(i+1,cur+arr[i],arr,sums)
        
        sums1,sums2=set(),set()
        # generate all possible sums of the 1st and 2nd half 
        dfs(0,0,nums[:len(nums)//2],sums1)
        dfs(0,0,nums[len(nums)//2:],sums2)
        
        # sort the possible sums of the 2nd half
        s2=sorted(sums2)
        ans=10**10
        # for each possible sum of the 1st half, find the sum in the 2nd half
        # that gives a value closest to the goal using binary search
        for s in sums1:
            remain=goal-s
			# binary search for the value in s2 that's closest to the remaining value
            i2=bisect.bisect_left(s2,remain)
            if i2<len(s2):
                ans=min(ans,abs(remain-s2[i2]))
            if i2>0:
                ans=min(ans,abs(remain-s2[i2-1]))
        return ans
    
    def minAbsDifference2(self, nums: List[int], goal: int) -> int:
        # TLE
        n = len(nums)
        m = n // 2 if n % 2 == 0 else n//2+1
        #nums.sort()
        #A, B = nums[::2], nums[1::2]
        A, B = nums[:m], nums[m:]
        #print(A, B)
        sumA = set()
        for mask in range((1<<len(A))):
            x = 0
            for i in range(len(A)):
                if mask & (1<<i) > 0:
                    x += A[i]
            sumA.add(x)
        s1 = sorted(sumA)
        #print(sumA)
        ans = float('inf')
        sumB = set()
        for mask in range((1<<len(B))):
            x = 0
            for i in range(len(B)):
                if mask & (1<<i) > 0:
                    x += B[i]
            sumB.add(x)

        for x in sumB:
            remain = goal - x 
            idx = bisect.bisect_left(s1, remain)            
            if idx < len(s1):
                ans = min(ans, abs(remain-s1[idx]))   
            if idx > 0:
                ans = min(ans, abs(remain-s1[idx-1]))   
            #print('idx', idx, x, goal-x, sumA[idx] if 0<=idx<len(sumA) else 0, ans)
        return ans

            
            




        

if __name__ == "__main__":
    # print(Solution().minAbsDifference(nums = [5,-7,3,5], goal = 6))
    # print(Solution().minAbsDifference(nums = [7,-9,15,-2], goal = -5))
    # print(Solution().minAbsDifference(nums = [1,2,3], goal = -7))
    # print(Solution().minAbsDifference([9152249,8464156,-2493402,8990685,-7257152,-1050240,2243737,-82901,8939692], 26915229))
    print(Solution().minAbsDifference([1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,-8192,-16384,-32768,-65536,-131072,-262144,-524288], 1048574))
