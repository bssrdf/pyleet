'''


'''
from math import gcd
from typing import List
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):            
            if k % nums[i] != 0:
                continue
            g = nums[i]
            m = nums[i]            
            m1 = m             
            if m == k:
                ans += 1
            for j in range(i+1, n):
                if k % nums[j] == 0:
                    g = gcd(g, nums[j])
                    m = m1 * nums[j]
                    if m//g == k:
                        ans += 1  
                else:
                    break              
                g = nums[j]
                m1 = nums[j]
        return ans

    def subarrayLCM2(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        def lcm(a, b):
            return a * b // gcd(a,b)
        for i in range(n):            
            l = nums[i]
            for j in range(i, n):
                l = lcm(l, nums[j])
                if l == k: ans += 1  
                elif l > k:
                    break              
        return ans
                    
print(Solution().subarrayLCM([2,1,1,5], 5))      
print(Solution().subarrayLCM([3,6,2,7,1], 6))
print(Solution().subarrayLCM2([2,1,1,5], 5))      
print(Solution().subarrayLCM2([3,6,2,7,1], 6))