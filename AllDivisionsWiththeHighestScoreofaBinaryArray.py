'''
-Medium-

You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:

numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
If i == 0, numsleft is empty, while numsright has all the elements of nums.
If i == n, numsleft has all the elements of nums, while numsright is empty.
The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

Return all distinct indices that have the highest possible division score. You may return the answer in any order.

 

Example 1:

Input: nums = [0,0,1,0]
Output: [2,4]
Explanation: Division at index
- 0: numsleft is []. numsright is [0,0,1,0]. The score is 0 + 1 = 1.
- 1: numsleft is [0]. numsright is [0,1,0]. The score is 1 + 1 = 2.
- 2: numsleft is [0,0]. numsright is [1,0]. The score is 2 + 1 = 3.
- 3: numsleft is [0,0,1]. numsright is [0]. The score is 2 + 0 = 2.
- 4: numsleft is [0,0,1,0]. numsright is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
Example 2:

Input: nums = [0,0,0]
Output: [3]
Explanation: Division at index
- 0: numsleft is []. numsright is [0,0,0]. The score is 0 + 0 = 0.
- 1: numsleft is [0]. numsright is [0,0]. The score is 1 + 0 = 1.
- 2: numsleft is [0,0]. numsright is [0]. The score is 2 + 0 = 2.
- 3: numsleft is [0,0,0]. numsright is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
Example 3:

Input: nums = [1,1]
Output: [0]
Explanation: Division at index
- 0: numsleft is []. numsright is [1,1]. The score is 0 + 2 = 2.
- 1: numsleft is [1]. numsright is [1]. The score is 0 + 1 = 1.
- 2: numsleft is [1,1]. numsright is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
 

Constraints:

n == nums.length
1 <= n <= 105
nums[i] is either 0 or 1.


'''

from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros, ones = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            zeros[i+1] = zeros[i] + (1 if nums[i] == 0 else 0)
            ones[i+1] = ones[i] + (1 if nums[i] == 1 else 0)
        # print(zeros)
        # print(ones)
        score, maxScore, maxIndex = 0, ones[-1], [0]
        if zeros[-1] > maxScore:
            maxScore = zeros[-1]
            maxIndex = [n]
        elif zeros[-1] == maxScore:
            maxIndex.append(n)    
        for i in range(1,n):
            
            score = zeros[i] - zeros[0] + ones[-1] - ones[i]
            if score > maxScore:
                maxScore = score
                maxIndex = [i]
            elif score == maxScore:
                maxIndex.append(i)
        return maxIndex
    
    def maxScoreIndices2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ones = [0]*(n+1)
        for i in range(n):
            ones[i+1] = ones[i] + (1 if nums[i] == 1 else 0)
        # print(zeros)
        # print(ones)
        score, maxScore, maxIndex = 0, ones[-1], [0]
        zeros = 0
        for i in range(1,n+1):
            if nums[i-1] == 0: zeros += 1
            score = zeros + ones[-1] - ones[i]
            if score > maxScore:
                maxScore = score
                maxIndex = [i]
            elif score == maxScore:
                maxIndex.append(i)
        
        return maxIndex
    
    def maxScoreIndices3(self, nums: List[int]) -> List[int]:
        n = len(nums)
        allones = sum(1 if i == 1 else 0 for i in nums)
        # print(zeros)
        # print(ones)
        score, maxScore, maxIndex = 0, 0, [0]
        zeros, ones = 0, 0
        for i in range(1,n+1):
            if nums[i-1] == 0: 
                zeros += 1
            else:
                ones += 1
            score = zeros - ones
            if score > maxScore:
                maxScore = score
                maxIndex = [i]
            elif score == maxScore:
                maxIndex.append(i)
        
        return maxIndex