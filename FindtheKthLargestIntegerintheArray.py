'''
-Medium-

You are given an array of strings nums and an integer k. Each string in nums 
represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, 
if nums is ["1","2","2"], "2" is the first largest integer, 
"2" is the second-largest integer, and "1" is the third-largest integer.

 

Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".
Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".
Example 3:

Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".
 

Constraints:

1 <= k <= nums.length <= 10^4
1 <= nums[i].length <= 100
nums[i] consists of only digits.
nums[i] will not have any leading zeros.

'''

from typing import List
from random import randint
import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        def partition(p, r):           
            x = nums[r]
            i = p-1
            for j in range(p,r):
                if int(nums[j]) < int(x):
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1],nums[r] = nums[r], nums[i+1]    
            return i+1     

        def random_partition(p,r):
            ri = randint(p,r)
            nums[ri], nums[r] = nums[r], nums[ri]
            return partition(p, r)     

        def select(p, r, k):
            # returns kth smallest
            if p == r:
                return nums[p]
            q = random_partition(p, r)
            i = q-p+1
            if i == k:
                return nums[q]
            elif k < i:
                return select(p, q-1, k)
            else:
                return select(q+1, r, k-i)
        n = len(nums)    
        return select(0, n-1, n-k+1)   

    def kthLargestNumber2(self, nums: List[str], k: int) -> str:
        minHeap = []
        for x in nums:
            heapq.heappush(minHeap, int(x))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        return str(minHeap[0])

if __name__ == "__main__":
    print(Solution().kthLargestNumber(nums = ["3","6","7","10"], k = 4))
    print(Solution().kthLargestNumber2(nums = ["3","6","7","10"], k = 4))
    arr = ['0']*10000
    #print(Solution().kthLargestNumber(nums = arr, k = 1))
    arr = ['3']*10000
    #print(Solution().kthLargestNumber(nums = arr, k = 10000))
