'''
-Hard-

You are given an integer array nums of 2 * n integers. You need to partition 
nums into two arrays of length n to minimize the absolute difference of the sums 
of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
 

Constraints:

1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107


'''
from typing import List
from itertools import combinations
import bisect


class Solution:
    def minimumDifference1(self, nums: List[int]) -> int:
        n = len(nums)//2
        total = sum(nums)
        target = total // 2
        def dfs2(i,d,k,cur,arr,sums):
            if d == k:
                sums.append(cur)
                return 
            if i==len(arr):
                # sums.add(cur)
                return
            dfs2(i+1,d,k,cur,arr,sums)
            dfs2(i+1,d+1,k,cur+arr[i],arr,sums)

        def dfs(start, depth, k, cur, sm, arr):
            if depth == k:
                sm.append(cur)
                return
            for i in range(start, n):        
                if n-i < (k-depth): break        
                dfs(i+1, depth+1, k, cur+arr[i], sm, arr)
        
        def get_sums(arr): # generate all combinations sum of k elements
            ans = [[] for _ in range(n+1)]        
            for k in range(1, n+1): # takes k element for nums
                for comb in combinations(arr, k):
                    s = sum(comb)
                    ans[k].append(s)
            ans[0] = [0]
            return ans
        #sumAk = get_sums(nums[:n])
        #sumBk = get_sums(nums[n:])
        sumAk = [[] for _ in range(n+1)]        
        sumBk = [[] for _ in range(n+1)]        
        for k in range(1,n+1):
            # dfs(0, 0, k, 0, sumAk[k], nums[:n])
            # dfs(0, 0, k, 0, sumBk[k], nums[n:])
            dfs2(0, 0, k, 0, nums[:n], sumAk[k])
            dfs2(0, 0, k, 0, nums[n:], sumBk[k])
        sumAk[0] = [0]
        sumBk[0] = [0]  
       
        for k in range(n+1):
            sumBk[k].sort()
        ans = float('inf')
        for k in range(n+1):
            for sA in sumAk[k]:
                idx = bisect.bisect_left(sumBk[n-k], target - sA)
                if idx < len(sumBk[n-k]):
                    x = sA+sumBk[n-k][idx]
                    ans = min(ans, abs(x - (total-x)))
                if idx > 0:
                    x = sA+sumBk[n-k][idx-1]
                    ans = min(ans, abs(x - (total-x)))
        return ans            

    def minimumDifference(self, nums: List[int]) -> int:
        # still TLE
        n = len(nums)//2
        A, B = nums[:n], nums[n:]
        total = sum(nums)
        target = total // 2
        def popcount(x):
            result = 0
            while x:
                x &= (x-1)
                result += 1
            return result
        def sumK(arr):
            # this part is N*2^N with bitmask
            sk = [set() for _ in range(n+1)]            
            mask = (1<<n)-1 
            #for mask in range(1<<n):
            while mask:
                sm, j = 0, 0                
                #for i in range(n):
                while 1<<j <= mask:
                    if mask & (1<<j):
                        sm += arr[j]
                    j += 1
                #sk[popcount(mask)].add(sm)
                sk[bin(mask).count('1')].add(sm)
                mask = (mask-1) & (1<<n)-1
            #for k in range(n):
            #    sk[k].sort()            
            return [list(sk[k]) if k > 0 else [0] for k in range (n+1)]
        sumAk = sumK(A)
        sumBk = sumK(B)
        for k in range(n+1):
            sumBk[k].sort()
        ans = float('inf')
        for k in range(n+1):
            for sA in sumAk[k]:
                idx = bisect.bisect_left(sumBk[n-k], target - sA)
                if idx < len(sumBk[n-k]):
                    x = sA+sumBk[n-k][idx]
                    ans = min(ans, abs(x - (total-x)))
                if idx > 0:
                    x = sA+sumBk[n-k][idx-1]
                    ans = min(ans, abs(x - (total-x)))
        return ans            
        



        


    def minimumDifference2(self, nums: List[int]) -> int:
        # Brute force, TLE
        sm = sum(nums)
        ans = float('inf')
        for a in combinations(nums, len(nums)//2):
            t = 0
            for i in a:
                t += i
            ans = min(ans, abs(t - (sm-t)))
        return ans     
    
if __name__ == "__main__":
    print(Solution().minimumDifference([-36, 36]))
    print(Solution().minimumDifference1([-36, 36]))
    print(Solution().minimumDifference([3,9,7,3]))
    #print(Solution().minimumDifference2([3,9,7,3]))
    print(Solution().minimumDifference1([3,9,7,3]))
    print(Solution().minimumDifference([2,-1,0,4,-2,-9]))
    #print(Solution().minimumDifference2([2,-1,0,4,-2,-9]))
    print(Solution().minimumDifference1([2,-1,0,4,-2,-9]))
    arr = [7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694]
    print(Solution().minimumDifference(arr))
    print(Solution().minimumDifference1(arr))
    arr = [8127,-2194502,543358,2943,9353,-621995,-2,470,-10,894,477,-6539964,3263,645828,7464,-3429,185061,522873,-53,-2,-5237803,-9,595,-4,371,-7936123,-819148,-967672,-6394899,1424]
    print(Solution().minimumDifference(arr))
    print(Solution().minimumDifference1(arr))
    arr = [713,-884350,5704299,8679718,-930502,6719,-729188,6071783,-9413925,-231521,-7324443,-445068,-373233,-770354,-658646,-2295902,-92461,28,-548591,-593643,-7973359,-598119,-770172,-705188,-640994,8609,4058020,-4998532,4707715,-455679]
    print(Solution().minimumDifference(arr))
    print(Solution().minimumDifference1(arr))
    arr = [8211,2806,-9574,5576,5268,9250,487,-2663,3197,-5984,-3340,-6127,5414,9990,6713,-636,-5793,2647,2467,-6818,-9275,5152,5883,-1814,-9164,-9494,5820,454,-9524,-4141]
    print(Solution().minimumDifference(arr))
    print(Solution().minimumDifference1(arr))
