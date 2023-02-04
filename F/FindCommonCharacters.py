'''

-Easy-

Given an array A of strings made only from lowercase letters, return a 
list of all characters that show up in all strings within the list 
(including duplicates).  For example, if a character occurs 3 times 
in all strings but not 4 times, you need to include that character three 
times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

'''

import sys 

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = []
        # for each lower case letter i (1-26), cnt[i]
        # contains the minimum number of occurrances of i 
        # in every word
        cnt = [sys.maxsize] * 26
        for word in A:
            t = [0] * 26
            for c in word: t[ord(c) - ord('a')] += 1
            for i in range(26):
                cnt[i] = min(cnt[i], t[i])
        for i in range(26):
            for j in range(cnt[i]):
                res.append(chr(ord('a') + i))
        return res


if __name__ == "__main__":
    print(Solution().commonChars(["bella","label","roller"]))
