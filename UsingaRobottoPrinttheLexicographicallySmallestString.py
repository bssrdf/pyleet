'''

-Medium-
*Stack*
*Hash Table*
You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

 

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.

'''
from collections import deque

class Solution:
    def robotWithString(self, s: str) -> str:
        # wrong
        def helper(s):
            n = len(s)
            pos = [[] for _ in range(26)]
            for i,c in enumerate(s):
                pos[ord(c) - ord('a')].append(i)
            ans, minch = [], []
            for i in range(26):
                if pos[i]:
                    pp = pos[i][::-1]
                    j = pp[0]
                    ch = chr(ord('a')+i)
                    minch.append(ch)
                    k, l = j-1, j+1
                    while k >= 0 and l < n:
                        if s[k] == ch:
                            k -= 1
                            minch.append(ch)
                            continue 
                        if s[k] == s[l]:
                            k -= 1
                            l += 1
                            ans.append(s[k])
                            ans.append(s[l])
                        elif s[k] < s[l]:
                            ans.append(s[k])
                            k -= 1
                        else:
                            ans.append(s[l])
                            l += 1
                    if l == n:
                        while k >= 0:
                            if s[k] != ch:
                                ans.append(s[k])
                            else:
                                minch.append(ch)
                            k -= 1
                        return ''.join(minch+ans)
                    if k < 0:
                        return ''.join(minch+ans) + helper(s[l:])
        return helper(s)          
    
    def robotWithString2(self, s: str) -> str:
        # wrong
        n = len(s)
        que = deque()
        for i in range(n):
            while que and s[que[-1]] > s[i]:
                que.pop()
            que.append(i)
        st = set(que)       
        ans = [s[que.popleft()]]
        i = n-1
        while i >= 0 and que:
            if i in st: 
                i -= 1
                continue
            if s[i] < s[que[0]]:
                ans.append(s[i])
                i -= 1
            else:
                j = que.popleft()
                ans.append(s[j])
                # st.remove(j)
        # print(ans)    
        # print(que)    
        while i >= 0:
            if i not in st:
                ans.append(s[i])
            i -= 1
        while que:
            j = que.popleft()
            ans.append(s[j])
        return ''.join(ans)

    def robotWithString3(self, s: str) -> str:
        # treat t as a stack, and anytime starting from top down there is 
        # a char which is smaller than or equal to the smallest in s, robot 
        # can write it to form the lexicographically smallest string        
        cnt = [0]*26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        p, t, lo = [], [], 0
        for c in s:
            t.append(c)
            cnt[ord(c)-ord('a')] -= 1
            # lo is the smallest char in s
            # it could be found by the following code
            # the smallest lo where cnt[lo] > 0
            while lo < 26 and cnt[lo] == 0:
                lo += 1
            print(t, chr(lo+ord('a')))
            while t and ord(t[-1])-ord('a') <= lo:
                p += t[-1]
                t.pop()
        return ''.join(p)


    


if __name__ == "__main__":
    # print(Solution().robotWithString(s = "zza"))      
    # print(Solution().robotWithString(s = "bac"))      
    # print(Solution().robotWithString(s = "bdda"))      

    # print(Solution().robotWithString(s = "bydizfve"))    
    # print(Solution().robotWithString2(s = "zza"))      
    # print(Solution().robotWithString2(s = "bac"))      
    # print(Solution().robotWithString2(s = "bdda"))        
    # print(Solution().robotWithString2(s = "bydizfve"))      
    # print(Solution().robotWithString2(s = "vzhofnpo"))
    print(Solution().robotWithString3(s = "vzhofnpo"))




