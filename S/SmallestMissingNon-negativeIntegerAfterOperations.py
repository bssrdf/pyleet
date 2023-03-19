'''
-Medium-

*Binary Search*
*Hash Table*

You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 105
-109 <= nums[i] <= 109


'''

from typing import List
from collections import Counter
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        st = Counter()
        for x in nums:
            st[x % value] += 1
        l, r = 0, len(nums) + 1
        def possible(m):
            s = Counter(st)
            for i in range(m):
                j = i % value
                if j not in s:
                    return False
                else:
                    s[j] -= 1
                    if s[j] == 0:
                        s.pop(j)
            return True
        while l < r:
            mid = l + (r-l)//2
            if possible(mid):
                l = mid + 1
            else:
                r = mid
        return l-1
    
    def findSmallestInteger2(self, nums: List[int], value: int) -> int:
        #为了方便寻找和维护同余的数字，可以一个哈希表 cnt 统计 (nums[i] % m + m) % m 的个数。
        cnt = Counter(x % value for x in nums)
        mex = 0
        # 枚举 mex。 
        # 有没有对 0 模 m 同余的数？如果有，把这个数通过操作变成 0；否则答案就是 0。
        # 有没有对 1 模 m 同余的数？如果有，把这个数通过操作变成 1；否则答案就是 1。
        # 有没有对 2 模 m 同余的数？如果有，把这个数通过操作变成 2；否则答案就是 2。
        while cnt[mex % value]:
            cnt[mex % value] -= 1
            mex += 1
        return mex




if __name__ == '__main__':
    print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5))
    print(Solution().findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7))
    print(Solution().findSmallestInteger(nums = [3,0,3,2,4,2,1,1,0,4], value = 5))
    print(Solution().findSmallestInteger(nums = [3,2,3,1,0,1,4,2,3,1,4,1,3], value=5))
        