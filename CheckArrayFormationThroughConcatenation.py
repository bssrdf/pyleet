'''

-Easy-

You are given an array of distinct integers arr and an array of integer 
arrays pieces, where the integers in pieces are distinct. Your goal is 
to form arr by concatenating the arrays in pieces in any order. However, 
you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, 
return false.

 

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true
Example 2:

Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
Example 3:

Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
Example 4:

Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
Example 5:

Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false
 

Constraints:

1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, 
all the integers in this array are distinct).

'''
from collections import defaultdict
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        m = defaultdict(int)
        for i,num in enumerate(pieces):
            for n in num: m[n] = i 
        nums = []
        last = -1
        for i in arr:
            if i in m:
                if last == -1: last = m[i]
                elif last == m[i]: continue                
                nums.extend(pieces[m[i]])
                last = m[i]
            else:
                return False
        if len(nums) != len(arr): return False
        for i, j in zip(arr, nums):
            if i != j: return False
        return True





if __name__ == "__main__":
    print(Solution().canFormArray([85], [[85]]))
    print(Solution().canFormArray([91,4,64,78], [[78],[4,64],[91]]))