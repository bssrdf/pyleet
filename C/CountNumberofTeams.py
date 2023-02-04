'''
-Medium-

*Fenwick Tree*
*DP*

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).

A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) 
where (0 <= i < j < k < n).

Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10^5
All the integers in rating are unique.


'''

class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        n = len(rating)
        res = 0
        rs, rb = [0]*n, [0]*n
        for i in range(n):            
            for j in range(i+1, n):
                if rating[j] > rating[i]:
                    rb[i] += 1
                else:
                    rs[i] += 1

        for i in range(n):
            ls, lb = 0, 0            
            for j in range(i):
                if rating[j] > rating[i]:
                    lb += 1
                else:
                    ls += 1
            res += ls * rb[i] + lb * rs[i]
        return res
    
    def numTeamsBIT(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        print('input', rating)
        RMAX = max(rating)
        n = len(rating)
        leftTree = [0]*(RMAX + 1)
        rightTree = [0]*(RMAX + 1)
        def update(BIT, index, val):
            while index < len(BIT):
                BIT[index] += val
                index += index & (-index)
        def getPrefixSum(BIT, index):
            sm = 0
            while index > 0:
                sm += BIT[index]
                index -= index & (-index)
            return sm
        def getSuffixSum(BIT, index):
            return getPrefixSum(BIT, RMAX) - getPrefixSum(BIT, index - 1)

        for r in rating: 
            update(rightTree, r, 1)
            print(rightTree)


        res = 0
        for r in rating:
            update(rightTree, r, -1)
            print('after removing', r, rightTree)
            res += (getPrefixSum(leftTree, r - 1) * getSuffixSum(rightTree, r + 1)) # count increase
            print(getSuffixSum(rightTree, r + 1), 'bigger than', r)
            print(getPrefixSum(leftTree, r - 1), 'smaller than', r)
            res += (getSuffixSum(leftTree, r + 1) * getPrefixSum(rightTree, r - 1)) # count decrease
            update(leftTree, r, 1)
            print('left tree after adding', r, leftTree)


        return res

        

if __name__ == "__main__":
    print(Solution().numTeams([2,5,3,4,1]))
    print(Solution().numTeamsBIT([2,5,3,4,1]))