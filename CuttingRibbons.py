'''
-Medium-

Given an array of integers with elements representing lengths of ribbons. Your goal is to obtain k ribbons of 
equal length cutting the ribbons into as many pieces as you want. Find the maximum integer length L to obtain 
at least k ribbons of length L.

Example 1:

Input: arr = [1, 2, 3, 4, 9], k = 5
Output: 3
Explanation: cut ribbon of length 9 into 3 pieces of length 3, length 4 into two pieces one of which is length 3 
and the other length 1,
and one piece is already is of length 3. So you get 5 total pieces (satisfying k) and the greatest length L 
possible which would be 3.

'''

class Solution:
    def maxLength(self, ribbons, k):
       
        def isCutPossible(length):
            ans = 0
            for r in ribbons:
                ans += r // length
            return ans >= k        
        left = 1
        right = max(ribbons)+1
        while left < right:
            mid = left + (right - left)//2
            if isCutPossible(mid):
                left = mid + 1
            else:
                right = mid
        return left-1



if __name__=="__main__":
  print(Solution().maxLength([1, 2, 3, 4, 9], 5))