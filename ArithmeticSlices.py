'''
-Medium-

*DP*

A sequence of numbers is called arithmetic if it consists of at least three 
elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
 
A zero-indexed array A consisting of N numbers is given. A slice of that array 
is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means 
that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

 
Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

'''

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        """
        一维dp数组，其中dp[i]表示，到i位置为止的算数切片的个数，那么我们从第三个数字开始遍历，
        如果当前数字和之前两个数字构成算数切片，那么我们更新dp[i]为dp[i-1]+1，然后res累加上
        dp[i]的值即可：
        if A[i-2], A[i-1], A[i] are arithmetic, then the number of arithmetic slices 
        ending with A[i] (dp[i]) equals to:
            the number of arithmetic slices ending with A[i-1] (dp[i-1], all these 
            arithmetic slices appending A[i] are also arithmetic)
            +
            1 (A[i-2], A[i-1], A[i] forms a brand new arithmetic slice)
        """
        res, n = 0,  len(A)
        '''
        dp = [0] * n
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
            res += dp[i]
        '''
        dp_i_1, dp_i = 0, 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp_i = dp_i_1 + 1                
            else:
                dp_i = 0
            res += dp_i
            dp_i_1 = dp_i  
        return res

if __name__ == "__main__":
    print(Solution().numberOfArithmeticSlices([1, 2, 3, 4]))
    print(Solution().numberOfArithmeticSlices([1,2,3,8,9,10]))