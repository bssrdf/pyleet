'''
-Hard-

Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they 
appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

 

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92
 

Constraints:

1 <= s.length <= 10^5
s consists of uppercase English letters only.

'''

class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        In each loop, We caculate cur[i], which represent the sum of Uniq() for all substrings whose last char is S.charAt(i).

        For example,
        S = 'ABCBD'
        When i = 2, cur[2] = Uniq('ABC') + Uniq('BC') + Uniq('C')
        When i = 3, cur[3] = Uniq('ABCB') + Uniq('BCB') + Uniq('CB') + Uniq('B')

        Notice, we append char 'B' into each previous substrings. Only in substrings 'CB' and 'B', 
        the char 'B' can be identified as uniq. The contribution of 'B' from cur[2] to cur[3] is 
        i - showLastPosition['B']. At the same time, in substrings 'ABCB', 'BCB', the char 'B' can‘t’ 
        be identified as uniq any more, the previous contribution of 'B' should be removed.

        So we have'cur[i] = cur[i - 1] - contribution[S.charAt(i)] + (i - showLastPosition[S.charAt(i)])
        Then the new contribution[S.charAt(i)] = i - showLastPosition[S.charAt(i)]

        The final result is the sum of all cur[i].

        The showLastPosition[x] represent the last showing positon of char x befor i. 
        (The initial showLastPosition[x] for all chars should be '-1'. For convenience, 
        I shift it to '0'. It may cause some confusion, notice I update 
        "showLastPosition[x] = i + 1" for each loop.)
        """
        res = 0
        if not s: return res    
        showLastPosition = [0]*26
        contribution = [0]*26
        cur = 0
        for i in range(len(s)):
            x = ord(s[i]) - ord('A')
            cur -= contribution[x]
            contribution[x] = (i - (showLastPosition[x] - 1))
            cur += contribution[x]
            showLastPosition[x] = i + 1
            res += cur
        return res



if __name__ == "__main__":
    print(Solution().uniqueLetterString('ABC'))