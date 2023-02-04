'''
-Medium-

You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

Return the number of seconds needed to complete this process.

 

Example 1:

Input: s = "0110101"
Output: 4
Explanation: 
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.
Example 2:

Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.

Follow up:

Can you solve this problem in O(n) time complexity?


'''

class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        # O(N^2)
        s1 = s
        s = s.replace('01', '10')
        ans = 0
        while s1 != s:
            ans += 1
            s1 = s
            s = s.replace('01', '10')
        return ans

    def secondsToRemoveOccurrences2(self, s: str) -> int:
        # O(N)
        # 对于任何一个1而言，它的任何一次移动意味着超越了它之前的一个0.因为最终这个1要超越所有它之前的0，
        # 假设这些0的数目是count，那么说明这个1最少要移动count次。

        # 但是这个1极有可能会被前面的1所阻挡。一旦这个1的前进过程被阻挡到，那么意味着从此后，它的前进
        # 只能在前一个1移动一步之后再进行。也就是说，如果前一个1移动了x次到达期待位置，这一个1只能在
        # 第x+1步之后才能到达期待位置（也就是前一个1的后一个位置）。所以最终的答案是max(x+1,count)

        # 由此我们可以从前一个1的答案递归出下一个1的答案。最终答案就是最后一个1需要多少步移动到期待位置。
        cnt, res = 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1
            elif cnt > 0:
                res = max(res+1, cnt)
        return res 
        

if __name__ == "__main__":
    print(Solution().secondsToRemoveOccurrences(s = "0110101"))
    print(Solution().secondsToRemoveOccurrences(s = "11100"))
    print(Solution().secondsToRemoveOccurrences2(s = "0110101"))
    print(Solution().secondsToRemoveOccurrences2(s = "11100"))