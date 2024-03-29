'''
-Hard-

*Greedy*


Given a sorted positive integer array nums and an integer n, add/patch 
elements to the array such that any number in range [1, n] inclusive 
can be formed by the sum of some elements in the array. Return the 
minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 
1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], 
[1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


'''

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        """
        我们定义一个变量miss，用来表示[0,n]之间最小的不能表示的值，那么初始化为1，
        为啥不为0呢，因为n=0没啥意义，直接返回0了。那么此时我们能表示的范围是
        [0, miss)，表示此时我们能表示0到miss-1的数，如果此时的num <= miss，
        那么我们可以把我们能表示数的范围扩大到[0, miss+num)，如果num>miss，
        那么此时我们需要添加一个数，为了能最大限度的增加表示数范围，我们加上miss
        本身，以此类推直至遍历完整个数组，我们可以得到结果。
        下面我们来举个例子说明：

        给定nums = [1, 2, 4, 11, 30], n = 50，我们需要让[0, 50]之间所有的数字
        都能被nums中的数字之和表示出来。

        首先使用1, 2, 4可能表示出0到7之间的所有数，表示范围为[0, 8)，但我们不能
        表示8，因为下一个数字11太大了，所以我们要在数组里加上一个8，此时能表示的
        范围是[0, 16)，那么我们需要插入16吗，答案是不需要，因为我们数组有1和4，
        可以组成5，而下一个数字11，加一起能组成16，所以有了数组中的11，我们此时
        能表示的范围扩大到[0, 27)，但我们没法表示27，因为30太大了，所以此时我们
        给数组中加入一个27，那么现在能表示的范围是[0, 54)，已经满足要求了，我们
        总共添加了两个数8和27，所以返回2即可。
        """
        res, miss, i = 0, 1, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]  # expand the range, but no need to add patch
                                 # we are using the numbers given
                i += 1
            else:
                print('A', i, nums[i], miss)
                miss += miss  # nums[i] > miss, so no way to represent numbers
                              # [miss, nums[i]], we need to add a patch.
                              # add a number (= miss) will allow us to represent
                              # [miss,  2*miss-1]
                res += 1
                print('B', i, nums[i], miss)
                
        return res
    
if __name__ == "__main__":
    #print(Solution().minPatches([1,3],  6))
    print(Solution().minPatches([1,5,10], 20))
    print(Solution().minPatches([1, 2, 4, 11, 30], 50))
    print(Solution().minPatches([1, 2, 4, 16, 30], 50))