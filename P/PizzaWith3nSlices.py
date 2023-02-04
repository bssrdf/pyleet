'''

-Hard-
*DP*


There is a pizza with 3n slices of varying size, you and your friends 
will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick the next slice in the anti-clockwise 
direction of your pick.
Your friend Bob will pick the next slice in the clockwise direction 
of your pick.
Repeat until there are no more slices of pizzas.
Given an integer array slices that represent the sizes of the pizza 
slices in a clockwise direction, return the maximum possible sum of 
slice sizes that you can pick.

 

Example 1:


Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
Example 2:


Input: slices = [8,9,8,6,1,1]
Output: 16
Explanation: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
 

Constraints:

3 * n == slices.length
1 <= slices.length <= 500
1 <= slices[i] <= 1000

'''


from typing import List

'''
In the house robber II problem, we are not forced to choose any fixed number of houses. 
Like out of 3n houses we can choose either total of 1 or 2 or n/2 or n... houses. 
Problem statement are not imposing any such condition. So except the smart trick to 
get rid of circular array problem, 1D dp solution is very easy to come up with.

In this problem: Condition has been imposed that we have to choose n elements out of 3n. 
Now forget that we have to choose n elements and try to solve it, in such case we may 
end up choosing exactly n elements or higher or lower. But we need to ensure that we 
choose exactly n elements. So the DP solution will be to get the maximum by 
choosing 1 , 2, 3, 4, ...n element from 3n elements. Now that's what made the DP 
solution from 1D to 2D.


'''
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # The problem is asking given 3n slices of pizza and we want to pick n slices 
        # of pizza from them and try to maximize the size of pizza we picked. So, 
        # in dp[i][j], i means the i th slices of pizza, we can choose to pick this 
        # slice or not. j means we already have j slices of pizza or we picked j slices 
        # pizza already. Therefore, dp[i][j] means the maximum size of j slices of pizza 
        # we got so far.
        m = len(slices)
        n = m//3  
        def maxSum(arr):
            m = len(arr)
            dp = [[0]*(n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if i == 1:
                        dp[i][j] = arr[0]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i-2][j-1]+arr[i-1])
            return dp[m][n]
        return max(maxSum(slices[:m-1]), maxSum(slices[1:m]))
    

    def maxSizeSlices2(self, slices: List[int]) -> int:
        m = len(slices)
        n = m//3  
        def maxSum(arr):
            m = len(arr)
            dp  = [0]*(n+1)
            dp1 = [0]*(n+1)
            dp2 = [0]*(n+1)
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if i == 1:
                        dp[j] = arr[0]
                    else:
                        dp[j] = max(dp1[j], dp2[j-1]+arr[i-1])
                dp1, dp2, dp = dp, dp1, dp2 
            return dp1[n]
        return max(maxSum(slices[:m-1]), maxSum(slices[1:m]))



if __name__ == "__main__":
    print(Solution().maxSizeSlices([1,2,3,4,5,6]))
    print(Solution().maxSizeSlices2([1,2,3,4,5,6]))
    print(Solution().maxSizeSlices([8,9,8,6,1,1]))
    print(Solution().maxSizeSlices2([8,9,8,6,1,1]))
        