'''

-Medium-


You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105


'''
from typing import List
from collections import Counter

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        totalOdd, totalEven = n//2, n//2+1 if n%2 == 1 else n//2
        even = Counter(nums[::2])        
        odd  = Counter(nums[1::2]) 
        e1, e2 = 0, 0, 
        et1, et2 = 0, 0 
        for i in even:
            if even[i] >= e1:
                e2, et2 = e1, et1  
                e1, et1 = even[i], i
            elif even[i] >= e2:
                e2, et2 = even[i], i
        o1, o2 = 0, 0
        ot1, ot2 = 0, 0 
        for i in odd:
            if odd[i] >= o1:
                o2, ot2 = o1, ot1  
                o1, ot1 = odd[i], i
            elif odd[i] >= o2:
                o2, ot2 = odd[i], i
        # print(et1, ot1, et2, ot2)
        operationsEven, operationsOdd = 0, 0
        operationsEven = totalEven - e1
        if et1 != ot1:
            operationsEven += (totalOdd - o1)
        else:
            operationsEven += (totalOdd - o2)
        operationsOdd = totalOdd - o1
        if et1 != ot1: 
            operationsOdd += (totalEven - e1)
        else:
            operationsOdd += (totalEven - e2)

        return min(operationsEven, operationsOdd)

if __name__ == "__main__":
    print(Solution().minimumOperations([3,1,3,2,4,3]))
    print(Solution().minimumOperations([1,2,2,2,2]))
    print(Solution().minimumOperations([2,1,3,1,1,3,1,3]))
    print(Solution().minimumOperations([1,1,3,1,2,2]))
        