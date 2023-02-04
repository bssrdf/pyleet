'''
-Medium-

You are given an integer array nums of even length n and an integer limit. 
In one move, you can replace any integer from nums with another integer 
between 1 and limit, inclusive.

The array nums is complementary if for all indices i (0-indexed), 
nums[i] + nums[n - 1 - i] equals the same number. For example, the array
[1,2,3,4] is complementary because for all indices i, nums[i] + 
nums[n - 1 - i] = 5.

Return the minimum number of moves required to make nums complementary.

 

Example 1:

Input: nums = [1,2,4,3], limit = 4
Output: 1
Explanation: In 1 move, you can change nums to [1,2,2,3] (underlined 
elements are changed).
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
Therefore, nums[i] + nums[n-1-i] = 4 for every i, so nums is complementary.
Example 2:

Input: nums = [1,2,2,1], limit = 2
Output: 2
Explanation: In 2 moves, you can change nums to [2,2,2,2]. You cannot 
change any number to 3 since 3 > limit.
Example 3:

Input: nums = [1,2,1,2], limit = 2
Output: 0
Explanation: nums is already complementary.
 

Constraints:

n == nums.length
2 <= n <= 10^5
1 <= nums[i] <= limit <= 10^5
n is even.

'''

import sys

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int

        此题非常关键的条件在于1 <= nums[i] <= limit <= 1e5 否则差分无法应用，
        会报错后文会说明。
        以下部分题解参考大佬周赛题解

        此题的正常思路为：
        设目标值为 target，根据题目要求，target应该属于 ∈ [2, 2limit]。（）
        对于一对数字 (a,b)，假设 a <= b。则对移动次数的贡献如下：
        target ∈ [2, a+1)，需要操作两次。
        target ∈ [a+1, a+b)，需要操作一次。
        target ∈ [a+b, a+b]，不需要操作。
        target ∈ (a+b, b + limit]，需要操作一次。
        target ∈ (b+limit, 2limit]，需要操作两次。(由此，b必须<= limit,否则该
        区间不成立)
        由此可以将操作次数表示为一个以a,b为变量的分段函数 f(a,b)

        这样就有了一个思路，设数组 res，用来记录移动次数。res[i] 为目标值为 i 时的
        移动次数。
        1.遍历数组(0-nums.size()/2),分别得到一组a,b;
        2.对每组a,b,利用分段函数f(a,b) 更新每一个res[i]; res[i]=res[i]+f(a,b)
        3.找出res[i]中的最小值，即为答案。
        复杂度为O(N*limit),即O(n^2);

        那么为什么上述方法可以用差分数组呢？关于差分数组可以看讲解差分

        差分数组的作用是什么呢，差分的作用主要有2个
        a.对于长区间内每个数同时+某值更新时，例如区间长度为1e5时，挨个去加是非常麻烦的
        b.对于某个区间多次更新其值时.

        在上述方法中，从 [2, 2limit]更新res[i]的过程，其实是分别对区间 [2, a+1) ，
        [a+1, a+b)，(a+b, b + limit]，(b+limit, 2limit]， 进行更新的过程，即对区间
        进行值更新的过程，可以利用差分数组 将从[2, 2*limit]更新res[i]的过程的复杂度
        由O(n)降至O(1)。

        那么，如何差分呢，方法很简单，和众多大佬说的一样，要对区间 [l,r] 中每个元素都
        增加 x，那么 dis 与之对应的变化为 ，dis[l] += x, dis[r+1] -= x。
        这里，需要注意的一点是，差分的更新的区间为[l,r],则需要改变的值为dis[l],dis[r+1]。
        """

        dis = [0]*(2*limit+2)
        n = len(nums)
        for i in range(n//2):
            a = min(nums[i],nums[n-i-1])   #a为一对数中的较小数
            b = max(nums[i],nums[n-i-1]) #b为一对数中的较大数

            point0=2
            point1=a+1          # target ∈ [2, a+1)，需要操作两次
            point2=a+b          # target ∈ [a+1, a+b)，需要操作一次
                                # target ∈ [a+b, a+b]，不需要操作
            point3 = b+limit    # target ∈ (a+b, b + limit]，需要操作一次 
            point4 = 2*limit    # target ∈ (b+limit, 2*limit]，需要操作两次

            #更新差分数组

            dis[point0]+=2
            dis[point1]-=2  # target ∈ [2, a+1)，需要操作两次

            dis[point1]+=1
            dis[point2]-=1  # target ∈ [a+1, a+b)，需要操作一次

            dis[point2+1]+=1
            dis[point3+1]-=1 # target ∈ (a+b, b + limit]，需要操作一次 

            dis[point3+1]+=2
            dis[point4+1]-=2 # target ∈ (b+limit, 2*limit]，需要操作两次
        

        # 还原原数组，并找出最小值
        sm = 0
        res = sys.maxsize
        for i in range(2, 2*limit+1):
            sm += dis[i]
            print(i, dis[i], sm)
            res = min(res, sm)
            
        return res


if __name__ == "__main__":
    print(Solution().minMoves([1,2,4,3], 4))
    print(Solution().minMoves([1,2,1,2], 2))
    print(Solution().minMoves([1,2,2,1], 2))