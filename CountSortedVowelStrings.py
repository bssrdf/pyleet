'''
-Medium-

Given an integer n, return the number of strings of length n that consist only 
of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as 
or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are 
["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
 

Constraints:

1 <= n <= 50 

'''

from functools import lru_cache

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        au = 'aeiou'
        m = len(au)
        self.ans = 0
        def helper(s, start):
            if len(s) == n:
                self.ans += 1
                return
            for i in range(start, m):
                helper(s+au[i], i)
        helper('', 0)
        return self.ans   



    def countVowelStringsMemo(self, n):
        """
        :type n: int
        :rtype: int
        """
        au = 'aeiou'
        m = len(au)
        memo = [[-1 for _ in range(n)] for _ in range(m)]        
        def helper(k, start):
            if k == n:                
                return 1
            if memo[start][k] != -1:
                return memo[start][k]
            cnt = 0
            for i in range(start, m):
                cnt += helper(k+1, i)
            memo[start][k] = cnt
            return cnt 
        return helper(0, 0)
        


if __name__=="__main__":
    print(Solution().countVowelStrings(1))
    print(Solution().countVowelStrings(2))
    print(Solution().countVowelStrings(33))
    print(Solution().countVowelStringsMemo(1))
    print(Solution().countVowelStringsMemo(2))
    print(Solution().countVowelStringsMemo(33))