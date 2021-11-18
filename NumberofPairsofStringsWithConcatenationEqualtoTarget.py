'''

-Medium-

*Hash Table*

Given an array of digit strings nums and a digit string target, return the number of 
pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] 
equals target.

 

Example 1:

Input: nums = ["777","7","77","77"], target = "7777"
Output: 4
Explanation: Valid pairs are:
- (0, 1): "777" + "7"
- (1, 0): "7" + "777"
- (2, 3): "77" + "77"
- (3, 2): "77" + "77"
Example 2:

Input: nums = ["123","4","12","34"], target = "1234"
Output: 2
Explanation: Valid pairs are:
- (0, 1): "123" + "4"
- (2, 3): "12" + "34"
Example 3:

Input: nums = ["1","1","1"], target = "11"
Output: 6
Explanation: Valid pairs are:
- (0, 1): "1" + "1"
- (1, 0): "1" + "1"
- (0, 2): "1" + "1"
- (2, 0): "1" + "1"
- (1, 2): "1" + "1"
- (2, 1): "1" + "1"
 

Constraints:

2 <= nums.length <= 100
1 <= nums[i].length <= 100
2 <= target.length <= 100
nums[i] and target consist of digits.
nums[i] and target do not have leading zeros.

'''
from typing import List

from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        def factorial(n):
            if n <= 1: return 1
            res = 1
            for i in range(2, n+1):
                res *= i
            return res
        m, res = Counter(nums), 0
        for i in range(1, len(target)):
            s1, s2  = target[:i], target[i:]
            if s1 == s2: 
                if m[s1] >= 2:
                    res += factorial(m[s1]) // factorial(m[s1]-2)                    
            elif s1 in m and s2 in m:
                res += m[s1] * m[s2]
        return res


if __name__ == "__main__":
    print(Solution().numOfPairs(nums = ["777","7","77","77"], target = "7777"))
    print(Solution().numOfPairs(nums = ["123","4","12","34"], target = "1234"))
    print(Solution().numOfPairs(nums = ["1","1","1"], target = "11"))
    print(Solution().numOfPairs(nums = ["1","111"], target = "11"))