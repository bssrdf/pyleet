'''
-Hard-

*DP*

There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place 
and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which 
will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.

'''

class Solution:
    def strangePrinter(self, s: str) -> int:
        # 思考的线索和思路很重要，不理解核心精髓，当背题侠是没用的，稍微变个形式又不会了，博主就经常是这样的-.-!!!。
        # 既然说了要用DP来做，先整个二维dp数组呗，其中dp[i][j]表示打印出字符串[i, j]范围内字符的最小步数，难点就
        # 是找递推公式啦。遇到乍看去没啥思路的题，博主一般会先从简单的例子开始，看能不能分析出规律，从而找到解题的线索。
        # 首先如果只有一个字符，比如字符串是"a"的话，那么直接一次打印出来就行了。如果字符串是"ab"的话，那么我们要么先
        # 打印出"aa"，再改成"ab"，或者先打印出"bb"，再改成"ab"。同理，如果字符串是"abc"的话，就需要三次打印。
        # 那么一个很明显的特征是，如果没有重复的字符，打印的次数就是字符的个数。燃鹅这题的难点就是要处理有相同字符的情况，
        # 比如字符串是"aba"的时候，我们先打"aaa"的话，两步就搞定了，如果先打"bbb"的话，就需要三步。我们再来看一个字符
        # 串"abcb"，我们知道需要需要三步，我们看如果把这个字符串分成两个部分"a"和"bcb"，它们分别的步数是1和2，加起来
        # 的3是整个的步数。而对于字符串"abba"，如果分成"a"和"bba"，它们分别的步数也是1和2，但是总步数却是2。这是因为
        # 分出的"a"和"bba"中的最后一个字符相同。对于字符串"abbac"，因为位置0上的a和位置3上的a相同，那么整个字符串的步数
        # 相当于"bb"和"ac"的步数之和，为3。那么分析到这，是不是有点眉目了？我们关心的是字符相等的地方，对于[i, j]范围
        # 的字符，我们从i+1位置上的字符开始遍历到j，如果和i位置上的字符相等，我们就以此位置为界，将[i+1, j]范围内的字符
        # 拆为两个部分，将二者的dp值加起来，和原dp值相比，取较小的那个。所以我们的递推式如下:

        # dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j]       (s[k] == s[i] and i + 1 <= k <= j)
        # 要注意一些初始化的值，dp[i][i]是1，因为一个字符嘛，打印1次，还是就是在遍历k之前，dp[i][j]初始化为 1 + dp[i + 1][j]，
        # 为啥呢，可以看成在[i + 1, j]的范围上多加了一个s[i]字符，最坏的情况就是加上的是一个不曾出现过的字符，步数顶多加1步，
        # 注意我们的i是从后往前遍历的，当然你可以从前往后遍历，参数对应好就行了，参见代码如下：
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = 1 if i == j else 1 + dp[i+1][j]
                for k in range(i+1, j+1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1]+dp[k][j])
        return dp[0][n-1]

        

if __name__ == '__main__':
    print(Solution().strangePrinter(s = "aaabbb"))