"""
-Medium-

*Two Pointers*

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


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

