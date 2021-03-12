"""
-Medium-

*Two Pointers*

Given an array S of n integers, are there elements a, b, c in S such that 
a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""
__author__ = 'Danyang'

from collections import defaultdict

class Solution:
    #def threeSum_duplicate(self, num):
    def threeSum(self, num):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        d1 = defaultdict(list)      
        for i, n in enumerate(num):
            d1[n].append(i)        
        res = []
        for i, n in enumerate(num):
            target = -1*n
            for j, m in enumerate(num):
                if (target - m) in d1:
                    #if len(d1[target-m]) == 1:
                    if d1[target-m][0] != j and j != i and d1[target-m][0] != i:
                        c=[n, m, target-m]
                        #print target, c
                        c.sort()
                        if c not in res:
                            res.append(c)
                    
        return res

    def threeSumTwoPointersSlow(self, nums):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        nums.sort()
        print(nums)
        res = set()
        for k in range(1, len(nums)-1):
            left, right = 0, len(nums)-1
            while left < k and right >= k+1:
                num = nums[left] + nums[k] + nums[right]
                if num == 0: 
                   res.add((nums[left], nums[k], nums[right]))
                   left += 1
                   right -= 1
                elif num < 0: left += 1
                else: right -= 1 
        return [list(x) for x in res]

    def threeSumTwoPointersFast(self, nums):
        """
        Hash
        O(n^2)
        :param num: array
        :return: a list of lists of length 3, [[val1,val2,val3]]
        """
        nums.sort()
        if not nums or nums[0] > 0 or nums[-1] < 0: return []
        res = []
        for k in range(len(nums)-2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k-1]: continue
            target, i, j = -1*nums[k], k+1, len(nums)-1
            while i < j:                
                if nums[i]+nums[j] == target: 
                   res.append([nums[k], nums[i], nums[j]])
                   while i < j and nums[i] == nums[i+1]: i += 1
                   while i < j and nums[j] == nums[j-1]: j -= 1
                   i += 1
                   j -= 1
                elif nums[i]+nums[j] < target: i += 1
                else: j -= 1 
        return res
        


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSumTwoPointersFast([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSumTwoPointersFast([]))
    print(Solution().threeSumTwoPointersFast([0]))
    print(Solution().threeSumTwoPointersSlow([3,0,-2,-1,1,2]))
    print(Solution().threeSumTwoPointersFast([3,0,-2,-1,1,2]))

