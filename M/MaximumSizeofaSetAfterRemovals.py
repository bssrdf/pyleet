'''
-Medium-


You are given two 0-indexed integer arrays nums1 and nums2 of even length n.

You must remove n / 2 elements from nums1 and n / 2 elements from nums2. After the removals, you insert the remaining elements of nums1 and nums2 into a set s.

Return the maximum possible size of the set s.

 

Example 1:

Input: nums1 = [1,2,1,2], nums2 = [1,1,1,1]
Output: 2
Explanation: We remove two occurences of 1 from nums1 and nums2. After the removals, the arrays become equal to nums1 = [2,2] and nums2 = [1,1]. Therefore, s = {1,2}.
It can be shown that 2 is the maximum possible size of the set s after the removals.
Example 2:

Input: nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]
Output: 5
Explanation: We remove 2, 3, and 6 from nums1, as well as 2 and two occurrences of 3 from nums2. After the removals, the arrays become equal to nums1 = [1,4,5] and nums2 = [2,3,2]. Therefore, s = {1,2,3,4,5}.
It can be shown that 5 is the maximum possible size of the set s after the removals.
Example 3:

Input: nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]
Output: 6
Explanation: We remove 1, 2, and 3 from nums1, as well as 4, 5, and 6 from nums2. After the removals, the arrays become equal to nums1 = [1,2,3] and nums2 = [4,5,6]. Therefore, s = {1,2,3,4,5,6}.
It can be shown that 6 is the maximum possible size of the set s after the removals.
 

Constraints:

n == nums1.length == nums2.length
1 <= n <= 2 * 104
n is even.
1 <= nums1[i], nums2[i] <= 109

'''

from typing import List
from collections import Counter
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        m = len(nums1)//2
        t1 = 0
        # while t1 < m:
        cnt1c = dict(cnt1)
        for c in cnt1:
            if cnt1[c] > 1:
                k = cnt1[c] - 1
                d = min(k, m-t1)
                t1 += d
                cnt1c[c] = cnt1[c] - d
            if t1 == m:
                break
        cnt1 = cnt1c    
        t2 = 0
        # while t2 < m:
        cnt2c = dict(cnt2)
        for c in cnt2:
            if cnt2[c] > 1:
                k = cnt2[c] - 1
                d = min(k, m-t2)
                t2 += d
                cnt2c[c] = cnt2[c] - d
            if t2 == m:
                break
        cnt2 = cnt2c    
        print(cnt1)
        print(cnt2)
        if t1 == m and t2 == m:
            return len(cnt1 | cnt2)
        elif t1 == m:
            cnt2c = dict(cnt2)
            for c in cnt2:
                if c in cnt1:                    
                    t2 += cnt2[c]
                    cnt2c.pop(c)                
                if t2 == m:
                    break
            cnt2 = cnt2c    
            if t2 == m:
                return len(cnt1 | cnt2)
            cnt2c = dict(cnt2)
            for c in cnt2:
                t2 += cnt2[c]
                cnt2c.pop(c)
                if t2 == m:
                    break
            cnt2 = cnt2c    
            return len(cnt1 | cnt2) 
        elif t2 == m:
            cnt1c = dict(cnt1)
            for c in cnt1:
                if c in cnt2:                    
                    t1 += cnt1[c]
                    cnt1c.pop(c)
                if t1 == m:
                    break
            cnt1 = cnt1c    
            if t1 == m:
                return len(cnt1 | cnt2)
            cnt1c= dict(cnt1)
            for c in cnt1:
                t1 += cnt1[c]
                cnt1c.pop(c)
                if t1 == m:
                    break
            cnt1 = cnt1c    
            return len(cnt1 | cnt2) 
        else:
            cnt1c, cnt2c = dict(cnt1), dict(cnt2)
            exc = set()
            for c in cnt1:                
                if c in cnt2 :
                   exc.add(c) 
                   cnt1c.pop(c)
                   cnt2c.pop(c)   
            a = len(cnt1c)                  
            b = len(cnt2c)  
            c = len(exc)
            print(a,b,c, cnt1c, cnt2c)
            # if c == 0:
            if a == 0 and b == 0:
                return c
            print(a,b,c)
            if a < m and b < m: 
                for z3 in range(c):
                    if (c - z3 + b - a) % 2 == 0:
                        z1 = (c - z3 + b - a)//2
                        z2 = c - z3 - z1
                        return a+z1+b+z2 
            elif a == m: 
                if b >= m:
                    return 2*m
                return 2*min(m, b+c)
            elif b == m: 
                if a >= m:
                    return 2*m
                return 2*min(m, a+c)
            else:
                return 2*m

    def maximumSetSize2(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = set(nums1)
        s2 = set(nums2)
        n = len(nums1)
        inter = s1.intersection(s2)
        ex1 = min(len(s1) - len(inter) , n//2)
        ex2 = min(len(s2) - len(inter) , n//2)
        return (min(ex1 + ex2 + len(inter) , n))
            


if __name__ == "__main__":
    # print(Solution().maximumSetSize(nums1 = [1,2,1,2], nums2 = [1,1,1,1]))
    # print(Solution().maximumSetSize(nums1 = [1,2,3,4,5,6], nums2 = [2,3,2,3,2,3]))
    # print(Solution().maximumSetSize(nums1 = [1,1,2,2,3,3], nums2 = [4,4,5,5,6,6]))
        
    # print(Solution().maximumSetSize(nums1 = [1,2,1,1], nums2 = [1,2,3,4]))
    # print(Solution().maximumSetSize(nums1 = [8,9], nums2 = [3,4]))
    # # print(Solution().maximumSetSize(nums1 = [10,8,7,9], nums2 = [7,9,9,5]))
    # # print(Solution().maximumSetSize(nums1 = [2,4,1,4], nums2 = [10,2,4,10]))
    # # print(Solution().maximumSetSize(nums1 = [7,2,5,1,3,1,4,5], nums2 = [1,5,5,9,1,6,4,1]))
    # print(Solution().maximumSetSize(nums1 = [5,1,9,5,6,4,9,6,7,6], nums2 = [7,6,9,2,10,8,3,10,8,2]))
    # print(Solution().maximumSetSize(nums1 = [1,10,6,5], nums2 = [3,7,10,10]))
    # print(Solution().maximumSetSize(nums1 = [5,2,8,6], nums2 = [7,4,1,1] ))
    print(Solution().maximumSetSize(nums1 = [1,3,3,2] , nums2 = [2,2,1,3] ))