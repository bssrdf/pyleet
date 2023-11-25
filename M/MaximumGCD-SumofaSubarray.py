'''
-Hard-

You are given an array of integers nums and an integer k.

The gcd-sum of an array a is calculated as follows:

Let s be the sum of all the elements of a.
Let g be the greatest common divisor of all the elements of a.
The gcd-sum of a is equal to s * g.
Return the maximum gcd-sum of a subarray of nums with at least k elements.

 

Example 1:

Input: nums = [2,1,4,4,4,2], k = 2
Output: 48
Explanation: We take the subarray [4,4,4], the gcd-sum of this array is 4 * (4 + 4 + 4) = 48.
It can be shown that we can not select any other subarray with a gcd-sum greater than 48.
Example 2:

Input: nums = [7,3,9,4], k = 1
Output: 81
Explanation: We take the subarray [9], the gcd-sum of this array is 9 * 9 = 81.
It can be shown that we can not select any other subarray with a gcd-sum greater than 81.
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= 106
1 <= k <= n

'''

from typing import List

from math import gcd, log
from itertools import accumulate

class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        s = list(accumulate(nums, initial=0))
        f = []
        ans = 0
        l = 0
        # for fixed index i, the value of GCD(i, j) will be decreasing 
        # as GCD(i, j) >= GCD(i, j + 1). Also, because GCD(i, j + 1) must 
        # be equal or divisor of GCD(i, j), the number of distinct value X 
        # of GCD(i, j), GCD(i, j + 1), ..., GCD(i, N) will satisfies 2^X <= A[i].
        # or X <= log2(A[i])
        for i, v in enumerate(nums):
            g = []
            for j, x in f:
                y = gcd(x, v)
                if not g or g[-1][1] != y:
                    g.append((j, y))
            # print(i,v, g, f)
            f = g
            f.append((i, v))
            if len(f) > l:
                l = len(f)
                print(f)
            for j, x in f:
                if i - j + 1 >= k:
                    ans = max(ans, (s[i + 1] - s[j]) * x)
        print('max len of f', l,f )            
        print('k, max(A), idx(max(A)), log2(max(A)', k, max(nums), nums.index(max(nums)), log(max(nums),2))        
        return ans

from random import randint
if __name__ == "__main__":
    print(Solution().maxGcdSum(nums = [2,1,4,4,4,2], k = 2))
    N = 10**4
    M = 10**5
    nums = [randint(1, M) for i in range(N)]
    k = randint(1, N)
    print('k= ', k)
    nums= [99987]+nums
    k = N
    print(Solution().maxGcdSum(nums = nums, k = k))

