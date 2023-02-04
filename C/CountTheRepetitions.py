'''

-Hard-

We define str = [s, n] as the string str which consists of the string s concatenated n times.

For example, str == ["abc", 3] =="abcabcabc".
We define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.

For example, s1 = "abc" can be obtained from s2 = "abdbec" based on our definition by removing the bolded underlined characters.
You are given two strings s1 and s2 and two integers n1 and n2. You have the two strings str1 = [s1, n1] and str2 = [s2, n2].

Return the maximum integer m such that str = [str2, m] can be obtained from str1.

 

Example 1:

Input: s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
Output: 2
Example 2:

Input: s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
Output: 1
 

Constraints:

1 <= s1.length, s2.length <= 100
s1 and s2 consist of lowercase English letters.
1 <= n1, n2 <= 106

'''


class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        d, l1, l2, i1, i2 = {}, len(s1), len(s2), 0, 0
        tot = l1 * n1

        while i1 < tot:
            if s1[i1 % l1] == s2[i2 % l2]:
                if (i1 % l1, i2 % l2) in d:
                    prev1, prev2 = d[(i1 % l1, i2 % l2)]
                    cir1, cir2 = i1 - prev1, i2 - prev2
                    count_cir1 = (tot - i1) // cir1
                    i1 += count_cir1 * cir1
                    i2 += count_cir1 * cir2
                    if i1 >= tot: break
                else:
                    d[(i1 % l1, i2 % l2)] = (i1, i2)
                i2 += 1
            i1 += 1
        return i2 // (l2 * n2)


if __name__ == "__main__":
    print(Solution().getMaxRepetitions(s1 = "acb", n1 = 4, s2 = "ab", n2 = 2))
        