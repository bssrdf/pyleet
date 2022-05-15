'''
-Hard-

The variance of a string is defined as the largest difference between the number of 
occurrences of any 2 characters present in the string. Note the two characters may 
or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest 
variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aababbb"
Output: 3
Explanation:
All possible variances along with their respective substrings are listed below:
- Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
- Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
- Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
- Variance 3 for substring "babbb".
Since the largest possible variance is 3, we return it.
Example 2:

Input: s = "abcde"
Output: 0
Explanation:
No letter occurs more than once in s, so the variance of every substring is 0.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


'''
from enum import unique
import string

class Solution:
    def largestVariance(self, s: str) -> int:
        freq, ans = [0]*26, 0
        for c in s:
            freq[ord(c)-ord('a')] += 1
        unique = set(s)
        # for ch1 in string.ascii_lowercase:
        #     for ch2 in string.ascii_lowercase:
        for ch1 in unique:
            for ch2 in unique:
                if ch1 == ch2 or freq[ord(ch1)-ord('a')] == 0 or freq[ord(ch2)-ord('a')] == 0:
                    continue
                for rev in range(1,3):
                    cnt1, cnt2 = 0, 0
                    for c in s:
                        cnt1 += c == ch1
                        cnt2 += c == ch2
                        if cnt1 < cnt2:
                            cnt1 = cnt2 = 0
                        if cnt1 > 0 and  cnt2 > 0:
                            ans = max(ans, cnt1-cnt2)
                    s = s[::-1]
        return ans
    
    def largestVariance2(self, s: str) -> int:
        def maxSubArray(nums):
            ans=-float('inf')
            runningSum=0
            seen=False
            for x in (nums):
                if x<0:
                    seen=True
                runningSum+=x
                if seen:
                    ans=max(ans,runningSum)
                else:
                    ans=max(ans,runningSum-1)
                if runningSum<0:
                    runningSum=0
                    seen=False
            return ans
        
        f=set()
        a=''
        for x in s:
            if x not in f:
                a+=x
                f.add(x)
       
        n=len(s)
        res=0
        for j in range(len(a)-1):
            for k in range(j+1,len(a)):
                x=a[j]
                y=a[k]
                arr=[]
                for i in range(n):
                    if s[i]!=x and s[i]!=y:
                        continue
                    elif s[i]==x:
                        arr.append(1)
                    else:
                        arr.append(-1)
                
                res=max(res,maxSubArray(arr),maxSubArray([-x for x in arr]))
                
        return res
    
    def largestVariance3(self, s: str) -> int:
        res = 0
        for p in string.ascii_lowercase:
            for q in string.ascii_lowercase:
                if p == q: continue
                
                # run Kadane's algo
                pCount = 0 # higher one
                qCount = 0 # lower one
                
                # this flag would deal with the edge case
                # e.g., "pqqpppppp"
                # after reset, there is no q but we can extend
                # the interval to the previous q
                # and the answer should -1
                canExtendprevQ = False
                
                for c in s:
                    if c == p: pCount += 1
                    if c == q: qCount += 1
                    
                    # an interval should contain at least one q
                    if qCount > 0:
                        res = max(res, pCount - qCount)
                    # edge case: consider previous q
                    elif qCount == 0 and canExtendprevQ:
                        res = max(res, pCount - qCount - 1)
                    
                    # reset if # of q > # of p
                    if qCount > pCount:
                        qCount = pCount = 0
                        
                        # once reset, the interval can be extended
                        # as there must be one q before the next interval
                        canExtendprevQ = True
        return res







if __name__ == "__main__":
    print(Solution().largestVariance(s = "aababbb"))        