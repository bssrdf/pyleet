'''


'''

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # can = [str(c)*2 for c in range(10)]
        # print(can)
        for i in range(n): 
            
            for j in range(i+1, n+1):
                s1 = s[i:j]
                cnt = 0
                for k in range(len(s1)-1):
                    if s1[k] == s1[k+1]: cnt += 1
                if cnt <= 1:
                    ans = max(ans, j-i) 
                #  print(i, j, ans, cnt)
        return ans


if __name__ == "__main__":
    print(Solution().longestSemiRepetitiveSubstring(s = "52233"))
    print(Solution().longestSemiRepetitiveSubstring(s = "1111111"))