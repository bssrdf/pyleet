'''
-Medium-
*Monotonic Queue*

Given an array A of positive integers, A[i] represents the value of the i-th 
sightseeing spot, and two sightseeing spots i and j have distance j - i between 
them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : 
the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 

Note:

2 <= A.length <= 50000
1 <= A[i] <= 1000

'''

from collections import deque

class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        q = deque()
        res = 0 
        for i in range(len(A)):
            if q:
                res = max(res, A[i]+A[q[0]]+q[0]-i)      
            while q and A[i]-A[q[-1]] >= q[-1]-i:            
                q.pop()                  
            q.append(i)
        return res
            

        

if __name__ == "__main__":
    print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))
    print(Solution().maxScoreSightseeingPair([1,2]))
    print(Solution().maxScoreSightseeingPair([7,8,8,10]))
    print(Solution().maxScoreSightseeingPair([7,2,6,6,9,4,3]))