'''
-Medium-
*Math*
*DP*


You are given an integer array nums. The adjacent integers in nums will perform the float division.

For example, for nums = [2,3,4], we will evaluate the expression "2/3/4".
However, you can add any number of parenthesis at any position to change the priority of operations. You want to add these parentheses such the value of the expression after the evaluation is maximum.

Return the corresponding expression that has the maximum value in string format.

Note: your expression should not contain redundant parenthesis.

 

Example 1:

Input: nums = [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, since they don't influence the operation priority. So you should return "1000/(100/10/2)".
Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Example 2:

Input: nums = [2,3,4]
Output: "2/(3/4)"
Example 3:

Input: nums = [2]
Output: "2"
 

Constraints:

1 <= nums.length <= 10
2 <= nums[i] <= 1000
There is only one optimal division for the given iput.




'''

from typing import List
import functools
import math

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # The standard DFS+Memo way is not easy because other than finding the max result, 
        # you also need to construct it's string expression.
        # In DFS, you remember both the max and min result for range [i,j]. [0,n-1] will 
        # be the final answer. You need to remember both max and min result because min 
        # result can be used as denominator.
        # It can also be explained in dp way:
        # dp(i,j) means the max and min result you can get for range [i,j], "k" represent 
        # any index between i~j.
        # max dp(i,j) = max dp(i,k) / min dp(k+1,j)
        # min dp(i,j) = min dp(i,k) / max dp(k+1,j)

        # Time: O(n^3) time, space: O(n^2)
        @functools.lru_cache(None)
        def dfs(start,end):
            if start==end:
                return nums[start],str(nums[start]),nums[end],str(nums[end])
            resmax,resmaxstr,resmin,resminstr=-1,'',math.inf,''
            for i in range(start,end):
                lmax,lmaxstr,lmin,lminstr=dfs(start,i)
                rmax,rmaxstr,rmin,rminstr=dfs(i+1,end)
                tmpmax=lmax/rmin
                if tmpmax>resmax:
                    resmax=tmpmax
                    if '/' in rminstr:
                        resmaxstr=lmaxstr+'/('+rminstr+')'
                    else:
                        resmaxstr=lmaxstr+'/'+rminstr
                tmpmin=lmin/rmax
                if tmpmin<resmin:
                    resmin=tmpmin
                    if '/' in rmaxstr:
                        resminstr=lminstr+'/('+rmaxstr+')'
                    else:
                        resminstr=lminstr+'/'+rmaxstr
                # tmpmin=lmin/rmax
            return resmax,resmaxstr,resmin,resminstr
        return dfs(0,len(nums)-1)[1]

    def optimalDivision2(self, nums: List[int]) -> str:
        # math solution
        A = nums
        return str(A[0]) + '/' +'(' + '/'.join(str(a) for a in A[1:]) + ')'

        

if __name__ == "__main__":
    print(Solution().optimalDivision(nums = [1000,100,10,2]))
    print(Solution().optimalDivision2(nums = [1000,100,10,2]))