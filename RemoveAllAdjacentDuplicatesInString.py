'''
-Easy-

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and 
equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the 
answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is 
the only possible move.  The result of this move is that the string is "aaca", of which only "aa" 
is possible, so the final string is "ca".
 

Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.

'''

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S: return ''
        t = []
        i = 0
        dup = False
        while i < len(S)-1:
            if S[i] == S[i+1]:
                i = i+2
                dup = True
            else:
                t.append(S[i])
                i += 1
        if i < len(S):
            t.append(S[i])
        if dup:
            return self.removeDuplicates(''.join(t))
        return S

    def removeDuplicatesStack(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)

    def removeDuplicates2Pointers(self, S):
        res = list(S)
        i = 0
        for j in range(len(S)):
            res[i] = res[j]
            if i > 0 and res[i-1] == res[i]:
                i -= 2
            i += 1
            print(j,i)
        return "".join(res[:i])

if __name__ == "__main__":
    #print(Solution().removeDuplicates("abbaca"))
    print(Solution().removeDuplicates2Pointers("abbaca"))