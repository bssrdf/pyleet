'''
-Hard-
*Difference Array*
*Prefix Sum*

You are given an array nums. You can rotate it by a non-negative integer k so that the array 
becomes [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]. 
Afterward, any entries that are less than or equal to their index are worth one point.

For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it becomes [1,3,0,2,4]. This 
is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 
4 <= 4 [one point].

Return the rotation index k that corresponds to the highest score we can achieve if we rotated nums by it. 
If there are multiple answers, return the smallest such index k.

 

Example 1:

Input: nums = [2,3,1,4,0]
Output: 3
Explanation: Scores for each k are listed below: 
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
So we should choose k = 3, which has the highest score.
Example 2:

Input: nums = [1,3,0,2,4]
Output: 0
Explanation: nums will always have 3 points no matter how it shifts.
So we will choose the smallest k, which is 0.
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] < nums.length

'''

from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # This problem can be thought of as a transformation to a more well known problem. 
        # After we have the transformation, we can solve it effiently.

        # Definitions
        # Let A be the input array, and N be the number of elements in the array. Let A[i] denote 
        # the value at index i in input array A. And let K be the number of rotations.

        # The Transformation
        # For every number in the array, write the ranges which the value will yield a score of + 1.

        # Example:
        # A: [2, 3, 1, 4, 0]
        # Range for 2: [1, 3] (Rotating the array for any value of 1 <= K <= 3 will give us a point for 2.
        # Range for 3: [2, 3]
        # Range for 1: [0, 1] and [3, 4]
        # ... and so on

        # After doing that, the value of K that gives the highest score is the value that is common to 
        # the most # of ranges. The question is how do we solve for that value? A simple approach would 
        # be to keep an array, called count, with indices from 0 to 4, and add 1 to each indice for 
        # every range that contains it. At the end the best value of k is the indice for which count 
        # has the largest value.

        # Example:
        # count would look like this if we added + 1 for range [1, 3]: count [0, 1, 1, 1, 0]. We would 
        # continue to add for every range. So after adding range [2, 3], count would look like [0, 1, 2, 2, 0] 
        # ... and so on.

        # But this would be O(n^2). We can improve this by making a simple adaptation. To represent some 
        # range [a, b] we can instead add +1 to only the indice a, and subtract 1 to the last b + 1 (if it exists). 
        # This would mean that we add +1 to every index >= a, and subtract -1 to every index b + 1. After 
        # doing this for every range, we can accumate from the front, we should get the same array count, 
        # as we did with out n^2 version.
        A = nums 
        count = [0]*len(A)
        for i in range(len(A)):
            if A[i] <= i:
                # in this case: A[i] <= i, to get a point we can 
                # 1) take no moves since A[i] is already scoring a point
                # 2) move A[i] left to position A[i] which takes i-A[i] moves 
                # 3) move A[i] left to all positions b.w. 1) and 2)
                # 4) move A[i] left and then to N-1 position which takes i+1 moves  
                # 5) move A[i] left to i+1 position by first to N-1 and then left to i+1 which takes N-1 moves
                # 6) move A[i] to all positions b.w. 4) and 5)  
                # for case 4), 5), 6), we only need to increment count[i+1] because
                # count[N-1+1] = count[N] does not exist

                # the range for case 1), 2) and 3) [mini, maxi] 
                mini = 0
                maxi = i - A[i]
                count[mini] += 1
                if maxi + 1 < len(A): count[maxi + 1] += -1
                # the range for case 4), 5) and 6) [i+1, N-1] 
                if i + 1 < len(A): count[i+1] += 1 
            else:
                #if A[i] == len(A):
                #    continue #no valid range
                # in this case: A[i] > i, to get a point we can 
                # 1) move A[i] left and then to N-1 position which takes i+1 moves 
                # 2) move A[i] left to i by first to N-1 and then left to i which takes N-(A[i]-i) moves  
                # 3) move A[i] to all positions b.w. 1) and 2)

                # the range for case 1), 2) and 3) [mini, maxi] 
                mini = i + 1
                maxi = len(A) - (A[i] - i)
                count[mini] += 1
                if maxi + 1 < len(A): count[maxi + 1] += -1

        # count[] is in fact a difference array
        # we take prefixSum to recover the original array
        for i in range(1, len(A)):
            count[i] += count[i-1]
        #print('max score is ', max(count))
        return count.index(max(count)) # the highest score is max(count) 
                                       # while its index is the K that makes the highest score
                                     
        
if __name__=="__main__":
    print(Solution().bestRotation(nums = [2,3,1,4,0]))
    print(Solution().bestRotation([1,3,0,2,4]))