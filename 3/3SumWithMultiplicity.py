'''
-Medium-

Given an integer array arr, and an integer target, return the number of tuples i, j, k such 
that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.
 

Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300


'''

class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """        
        
        n = len(arr)
        ans = 0
        MOD = 10**9+7
        m = {}
        for i in range(n-1):
            for j in range(i+1, n):
                if target - arr[j] - arr[i] in m:
                    ans += m[target - arr[j] - arr[i]]
            m[arr[i]] = m.setdefault(arr[i],0)+1
        return ans % MOD
    
    def threeSumMultiTwoPointers(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """        
        n = len(arr)
        arr.sort()
        ans = 0
        MOD = 10**9+7
        for i in range(n-2):
            j, k = i+1, n-1
            while j < k:  
                if arr[j]+arr[k] < target-arr[i]: j += 1
                elif arr[j]+arr[k] > target-arr[i]: k -= 1
                else: 
                    l, r = 1, 1
                    while j+l < k and arr[j+l] == arr[j]: l += 1
                    while k-r >= j+l and arr[k-r] == arr[k]: r += 1   
                    ans += (k-j+1)*(k-j)//2 if arr[k] == arr[j] else l*r
                    j += l
                    k -= r
        return ans % MOD

    def threeSumMultiUsingCombination(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """        
        
        n = len(arr)
        ans = 0
        MOD = 10**9+7
        count = [0]*101
        for a in arr:
            count[a] += 1 
        for i in range(target+1):
            for j in range(i, target+1):
                k = target - i - j
                if k < 0 or k >= 101 or k < j: continue
                if (count[i] == 0 or count[j] == 0 or count[k] == 0): continue
                if i == j and j == k:
                    ans += (count[i]-2)*(count[i]-1)*count[i]//6
                elif i == j and j != k:
                    ans += (count[i]-1)*count[i]//2*count[k]
                elif i != j and j == k:
                    ans += (count[j]-1)*count[j]//2*count[i]
                elif i != j and j != k:
                    ans += count[i]*count[j]*count[k]
        return ans % MOD

if __name__ == "__main__":
    print(Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8))
    print(Solution().threeSumMultiTwoPointers([1,1,2,2,3,3,4,4,5,5], 8))
    print(Solution().threeSumMultiUsingCombination([1,1,2,2,3,3,4,4,5,5], 8))

