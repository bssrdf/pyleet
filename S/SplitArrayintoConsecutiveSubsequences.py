'''

-Medium-

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such 
that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer 
is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original 
array by deleting some (can be none) of the elements without disturbing the 
relative positions of the remaining elements. (i.e., [1,3,5] is a 
subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.


'''

from typing import List
from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 这道题就用贪婪解法就可以了，使用两个 HashMap，第一个 HashMap 用来建立数字和
        # 其出现次数之间的映射 freq，第二个用来建立可以加在某个连续子序列后的数字与其
        # 可以出现的次数之间的映射 need。对于第二个 HashMap，举个例子来说，就是假如有个连牌，
        # 比如对于数字1，此时检测数字2和3是否存在，若存在的话，表明有连牌 [1,2,3] 存在，
        # 由于后面可以加上4，组成更长的连牌，所以不管此时牌里有没有4，都可以建立 4->1 的映射，
        # 表明此时需要一个4。
        # 这样首先遍历一遍数组，统计每个数字出现的频率，然后开始遍历数组，对于每个遍历到的数字，
        # 首先看其当前出现的次数，如果为0，则继续循环；如果 need 中存在这个数字的非0映射，
        # 那么表示当前的数字可以加到某个连的末尾，将当前数字在 need 中的映射值自减1，然后将
        # 下一个连续数字的映射值加1，因为当 [1,2,3] 连上4后变成 [1,2,3,4] 之后，就可以连上5了，
        # 说明此时还需要一个5；如果不能连到其他子序列后面，则来看其是否可以成为新的子序列的起点，
        # 可以通过看后面两个数字的映射值是否大于0，都大于0的话，说明可以组成3连儿，于是将后面
        # 两个数字的映射值都自减1，还有由于组成了3连儿，在 need 中将末尾的下一位数字的映射值自增1；
        # 如果上面情况都不满足，说明该数字是单牌，只能划单儿，直接返回 false。最后别忘了将当前数字
        # 的 freq 映射值自减1。退出 for 循环后返回 true
        freq, need = Counter(nums), Counter() 
        for num in nums:
            if freq[num] == 0: continue
            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0: 
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                need[num + 3] += 1
            else: return False
            freq[num] -= 1
        return True

    def isPossible2(self, nums: List[int]) -> bool:
        left, seq = Counter(nums), Counter() 
        for x in nums:
            if left[x] == 0: continue # x is used up, skip to next
            if seq[x-1] == 0: # if a sequence of length > 3 ending with x-1  
                # DOES NOT exists, form a new seq (starting with x and ending 
                # with x+2 if both x+1 and x+2 are available
                if left[x+1] > 0 and left[x+2] > 0:
                    seq[x+2] += 1
                    left[x+1] -= 1
                    left[x+2] -= 1
                else: # otherwise, can not split, return False
                    return False 
            else: # if a sequence of length > 3 ending with x-1 exists,
                  # greedily attach x to that sequence to form a longer one 
                seq[x] += 1
                seq[x-1] -= 1
            left[x] -= 1
        return True        
                 


if __name__ == "__main__":
    print(Solution().isPossible([1,2,3,3,4,5]))
    print(Solution().isPossible2([1,2,3,3,4,5]))