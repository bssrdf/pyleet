'''

'''

from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        A, n = nums, len(nums)
        dec, inc = [-1]*n, [-1]*n
        dec[0] = 0
        inc[-1] = n-1
        for i in range(1,n):
            if A[i] <= A[i-1]:
                dec[i] = dec[i-1]
            else:
                dec[i] = i
        for i in range(n-2, -1, -1):
            if A[i] <= A[i+1]:
                inc[i] = inc[i+1]
            else:
                inc[i] = i
        ans = []
        for i in range(k, n-k):
            if i-1 - dec[i-1] + 1 >= k and inc[i+1] - (i+1) + 1>= k:
                ans.append(i)
        # print(dec)
        # print(inc)
        return ans

if __name__ == "__main__":
    print(Solution().goodIndices(nums = [2,1,1,1,3,4,1], k = 2))
    print(Solution().goodIndices(nums = [2,1,1,2], k = 2))
        