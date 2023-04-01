'''
-Medium-
*GCD*
*Sorting*

You are given a 0-indexed integer array arr and an integer k. The array arr is circular. In other words, the first element of the array is the next element of the last element, and the last element of the array is the previous element of the first element.

You can do the following operation any number of times:

Pick any element from arr and increase or decrease it by 1.
Return the minimum number of operations such that the sum of each subarray of length k is equal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: arr = [1,4,1,3], k = 2
Output: 1
Explanation: we can do one operation on index 1 to make its value equal to 3.
The array after the operation is [1,3,1,3]
- Subarray starts at index 0 is [1, 3], and its sum is 4 
- Subarray starts at index 1 is [3, 1], and its sum is 4 
- Subarray starts at index 2 is [1, 3], and its sum is 4 
- Subarray starts at index 3 is [3, 1], and its sum is 4 
Example 2:

Input: arr = [2,5,5,7], k = 3
Output: 5
Explanation: we can do three operations on index 0 to make its value equal to 5 and two operations on index 3 to make its value equal to 5.
The array after the operations is [5,5,5,5]
- Subarray starts at index 0 is [5, 5, 5], and its sum is 15
- Subarray starts at index 1 is [5, 5, 5], and its sum is 15
- Subarray starts at index 2 is [5, 5, 5], and its sum is 15
- Subarray starts at index 3 is [5, 5, 5], and its sum is 15 
 

Constraints:

1 <= k <= arr.length <= 105
1 <= arr[i] <= 109


'''

from typing import List
import heapq
from math import gcd
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        sums = [0]*n
        t = 0
        j = 0
        pq = []
        for i in range(2*n):
            t += arr[i % n]
            if i >= k:
                t -= arr[(i-k)%n]           
            if i >= k-1:
                sums[j] = t
                j += 1
            if j == n: break
        print(sums)
        sums.sort()
        target = sums[n//2]

        for i in range(2*n):
            heapq.heappush(pq, abs(arr[i%n]-target))


        return 0     
    
    def makeSubKSumEqual2(self, arr: List[int], k: int) -> int:
        # Key Intuition
        # Let’s first look at a toy example by assuming k = 3. Because the 
        # problem requires the sum of each subarray of length k to be equal, 
        # we then need to have arr[0] + arr[1] + arr[2] = arr[1] + arr[2] + arr[3], which 
        # implies that arr[0] = arr[3]. Essentially, this is saying that every k-th 
        # element of arr needs to be equal after all operations.

        # There is one caveat yet to make the argument complete: In this problem arr is 
        # not only a regular array but also a circular array. Suppose n = 6 and k = 4, 
        # we need to have every gcd(n, k) = gcd(6, 4) = 2-th element of arr to be equal 
        # after all operations.

        n = len(arr)        
        k = gcd(n, k)
        v = [[] for i in range(k)]
        for i in range(n):
            v[i % k].append(arr[i])
        ans = 0
        for i in range(k):
            v[i].sort()
            x = v[i][len(v[i]) // 2]
            for j in v[i]:
                ans += abs(x - j)
        return ans

    

if __name__ == '__main__':
    print(Solution().makeSubKSumEqual(arr = [1,4,1,3], k = 2))