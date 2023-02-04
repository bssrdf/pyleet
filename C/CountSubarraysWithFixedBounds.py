'''


'''
from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        pminK, pmaxK = [-1]*n, [-1]*n
        outB = [-1]*n
        if nums[0] == minK:
            pminK[0] = 0
        if nums[0] == maxK:
            pmaxK[0] = 0
        if nums[0] < minK or nums[0] > maxK:
            outB[0] = 0    
        for i in range(1, n):
            if nums[i] == minK:
                pminK[i] = i
            elif minK <= nums[i] <= maxK:
                pminK[i] = pminK[i-1]               

            if nums[i] == maxK:
                pmaxK[i] = i
            elif minK <= nums[i] <= maxK:
                pmaxK[i] = pmaxK[i-1]
            if  nums[i] < minK or nums[i] > maxK:
                outB[i] = i 
            else:
                outB[i] = outB[i-1]

        ans = 0
        for i in range(n):
            if pminK[i] != -1 and pmaxK[i] != -1:
                ans += min(pminK[i], pmaxK[i]) - outB[i] 
        return ans
    
    def countSubarrays2(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        pminK, pmaxK = [-1]*n, [-1]*n
        outB = [-1]*n
        if nums[0] == minK:
            pminK[0] = 0
        if nums[0] == maxK:
            pmaxK[0] = 0
        if nums[0] < minK or nums[0] > maxK:
            outB[0] = 0    
        for i in range(1, n):
            if nums[i] == minK:
                pminK[i] = i
            else:
                pminK[i] = pminK[i-1]               
            if nums[i] == maxK:
                pmaxK[i] = i
            else:
                pmaxK[i] = pmaxK[i-1]
            if  nums[i] < minK or nums[i] > maxK:
                outB[i] = i 
            else:
                outB[i] = outB[i-1]
        ans = 0
        for i in range(n):
            if pminK[i] != -1 and pmaxK[i] != -1:
                j = min(pminK[i], pmaxK[i])
                ans += j - outB[i] if j - outB[i] > 0 else 0 
        return ans

    def countSubarrays3(self, nums: List[int], minK: int, maxK: int) -> int:
        # O(1) space
        pminK, pmaxK, outB = -1, -1, -1
        ans = 0
        for i,a in enumerate(nums):
            if a == minK:
                pminK = i
            if a == maxK:
                pmaxK = i
            if  a < minK or a > maxK:
                outB = i 
            if pminK != -1 and pmaxK != -1:
                j = min(pminK, pmaxK)
                ans += j - outB if j - outB > 0 else 0 
        return ans
        

if __name__ == "__main__":
    print(Solution().countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(Solution().countSubarrays2(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(Solution().countSubarrays3(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
    print(Solution().countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))
    print(Solution().countSubarrays2(nums = [1,1,1,1], minK = 1, maxK = 1))
    print(Solution().countSubarrays3(nums = [1,1,1,1], minK = 1, maxK = 1))
    nums = [934372,927845,479424,49441,17167,17167,65553,927845,17167,927845,17167,425106,17167,927845,17167,927845,251338,17167]
    print(Solution().countSubarrays(nums = nums, minK = 17167, maxK = 927845))
    print(Solution().countSubarrays2(nums = nums, minK = 17167, maxK = 927845))
    print(Solution().countSubarrays3(nums = nums, minK = 17167, maxK = 927845))
        