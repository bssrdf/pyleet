'''

-Hard-

Alice is a caretaker of n gardens and she wants to plant flowers to maximize the 
total beauty of all her gardens.

You are given a 0-indexed integer array flowers of size n, where flowers[i] is the 
number of flowers already planted in the ith garden. Flowers that are already 
planted cannot be removed. You are then given another integer newFlowers, which is 
the maximum number of flowers that Alice can additionally plant. You are also given 
the integers target, full, and partial.

A garden is considered complete if it has at least target flowers. The total beauty 
of the gardens is then determined as the sum of the following:

The number of complete gardens multiplied by full.
The minimum number of flowers in any of the incomplete gardens multiplied by partial. 
If there are no incomplete gardens, then this value will be 0.
Return the maximum total beauty that Alice can obtain after planting at most newFlowers 
flowers.

 

Example 1:

Input: flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
Output: 14
Explanation: Alice can plant
- 2 flowers in the 0th garden
- 3 flowers in the 1st garden
- 1 flower in the 2nd garden
- 1 flower in the 3rd garden
The gardens will then be [3,6,2,2]. She planted a total of 2 + 3 + 1 + 1 = 7 flowers.
There is 1 garden that is complete.
The minimum number of flowers in the incomplete gardens is 2.
Thus, the total beauty is 1 * 12 + 2 * 1 = 12 + 2 = 14.
No other way of planting flowers can obtain a total beauty higher than 14.
Example 2:

Input: flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
Output: 30
Explanation: Alice can plant
- 3 flowers in the 0th garden
- 0 flowers in the 1st garden
- 0 flowers in the 2nd garden
- 2 flowers in the 3rd garden
The gardens will then be [5,4,5,5]. She planted a total of 3 + 0 + 0 + 2 = 5 flowers.
There are 3 gardens that are complete.
The minimum number of flowers in the incomplete gardens is 4.
Thus, the total beauty is 3 * 2 + 4 * 6 = 6 + 24 = 30.
No other way of planting flowers can obtain a total beauty higher than 30.
Note that Alice could make all the gardens complete but in this case, she would obtain a lower total beauty.
 

Constraints:

1 <= flowers.length <= 105
1 <= flowers[i], target <= 105
1 <= newFlowers <= 1010
1 <= full, partial <= 105

'''

from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort(reverse=True)
        F = flowers
        # print(flowers)
        
        n = len(flowers)
        if F[-1] >= target:
            return n*full
        preSum = [0]*(n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + F[i]
        l, r = 1, n+1
        def minRemain(k, avail):            
            l, r = F[-1], target 
            while l < r:
                mid = l + (r-l)//2
                left, right = k, n
                while left < right:
                    m = left + (right-left)//2
                    if F[m] > mid:
                        left = m + 1
                    else:
                        right = m
                # print('left =', left, mid, l, r)
                # print( mid*(n-left), preSum[n]-preSum[left], preSum[n], preSum[left])
                if mid*(n-left) - (preSum[n]-preSum[left]) <= avail:
                    l = mid + 1
                else:
                    r = mid               
            return l - 1
        ans = 0
        
        avail = newFlowers
        ans = max(ans, partial*minRemain(0, avail))
        for i in range(1,n):
            if flowers[i] < target:
                if avail >= target - flowers[i-1]:
                    avail -= target - flowers[i-1]                
                else:
                    break
            mr = minRemain(i, avail) 
            beat = i*full + partial * mr
            print(i, ans, beat, avail, i*full, mr)
            ans = max(ans,  beat)
        
        return ans


    def maximumBeauty2(self, A: List[int], new: int, t: int, full: int, part: int) -> int:
        A = [min(t, a) for a in A]
        A.sort()
		
		# Two edge cases
        if min(A) == t: return full * len(A)
        if new >= t * len(A) - sum(A):
            return max(full*len(A), full*(len(A)-1) + part*(t-1))
        
		# Build the array `cost`.
        cost = [0]
        for i in range(1, len(A)):
            pre = cost[-1]
            cost.append(pre + i * (A[i] - A[i - 1]))

		# Since there might be some gardens having `target` flowers already, we will skip them.
        j = len(A) - 1
        while A[j] == t:
            j -= 1
        
		# Start the iteration
        ans = 0
        while new >= 0:
		
			# idx stands for the first `j` gardens, notice a edge case might happen.
            idx = min(j, bisect_right(cost, new) - 1)
			
			# bar is the current minimum flower in the incomplete garden
            bar = A[idx] + (new - cost[idx]) // (idx + 1)
			
            ans = max(ans, bar * part + full *(len(A) - j - 1))
            
			# Now we would like to complete garden j, thus deduct the cost for garden j 
			# from new and move on to the previous(next) incomplete garden!
            new -= (t - A[j])
            j -= 1
            
        return ans    





if __name__ == "__main__":
    # print(Solution().maximumBeauty(flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1))
    # print(Solution().maximumBeauty(flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6))
    # print(Solution().maximumBeauty([18,16,10,10,5], 10, 3, 15, 4))
    # print(Solution().maximumBeauty([13], 18, 15, 9, 2))
 
    print(Solution().maximumBeauty([10,9,16,14,6,5,11,12,17,2,11,15,1], 80, 14, 15, 1))
