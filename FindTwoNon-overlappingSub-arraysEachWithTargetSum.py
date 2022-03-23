'''
-Medium-
        
*Sliding Window*
*DP*
*Binary Search*

You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum 
equal target. There can be multiple answers so you have to find an answer 
where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, 
or return -1 if you cannot find such two sub-arrays.

 

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
Example 2:

Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
Example 3:

Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 1000
1 <= target <= 108


'''
from typing import List
import bisect
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n, sums, left, right = len(arr), 0, 0, 0
        ans, intervals, min_sofar = float('inf'), [-1], [float('inf')]
        while right < n:
            sums += arr[right]            
            while sums > target:
                sums -= arr[left]
                left += 1
            if sums == target: # sliding window to get the interval
                lth = right-left+1
                # binary search the index where all intervals prior are not overlapping
                idx = bisect.bisect_left(intervals, left)
                if idx-1 >= 0:
                    ans = min(ans, lth + min_sofar[idx-1])
                intervals.append(right) # the intervals are added in an ascending order so 
                                        # binary search could work
                min_sofar.append(min(min_sofar[-1], lth)) # dp saves the minimum length 
                                                          # since the first interval
            right += 1
        return -1 if ans == float('inf') else ans
        





if __name__ == "__main__":
    print(Solution().minSumOfLengths(arr = [3,2,2,4,3], target = 3))
    print(Solution().minSumOfLengths(arr = [7,3,4,7], target = 7))
    print(Solution().minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))
    print(Solution().minSumOfLengths(arr = [1,6,1], target = 7))
    print(Solution().minSumOfLengths(arr = [1,2,2,3,2,6,7,2,1,4,8], target = 5))
    print(Solution().minSumOfLengths(arr = [64,5,20,9,1,39], target = 69))