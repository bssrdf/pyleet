'''
-Medium-
*Two Pointers*
*Sliding Window*

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
 

Note:

1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1 

'''

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        left, right = 0, 0
        cnt0, cnt1 = 0, 0
        res = 0
        while right < n:
            if A[right] == 0:
                cnt0 += 1
            else:
                cnt1 += 1    
            if cnt0 <= K: # change up to K 
                res = max(res, cnt0+cnt1)
            elif cnt0 > K:
                # we got another 0, so move left pointer to 
                # skip the leftmost 0 to make # of 0's back to K; 
                # during moving, if passing 1, reduce its count 
                while left <= right and A[left] == 1:
                    cnt1 -= 1
                    left += 1
                left += 1
                cnt0 -= 1
            right += 1
        return res
                    

if __name__ == "__main__":
    print(Solution().longestOnes([0,0,0,1], 4))
    #'''
    print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
    print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 0))
    #'''