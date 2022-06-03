'''

-Hard-
*Monotonic Stack*
*Prefix Max*
*Suffix Min*


You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
 

Constraints:

1 <= arr.length <= 2000
0 <= arr[i] <= 108

'''

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Intuition: the mono-stack keeps the max of each chunk, when 
        # the max of current chunk is larger than next number, merge next 
        # number to current chunk (with stack.pop())
        stack = []
        for num in arr:
            largest = num
            while stack and stack[-1] > num:
                largest = max(largest, stack.pop())
            stack.append(largest)
        
        return len(stack)

    def maxChunksToSorted2(self, arr: List[int]) -> int:
        n = len(arr)
        preMax, sufMin = [0]*n, [0]*n 
        preMax[0] = arr[0]
        for i in range(1, n):
            preMax[i] = max(preMax[i-1], arr[i])
        sufMin[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            sufMin[i] = min(sufMin[i+1], arr[i])
        res = 0
        for i in range(n-1):
            if preMax[i] <= sufMin[i+1]: res += 1
        return res+1



        


if __name__ == "__main__":
    print(Solution().maxChunksToSorted(arr = [5,4,3,2,1]))
    print(Solution().maxChunksToSorted(arr = [2,1,3,4,4]))
    print(Solution().maxChunksToSorted2(arr = [5,4,3,2,1]))
    print(Solution().maxChunksToSorted2(arr = [2,1,3,4,4]))