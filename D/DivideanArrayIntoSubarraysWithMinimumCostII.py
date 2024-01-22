'''

-Hard-

You are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous 
subarrays
, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

 

Example 1:

Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.
Example 2:

Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.
Example 3:

Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.
 

Constraints:

3 <= n <= 105
1 <= nums[i] <= 109
3 <= k <= n
k - 2 <= dist <= n - 2

'''
from typing import List
import heapq

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        A = nums
        n = len(A)
        B = [ (v,i) for (i,v) in enumerate(A)]
        B.sort()
        mp = {}
        for i in range(n):
            mp[B[i][1]] = i 
        bits = [0]*(n+1)
        cnts = [0]*(n+1)
        def update(arr, i, x):
            while i <= n:
                arr[i] += x
                i += i & (-i)
        def query(arr, i):
            t = 0
            while i > 0:
                t += arr[i]
                i -= i & (-i)
            return t            

        for i in range(1, dist+2):
            update(bits, mp[i]+1, A[i])
            update(cnts, mp[i]+1, 1)
        def find():
            l, r = 1, n+1
            while l < r:
                mid = l + (r -l)//2
                d = query(cnts, mid) 
                if d == k-1:
                    return mid
                elif d < k-1:
                    l = mid + 1
                else:
                    r = mid 
            return l-1
        ans = A[0] + query(bits, find())
        for i in range(2, n-dist):
            update(bits, mp[i-1]+1, -A[i-1])
            update(cnts, mp[i-1]+1, -1)
            update(bits, mp[i+dist]+1, A[i+dist])
            update(cnts, mp[i+dist]+1, 1)
            ans = min(ans, A[0] + query(bits, find()))
        return ans    
                      

if __name__ == "__main__":      
    print(Solution().minimumCost(nums = [1,3,2,6,4,2], k = 3, dist = 3))
    print(Solution().minimumCost(nums = [10,1,2,2,2,1], k = 4, dist = 3))
    print(Solution().minimumCost(nums = [10,8,18,9], k = 3, dist = 1))
    print(Solution().minimumCost(nums = [2,6,3,5], k = 3, dist = 1))