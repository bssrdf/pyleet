'''

-Medium-


Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.

 

Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6


'''

from typing import List

class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        A = []
        for i in range(n):
            A.append([arr1[i], arr2[i], i])
        ans = 0
        for s in range(1<<3):
            mi, mx = float('inf'), -float('inf')
            for i in range(n):
                t = 0
                for j in range(3):
                    if (1<<j) & s:
                        t += A[i][j]
                    else:
                        t -= A[i][j]
                mi = min(mi, t)
                mx = max(mx, t)        
            ans = max(ans, mx - mi)
        return ans
    
    def maxAbsValExpr2(self, arr1: list, arr2: list) -> int:
        a = [arr1[i] + arr2[i] + i for i in range(len(arr1))]
        b = [arr1[i] + arr2[i] - i for i in range(len(arr1))]
        c = [arr1[i] - arr2[i] + i for i in range(len(arr1))]
        d = [arr1[i] - arr2[i] - i for i in range(len(arr1))]
        return max(map(lambda x: max(x) - min(x), (a, b, c, d)))



if __name__ == "__main__":
    print(Solution().maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))
