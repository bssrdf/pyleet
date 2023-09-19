'''



-Hard-


You are given a 1-indexed array nums of n integers.

A set of numbers is complete if the product of every pair of its elements is a perfect square.

For a subset of the indices set {1, 2, ..., n} represented as {i1, i2, ..., ik}, we define its element-sum as: nums[i1] + nums[i2] + ... + nums[ik].

Return the maximum element-sum of a complete subset of the indices set {1, 2, ..., n}.

A perfect square is a number that can be expressed as the product of an integer by itself.

 

Example 1:

Input: nums = [8,7,3,5,7,2,4,9]
Output: 16
Explanation: Apart from the subsets consisting of a single index, there are two other complete subsets of indices: {1,4} and {2,8}.
The sum of the elements corresponding to indices 1 and 4 is equal to nums[1] + nums[4] = 8 + 5 = 13.
The sum of the elements corresponding to indices 2 and 8 is equal to nums[2] + nums[8] = 7 + 9 = 16.
Hence, the maximum element-sum of a complete subset of indices is 16.
Example 2:

Input: nums = [5,10,3,10,1,13,7,9,4]
Output: 19
Explanation: Apart from the subsets consisting of a single index, there are four other complete subsets of indices: {1,4}, {1,9}, {2,8}, {4,9}, and {1,4,9}.
The sum of the elements conrresponding to indices 1 and 4 is equal to nums[1] + nums[4] = 5 + 10 = 15.
The sum of the elements conrresponding to indices 1 and 9 is equal to nums[1] + nums[9] = 5 + 4 = 9.
The sum of the elements conrresponding to indices 2 and 8 is equal to nums[2] + nums[8] = 10 + 9 = 19.
The sum of the elements conrresponding to indices 4 and 9 is equal to nums[4] + nums[9] = 10 + 4 = 14.
The sum of the elements conrresponding to indices 1, 4, and 9 is equal to nums[1] + nums[4] + nums[9] = 5 + 10 + 4 = 19.
Hence, the maximum element-sum of a complete subset of indices is 19.
 

Constraints:

1 <= n == nums.length <= 104
1 <= nums[i] <= 109

'''


from typing import List
from collections import defaultdict, Counter
from math import sqrt, ceil
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # wrong
        n = len(nums)
        ans = 0
        i = 1
        while i*i < n+1: 
            ans += nums[i*i-1]
            i += 1
        # print(ans)
        # m = defaultdict(int)
        for i in range(1, n+1):
            for j in range(ceil(sqrt(i)), i):
                if (j*j) % i == 0:
                    ans = max(ans, nums[i-1]+nums[(j*j) // i-1])
        return max(ans, max(nums))      
    
    def maximumSum2(self, nums: List[int]) -> int:
        # key of a number represents how much is it short of becoming a perfect square.

        # For example,

        # key(6) = shortage of 6 = 6
        # key(24) = shortage of 24 = 6, as (24 = 4 * 6). It already has 4(a perfect square) but requires 6 more to become perfect square.
        # key(8) = shortage of 8 = 2, as (8 = 4 * 2). It requires multiplication by 2 to become perfect square.
        # ...and so on
        A = nums
        count = Counter()
        for i in range(len(A)):
            x, v = i + 1, 2
            while x >= v * v:
                while x % (v * v) == 0:
                    x //= v * v
                v += 1
            count[x] += A[i]
        return max(count.values())
    

            
        


if __name__ == "__main__":
    # print(Solution().maximumSum(nums = [8,7,3,5,7,2,4,9]))
    # print(Solution().maximumSum(nums = [5,10,3,10,1,13,7,9,4]))
    print(Solution().maximumSum(nums = [1,100,100,1]))
    nums = [33969,24796,64674,1378,12216,70450,58226,71401,64921,95169,5383,47175,24892,4130,74768,54172,31625,781067253,25106074,57175513,1,240671921,95079775,520810854,1,344117679,575539902,678498979,443032835,685824944,152895587,1,784748873,667662128,109570671,654252351,763152321,716977360,750506142,574160523,629177330,386270189,317284125,668042248,620709633,325542831,407572002,610115189,320351721,412659468,1,1,527228178,359984365,1,149339083,1,136493305,100938728,754000216,5751596,582609624,275055892,114306242,21277447,91154507,745223795,663228215,1,474272254,39451110]
    print(Solution().maximumSum(nums = nums))