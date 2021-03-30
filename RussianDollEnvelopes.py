'''
-Hard-

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] 
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of 
one envelope is greater than the width and height of the other envelope.

Return the maximum number of envelopes can you Russian doll (i.e., put one 
inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 10^4
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0],(-x[1])))
        dp = []
        for w, h in envelopes:
            l, r = 0, len(dp)
            while l < r:
                mid = l + (r-l)//2
                if dp[mid] >= h:
                    r = mid
                else:
                    l = mid + 1
            if r >= len(dp):
                dp.append(h)
            else:
                dp[r] = h
            print(dp)
        return len(dp)



if __name__ == "__main__":
    print(Solution().maxEnvelopes([[5,5],[6,4],[6,7],[2,3]]))
    print(Solution().maxEnvelopes([[1,1],[1,1],[1,1]]))
