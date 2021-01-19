'''
-Medium-

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        self.cnt = 0
        self.ans = s[0]
        def compare_two_sides(count, left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                count += 2
                if count > self.cnt:
                    self.cnt = count
                    self.ans = s[left:right+1]
                left -= 1
                right += 1                
            return 

        for i in range(n):
            compare_two_sides(1,i-1,i+1)
            compare_two_sides(0,i-1,i)
           
        return self.ans

    def longestPalindromeDP(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        state variable:
        start index and end index of a substring can identify a state, which 
        influences our decision
        so state variable is state(s, e) indicates whether str[s, e] is palindromic
        goal state:
        max(e - s + 1) that makes state(s, e) = true
        state transition:
        
        Let's observe example base cases

        for s = e, "a" is palindromic,
        for s + 1 = e, "aa" is palindromic (if str[s] = str[e])
        for s + 2 = e, "aba" is palindromic (if str[s] = str[e] and "b" is palindromic)
        for s + 3 = e, "abba" is palindromic (if str[s] = str[e] and "bb" is palindromic)
        we realize that

        for s + dist = e, str[s, e] will be palindromic (if str[s] == str[e] and 
        str[s + 1, e - 1] is palindromic) 

        note:
        state(s + 1, e - 1) should be calculated before state(s, e). That is, s is 
        decreasing during the bottop-up dp implementation, while the dist between 
        s and e is increasing, that's why

        for (int s = len - 1; s >= 0; s--) {
            for (int dist = 1; dist < len - i; dist++) {
        """

        n = len(s)        
        if n <= 1: return s
        res = None
        dp = [[False for _ in range(n)] for _ in range(n)]        

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j-i < 3 or dp[i+1][j-1])
                if dp[i][j] and (res is None or j-i+1 > len(res)):
                    res = s[i:j+1]
        return res
        

    def longestPalindromeOptimizedN2(self, s):
        if len(s)==0:
            return 0
        maxLen=1
        start=0
        for i in range(len(s)):
            if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
                start=i-maxLen-1
                maxLen+=2
                continue

            if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
                start=i-maxLen
                maxLen+=1
        return s[start:start+maxLen]


            

if __name__ == "__main__":
    #print(Solution().longestPalindrome("babad"))
    #print(Solution().longestPalindromeDP("babad"))

    #print(Solution().longestPalindromeDP("cbbd"))
    s = "wsgdzojcrxtfqcfkhhcuxxnbwtxzkkeunmpdsqfvgfjhusholnwrhmzexhfqppatkexuzdllrbaxygmovqwfvmmbvuuctcwxhrmepxmnxlxdkyzfsqypuroxdczuilbjypnirljxfgpuhhgusflhalorkcvqfknnkqyprxlwmakqszsdqnfovptsgbppvejvukbxaybccxzeqcjhmnexlaafmycwopxntuisxcitxdbarsicvwrvjmxsapmhbbnuivzhkgcrshokkioagwidhmfzjwwywastecjsolxmhfnmgommkoimiwlgwxxdsxhuwwjhpxxgmeuzhdzmuqhmhnfwwokgvwsznfcoxbferdonrexzanpymxtfojodcfydedlxmxeffhwjeegqnagoqlwwdctbqnuxngrgovrjesrkjrfjawknbrsfywljscfvnjhczhyeoyzrtbkvvfvofykkwoiclgxyaddhpdoztdhcbauaagjmfzkkdqexkczfsztckdlujgqzjyuittnudpldjvsbwbzcsazjpxrwfafievenvuetzcxynnmskoytgznvqdlkhaowjtetveahpjguiowkiuvikwewmgxhgfjuzkgrkqhmxxavbriftadtogmhlatczusxkktcsyrnwjbeshifzbykqibghmmvecwwtwdcscikyzyiqlgwzycptlxiwfaigyhrlgtjocvajcnqyenxrnjgogeqtvkxllxpuoxargzgcsfwavwbnktchwjebvwwhfghqkcjhuhuqwcdsixrkfjxuzvhjxlyoxswdlwfytgbtqbeimzzogzrlovcdpseoafuxfmrhdswwictsctawjanvoafvzqanvhaohgndbsxlzuymvfflyswnkvpsvqezekeidadatsymbvgwobdrixisknqpehddjrsntkqpsfxictqbnedjmsveurvrtvpvzbengdijkfcogpcrvwyf"
    print(Solution().longestPalindrome(s))
    print(Solution().longestPalindromeDP(s))
    print(Solution().longestPalindromeOptimizedN2(s))