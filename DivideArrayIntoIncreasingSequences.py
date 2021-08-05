'''
-Hard-
*Math*


Given a non-decreasing array of positive integers nums and an integer K, find out if this 
array can be divided into one or more disjoint increasing subsequences of length at least K.

 

Example 1:

Input: nums = [1,2,2,3,3,4,4], K = 3
Output: true
Explanation: 
The array can be divided into the two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
Example 2:

Input: nums = [5,6,6,7,8], K = 3
Output: false
Explanation: 
There is no way to divide the array using the conditions required.
 

Note:

1 <= nums.length <= 10^5
1 <= K <= nums.length
1 <= nums[i] <= 10^5
Hints
Think in the frequency of the numbers and how this affects the number of sequences needed.
What is the minimum number of sequences we need to form? Considering frequency of the numbers.
Think about the least number of sequences to maximize the lengths.
The number of sequences needed is equal to the maximum frequency of an element.
How to put the other elements into sequences ? Think in a greedy approach.

'''

from collections import Counter

class Solution(object):
    def canDivideIntoSubsequencesMath(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        counter = Counter(nums)
        n = max(counter.values())
        return n*K <= len(nums)

    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        counter = Counter(nums)
        n = max(counter.values())
        if n*K > len(nums): return False
        while n > 0:
            m = K
            for c in counter:
                if counter[c] > 0: 
                    counter[c] -= 1
                    m -= 1                
                if m == 0: break
           # print(n, m, counter)
            if m > 0: return False
            n -= 1
        return True



if __name__ == "__main__":
    print(Solution().canDivideIntoSubsequences(nums = [1,2,2,3,3,4,4], K = 3))
    print(Solution().canDivideIntoSubsequences([5,6,6,7,8], K = 3))