'''

-Medium-
$$$

=== 题意 ===

给定一个只包含 0 和 1 的数组，求所有满足 1 的个数大于 0 的个数的子数组个数。

You are given a binary array nums containing only the integers 0 and 1. Return 
the number of subarrays in nums that have more 1's than 0's. Since the answer 
may be very large, return it modulo 10**9 + 7.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [0,1,1,0,1]
Output: 9
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]
Example 2:

Input: nums = [0]
Output: 0
Explanation:
No subarrays have more ones than zeros.
Example 3:

Input: nums = [1]
Output: 1
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 1

=== 思路 ===

看到这种 0、1 比较单调的数组加上个数的大小比较，可以快速的想到将 0 看作 -1，进行前缀和，
当前缀和区间大于 0 时，表示这个区间内 1 比 0 多。

通过简单的推算，可得用例一的前缀和数组为 [-1, 0, 1, 0, 1]，根据前缀和区间做差后的特性，

此时 x 对所有子数组的贡献取决于其后面有多少个数字大于 x：4 + 2 + 0 + 1 + 0 = 7。

而 7 < 9 很明显是漏答案了，因为没有将空数组这个边界考虑进去。我们需要加上边界对应的哨兵位 0，
此时得到 [0, -1, 0, 1, 0, 1]，计算出 2 + 4 + 2 + 0 + 1 + 0 = 9。

总之，在得到前缀和数组后，对每个数字求出后面比它大的数字个数，接着将这些个数求和即为答案。

这里可以使用树状数组进行计算，或者无脑一点，使用有序列表，比如 SortedList，通过查找插入位置

与列表长度的差值即可得到每个数字对答案的贡献。

'''
import collections

class Solution(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        A = nums
        n = len(nums)
        ans, preSum, MOD = 0, 0, 10**9+7       

        BIT = [0]*(2*n+1)
        def update(x, delta):
            x += n+1
            while x < len(BIT):
                BIT[x] += delta
                x += x & (-x)
        def get(x):
            x += n+1
            sm = 0
            while x > 0:
                sm += BIT[x]
                x -= x & (-x)
            return sm
        update(0, 1)
        for i in range(n):
            preSum += 1 if A[i] == 1 else -1
            #print(preSum, get(preSum-1), BIT)
            ans = (ans + get(preSum-1)) % MOD
            #print('ans:',ans)
            update(preSum, 1)
        return ans

    def subarraysWithMoreZerosThanOnes2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        lookup = collections.defaultdict(int)
        lookup[0] = 1
        result = total = same = more = 0
        for x in nums:
            total += 1 if x == 1 else -1
            new_same = lookup[total]
            new_more = (same+more+1)%MOD if x == 1 else (more-new_same)%MOD
            lookup[total] += 1
            result = (result+new_more)%MOD
            same, more = new_same, new_more
        return result
    
    def subarraysWithMoreZerosThanOnes3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        lookup = {0:-1}
        dp = [0]*len(nums)
        result = total = 0
        for i, x in enumerate(nums):
            total += 1 if x == 1 else -1
            if total not in lookup:
                if total > 0:
                    #print('case A',i, x, total)
                    dp[i] = i+1
                    #print('case A', dp[i])
            else:
                j = lookup[total]
                if j != -1: # 
                    #print('case B', i, x, j, total)
                    dp[i] = dp[j]
                    #print('case B', dp[i])
                if x > 0:
                   # print('case C', i, x, j, total)
                    dp[i] += (i-1)-j
                   # print('case C', dp[i])
                #print('case B/C', dp[i])    
            lookup[total] = i
            result = (result+dp[i])%MOD
        return result

    def subarraysWithMoreZerosThanOnes4(self, nums):
        # 这里sum表示截止当前位置的前缀和(0转化为-1）,以当前位置为末尾，
        # 且满足的子数组的设为B，而该数组前面的子数组设为A，
        # 有sum(B) > 0, sum(B) = sum(A+B) - sum(A) > 0,因此sum(A+B) > sum(A),
        # 因此只需要计算前面有多少前缀和小于当前的前缀和，而这里的cnt 记录的就是
        # 小于等于sum - 1 的前缀和数目，如果当前位为1，那么 sum 会转变为sum + 1，
        # 也就是说前缀和为sum也可以满足条件，因此有cnt += umap[sum-1]， 
        # 同理如果当前位为-1，那么sum 会转变为sum - 1, 这里前缀和sum - 1不再满足条件，
        # 而cnt又包含，因此需要cnt -= umap[sum]
        umap = collections.defaultdict(int)
        umap[0] = 1
        MOD = 10**9 + 7
        ans = cnt = sm = 0
        for i in range(len(nums)):
            sm += 1 if nums[i] else -1
            print('a:', i, nums[i], sm, cnt, umap)
            if nums[i]:
                cnt += umap[sm-1]
            else:
                cnt -= umap[sm]
            print('b:', sm, cnt)
            umap[sm] += 1
            ans += cnt
            ans %= MOD
        return ans


if __name__ == "__main__":
    #print(Solution().subarraysWithMoreZerosThanOnes([0, 1, 1, 0, 1]))
    #print(Solution().subarraysWithMoreZerosThanOnes2([0, 1, 1, 0, 1]))
    print(Solution().subarraysWithMoreZerosThanOnes3([0, 1, 1, 0, 1]))
    print(Solution().subarraysWithMoreZerosThanOnes4([0, 1, 1, 0, 1]))
    print(Solution().subarraysWithMoreZerosThanOnes3([0, 0, 1, 1, 0, 1]))
    print(Solution().subarraysWithMoreZerosThanOnes4([0, 0, 1, 1, 0, 1]))

