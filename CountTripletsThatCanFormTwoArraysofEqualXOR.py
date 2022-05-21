'''

-Medium-


Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108



'''

from typing import List
from collections import Counter

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        preXor = [0]*n
        preXor[0] = arr[0]
        ans = 0
        for i in range(1, n):
            preXor[i] = preXor[i-1] ^ arr[i]
        for i in range(n-1):
            for j in range(i+1, n):   
                a = (preXor[j-1] ^ preXor[i-1]) if i > 0 else preXor[j-1]
                for k in range(j, n):
                    b = (preXor[k] ^ preXor[j-1])
                    if a == b: ans += 1
        return ans
    
    def countTriplets2(self, arr: List[int]) -> int:
        n = len(arr)
        preXor = [0]*n
        preXor[0] = arr[0]
        ans = 0
        for i in range(1, n):
            preXor[i] = preXor[i-1] ^ arr[i]
        for j in range(1, n):   
            cnt = Counter()
            for i in range(j):
                a = (preXor[j-1] ^ preXor[i-1]) if i > 0 else preXor[j-1]
                cnt[a] += 1                            
            for k in range(j, n):
                b = preXor[k] ^ preXor[j-1]
                if b in cnt:
                   ans += cnt[b]
            # print(j, ans, cnt)
        return ans




if __name__ == "__main__":
    print(Solution().countTriplets(arr = [2,3,1,6,7]))
    print(Solution().countTriplets(arr = [1,1,1,1,1]))
    print(Solution().countTriplets2(arr = [2,3,1,6,7]))
    print(Solution().countTriplets2(arr = [1,1,1,1,1]))