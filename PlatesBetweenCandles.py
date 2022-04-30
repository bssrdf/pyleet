'''
-Medium-

There is a long table with a line of plates and candles arranged on top of it. You are 
given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' 
represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] 
denotes the substring s[lefti...righti] (inclusive). For each query, you need to 
find the number of plates between candles that are in the substring. A plate is 
considered between candles if there is at least one candle to its left and at least 
one candle to its right in the substring.

For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". 
The number of plates between candles in this substring is 2, as each of the two 
plates has at least one candle in the substring to its left and right.
Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:

ex-1
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.
Example 2:

ex-2
Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.
 

Constraints:

3 <= s.length <= 105
s consists of '*' and '|' characters.
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length



'''
from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        c, p = [0]*(n+1), [0]*(n+1)
        for i in range(n):
            if s[i] == '*': 
                p[i+1] = p[i] + 1
                c[i+1] = c[i]
            else:
                c[i+1] = c[i] + 1
                p[i+1] = p[i]
        ans = []
        def findFirstCandle(left, right):
            l, r = left, right+1
            while l < r:
                mid = l + (r-l)//2  
                k = c[mid+1]-c[left] 
                if  k > 1 or k == 1 and s[mid] != '|':
                    r = mid
                elif k == 0:
                    l = mid + 1
                else:
                    return mid
            return l
        def findLastCandle(left, right, m):
            l, r = left, right+1
            while l < r:
                mid = l + (r-l)//2  
                k = c[mid+1]-c[left] 
                if k < m:
                    l = mid + 1
                elif k == m and s[mid] != '|':
                    r = mid
                else:
                    return mid
            return l-1

        for l, r in queries:
            candles = c[r+1] - c[l]
            if candles < 2:
                ans.append(0)
            else:
                left = findFirstCandle(l, r)
                right = findLastCandle(l, r, candles)
                ans.append(p[right+1]-p[left])

                # print(candles, left, right)
        return ans
    
    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        p = [0]*(n+1)
        ans = []
        for i in range(n):
            if s[i] == '*': 
                p[i+1] = p[i] + 1
            else:
                p[i+1] = p[i]
        cL, cR = [-1]*n, [n]*n
        l = -1
        for i in range(n):
            if s[i] == '|':
                l = i
            cL[i] = l
        r = n
        for i in range(n-1, -1, -1):
            if s[i] == '|':
                r = i
            cR[i] = r
        for l, r in queries:
            left = cR[l]
            right = cL[r]
            #ans.append(p[right+1]-p[left])
            # print(left, right)
            if right > left:  
                ans.append(p[right+1]-p[left])
            else:
                ans.append(0)
        return ans






        

if __name__ == "__main__":
    # print(Solution().platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))
    # print(Solution().platesBetweenCandles(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))
    # print(Solution().platesBetweenCandles2(s = "**|**|***|", queries = [[2,5],[5,9]]))
    # print(Solution().platesBetweenCandles2(s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]))
    print(Solution().platesBetweenCandles2(s = "||*", queries = [[2,2]]))