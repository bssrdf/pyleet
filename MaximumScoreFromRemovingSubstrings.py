'''
-Medium-

*Greedy*

You are given a string s and two integers x and y. You can perform two types of operations any 
number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 10^5
1 <= x, y <= 10^4
s consists of lowercase English letters.


'''

class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        a, b = ("ab", "ba") if x > y else ("ba", "ab")
        x, y = (y, x) if x < y else (x, y)
        self.S = list(s)
        def remove(r, x):            
            i, ans = 0, 0
            for j in range(len(self.S)):
                self.S[i] = self.S[j]
                i += 1
                if i > 1 and self.S[i - 2] == r[0] and self.S[i - 1] == r[1]:
                    i -= 2 
                    ans += x # We keep removing pattern string `r` when `r` shows up in the end of written part.
            self.S = self.S[:i]
            return ans
        return remove(a, x)+remove(b, y)




if __name__ == "__main__":
    print(Solution().maximumGain("cdbcbbaaabab",  4,  5))