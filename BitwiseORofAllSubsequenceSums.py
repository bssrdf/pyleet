'''
-Medium-
$$$


Given an integer array nums, return the value of the bitwise OR of the sum of all possible subsequences in the array.

A subsequence is a sequence that can be derived from another sequence by removing zero or more elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [2,1,0,3]
Output: 7
Explanation: All possible subsequence sums that we can have are: 0, 1, 2, 3, 4, 5, 6.
And we have 0 OR 1 OR 2 OR 3 OR 4 OR 5 OR 6 = 7, so we return 7.
Example 2:

Input: nums = [0,0,0]
Output: 0
Explanation: 0 is the only possible subsequence sum we can have, so we return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109

'''


from typing import List

class Solution:
    def subsequenceSumOr(self, nums: List[int]) -> int:
        #wrong
        bits = [0]*64
        for a in nums:
            for i in range(31):
                if (1 << i) & a > 0:
                    if bits[i] == 1:
                        bits[i+1] = 1  
                    else:
                        bits[i] = 1
        return int(''.join([str(i) for i in bits[::-1]]), base=2)  
    

    def subsequenceSumOr2(self, nums: List[int]) -> int:
        '''
        我们先用数组cnt统计每一位上1的个数, 然后从低位到高位,如果该位上1的个数大于0,
        则将该位所表示的数加入到答案中。然后判断是否可以进位，是则累加到下一位。

        时间复杂度O(nlogM),其中n和M分别为数组长度和数组中元素的最大值。
        '''
        cnt = [0] * 64
        ans = 0
        for v in nums:
            for i in range(31):
                if (v >> i) & 1:
                    cnt[i] += 1
        for i in range(63):
            if cnt[i]:
                ans |= 1 << i
            cnt[i + 1] += cnt[i] // 2
        return ans





if __name__ == "__main__":
    print(Solution().subsequenceSumOr(nums = [2,1,0,3]))
    print(Solution().subsequenceSumOr(nums = [0,0,0]))

    print(Solution().subsequenceSumOr(nums = [2,1,0,256]))
    print(Solution().subsequenceSumOr2(nums = [2,1,0,256]))