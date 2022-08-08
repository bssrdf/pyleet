'''

-Medium-

Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

 

Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.
Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.
 

Constraints:

1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15


'''

from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:        
        start = 10**((intLength+1)//2-1)
        ans = [0]*len(queries)
        idx = -2 if intLength % 2 == 1 else -1 
        for i,q in enumerate(queries):
            t = start + q - 1
            s = str(t)+str(t)[idx::-1]
            if len(s) > intLength:
                ans[i] = -1
            else:            
                ans[i] = int(s)
        return ans

if __name__ == "__main__":
    print(Solution().kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3))
    print(Solution().kthPalindrome(queries = [2,4,6], intLength = 4))
    print(Solution().kthPalindrome(queries = [2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], intLength = 1))
    qrs = [94,18,388481008,38,16017953,16,223505660,78,123699557,346244579,2]
    print(Solution().kthPalindrome(queries = qrs, intLength = 8))
