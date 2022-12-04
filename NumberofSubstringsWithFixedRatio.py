'''
-Medium-

$$$

*Hash Table*


You are given a binary string s, and two integers num1 and num2. num1 and num2 are coprime numbers.

A ratio substring is a substring of s where the ratio between the number of 0's and the number of 1's in the substring is exactly num1 : num2.

For example, if num1 = 2 and num2 = 3, then "01011" and "1110000111" are ratio substrings, while "11000" is not.
Return the number of non-empty ratio substrings of s.

Note that:

A substring is a contiguous sequence of characters within a string.
Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.
 

Example 1:

Input: s = "0110011", num1 = 1, num2 = 2
Output: 4
Explanation: There exist 4 non-empty ratio substrings.
- The substring s[0..2]: "0110011". It contains one 0 and two 1's. The ratio is 1 : 2.
- The substring s[1..4]: "0110011". It contains one 0 and two 1's. The ratio is 1 : 2.
- The substring s[4..6]: "0110011". It contains one 0 and two 1's. The ratio is 1 : 2.
- The substring s[1..6]: "0110011". It contains two 0's and four 1's. The ratio is 2 : 4 == 1 : 2.
It can be shown that there are no more ratio substrings.
Example 2:

Input: s = "10101", num1 = 3, num2 = 1
Output: 0
Explanation: There is no ratio substrings of s. We return 0.
 

Constraints:

1 <= s.length <= 105
1 <= num1, num2 <= s.length
num1 and num2 are coprime integers.

'''
from collections import Counter

class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        '''
        前缀和 + 计数

        我们用 one[i] 表示字符串 s[0,..i] 中 '1' 的个数，用 zero[i] 表示字符串 s[0,..i] 
        中 '0' 的个数。子串符合条件，需要满足

        
        (zero[j] - zero[i]) / (one[j] - one[i]) = num1 / num2
        

        其中 i < j。我们可以将上式转化为

        
        one[j] * num1 - zero[j] * num2 = one[i] * num1 - zero[i] * num2
        

        遍历到下标 j 时，我们只需要统计有多少个下标 i 满足上式即可。因此，我们可以用
        哈希表记录 one[i] * num1 - zero[i] * num2 出现的次数，遍历到下标 j 时，
        只需要统计 one[j] * num1 - zero[j] * num2 出现的次数即可。

        哈希表初始时只有一个键值对 {0:1}。

        时间复杂度 O(n)，空间复杂度 O(n)。其中 n 为字符串 s 的长度。
        '''
        n0 = n1 = 0
        ans = 0
        cnt = Counter({0: 1})
        for c in s:
            n0 += c == '0'
            n1 += c == '1'
            x = n1 * num1 - n0 * num2
            # x = n0 * num2 - n1 * num1
            # print('A', c, n0, n1, x, ans, cnt)
            ans += cnt[x]            
            cnt[x] += 1
            # print('B', n0, n1, x, ans, cnt)
        return ans


if __name__ == "__main__":
    print(Solution().fixedRatio(s = "0110011", num1 = 1, num2 = 2))
