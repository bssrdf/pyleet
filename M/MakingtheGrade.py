'''

-Hard-
*DP*
*POJ3666*


A straight dirt road connects two fields on FJ's farm, but it changes elevation more 
than FJ would like. His cows do not mind climbing up or down a single slope, but they 
are not fond of an alternating succession of hills and valleys. FJ would like to 
add and remove dirt from the road so that it becomes one monotonic slope (either 
sloping up or down).

You are given N integers A1, ... , AN (1 ≤ N ≤ 2,000) describing the elevation 
(0 ≤ Ai ≤ 1,000,000,000) at each of N equally-spaced positions along the road, 
starting at the first field and ending at the other. FJ would like to adjust 
these elevations to a new sequence B1, . ... , BN that is either nonincreasing 
or nondecreasing. Since it costs the same amount of money to add or remove 
dirt at any position along the road, the total cost of modifying the road is

|A1 - B1| + |A2 - B2| + ... + |AN - BN |
Please compute the minimum cost of grading his road so it becomes a continuous slope. 
FJ happily informs you that signed 32-bit integers can certainly be used 
to compute the answer.

Input

* Line 1: A single integer: N
* Lines 2..N+1: Line i+1 contains a single integer elevation: Ai

Output

* Line 1: A single integer that is the minimum cost for FJ to grade his 
dirt road so it becomes nonincreasing or nondecreasing in elevation.




'''


from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        A = nums
        B = sorted(A)
        n = len(A)
        dp = [[0]*(n+1) for _ in range(n+1)]
        # print(B)
        for i in range(1, n+1):
            minn = dp[i-1][1]
            for j in range(1, n+1):
                minn = min(minn, dp[i-1][j])
                dp[i][j] = minn + abs(B[j-1]-A[i-1])
        return min(dp[n][1:])        

if __name__ == "__main__":   
    print(Solution().minimumCost(nums = [1, 3, 2, 4, 5, 3, 9]))