'''
-Medium-
*Monotonic Stack*

Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the 
following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

 

Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000

'''


class Solution(object):
    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = nums
        res, n = 0,  len(arr)
        st = []
        for i in range(n):
            while st and arr[st[-1]] > arr[i] :
                st.pop()
            res += len(st)+1
            st.append(i)            
        return res

if __name__ == "__main__":
    print(Solution().validSubarrays([1,4,2,5,3]))
    print(Solution().validSubarrays([3,2,1]))
    print(Solution().validSubarrays([2,2,2]))
