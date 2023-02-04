'''
-Hard-



You are given two integer arrays nums1 and nums2 of lengths m and n respectively. nums1 and nums2 represent the digits of two numbers. You are also given an integer k.

Create the maximum number of length k <= m + n from digits of the two numbers. The relative order of the digits from the same array must be preserved.

Return an array of the k digits representing the answer.

 

Example 1:

Input: nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
Output: [9,8,6,5,3]
Example 2:

Input: nums1 = [6,7], nums2 = [6,0,4], k = 5
Output: [6,7,6,0,4]
Example 3:

Input: nums1 = [3,9], nums2 = [8,9], k = 3
Output: [9,8,9]
 

Constraints:

m == nums1.length
n == nums2.length
1 <= m, n <= 500
0 <= nums1[i], nums2[i] <= 9
1 <= k <= m + n

'''

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def extract(nums, l):
            m = len(nums) - l  
            st = []
            for i in nums:
                while st and m and st[-1] < i:
                    st.pop()
                    m -= 1
                st.append(i)
            if m: # not fully spent
                st = st[0:-m]
            return st
        mi, ans = '0', []
        for i in range(min(len(nums1)+1,k+1)):
            s1 = extract(nums1, i)  
            if k-i > len(nums2): continue          
            s2 = extract(nums2, k-i)
            j1, j2 = 0, 0
            s, tmp = '', []
            while j1 < len(s1) and j2 < len(s2):
                if s1[j1] < s2[j2]:
                    s += str(s2[j2])  
                    tmp.append(s2[j2])
                    j2 += 1                    
                elif s1[j1] > s2[j2]:
                    s += str(s1[j1])  
                    tmp.append(s1[j1])
                    j1 += 1
                else:
                    t1, t2 = j1, j2
                    while t1 < len(s1) and t2 < len(s2) and s1[t1] == s2[t2]:
                        t1 += 1
                        t2 += 1

                    if t2 == len(s2):
                        s += str(s1[j1])  
                        tmp.append(s1[j1])
                        j1 += 1
                    elif t1 < len(s1) and s1[t1] > s2[t2]: 
                        s += str(s1[j1])  
                        tmp.append(s1[j1])
                        j1 += 1
                    else:
                        s += str(s2[j2])  
                        tmp.append(s2[j2])
                        j2 += 1   
                # print(s1, s2, j1, j2)                 

            # print(mi, s, j1, j2, s1, s2)
            while j1 < len(s1):
                s += str(s1[j1])  
                tmp.append(s1[j1])
                j1 += 1
            while j2 < len(s2):
                s += str(s2[j2])  
                tmp.append(s2[j2])
                j2 += 1
            # print(mi, len(s), j1, j2, len(s1), len(s2))
            if s > mi:
                mi = s
                ans = tmp[:]
        return ans    






if __name__ == "__main__":
    print(Solution().maxNumber(nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5))
    print(Solution().maxNumber(nums1 = [6,7], nums2 = [6,0,4], k = 5))
    print(Solution().maxNumber(nums1 = [3,9], nums2 = [8,9], k = 3))
    print(Solution().maxNumber(nums1 = [2,5,6,4,4,0], nums2 = [7,3,8,0,6,5,7,6,2], k = 15))

    print(Solution().maxNumber(nums1 = [5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3], 
                               nums2=[7,6,7,1,0,1,0,5,6,0,5,0], k=31))


    n1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    n2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    sol = Solution().maxNumber(n1, n2, 100)
    ans = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    print(len(sol), len(ans))