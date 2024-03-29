'''
-Medium-
*Two Pointers*

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length



'''
import bisect

from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0: return 0
        cnt = Counter(s)
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        left = [[0]*n for _ in range(3)]
        right = [[0]*n for _ in range(3)]
        idx = ord(s[0]) - ord('a')
        left[idx][0] = 1
        for i in range(1, n):
            for idx in range(3):
                if ord(s[i])-ord('a') == idx:
                    left[idx][i] = left[idx][i-1] + 1
                else:
                    left[idx][i] = left[idx][i-1] 
        idx = ord(s[-1]) - ord('a')
        right[idx][-1] = 1
        for i in range(n-2, -1, -1):
            for idx in range(3):
                if ord(s[i])-ord('a') == idx:
                    right[idx][i] = right[idx][i+1] + 1
                else:
                    right[idx][i] = right[idx][i+1] 
        # for l in left:
        #     print(l)
        # for l in right:
        #     print(l)   
        ans = len(s) + 1 
        for i in range(n, -1, -1):
            idx = [-1]*3
            for j in range(3):
                if i == n: 
                    idx[j] = bisect.bisect_left(left[j], k)
                elif k-right[j][i] > 0: 
                    idx[j] = bisect.bisect_left(left[j], k-right[j][i])
            # print(i, idx)
            ans = min(ans, max(idx)+ 1 + n-i)
        return ans
    

    def takeCharacters2(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0: return 0
        cnt = Counter(s)
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        left = [[0]*n for _ in range(3)]
        idx = ord(s[0]) - ord('a')
        left[idx][0] = 1
        for i in range(1, n):
            for idx in range(3):
                if ord(s[i])-ord('a') == idx:
                    left[idx][i] = left[idx][i-1] + 1
                else:
                    left[idx][i] = left[idx][i-1] 
        # for l  left:
            # print(l)
        ans = len(s) + 1 
        right = [0]*3
        for i in range(n, -1, -1):
            idx = [-1]*3            
            if i < n:
               for j in range(3): 
                    right[j] += 1 if ord(s[i])-ord('a') == j else 0 
            print(i, right)
            for j in range(3):
                if i == n or k-right[j] > 0: 
                    idx[j] = bisect.bisect_left(left[j], k-right[j])
            # print(i, idx)
            ans = min(ans, max(idx)+ 1 + n-i)
        return ans

    def takeCharacters3(self, s: str, k: int) -> int:
        n = len(s)
        if k == 0: return 0
        flag = False
        cnt = [0]*3
        l, r  = 0, n
        while l < n:
            for j in range(3):
                cnt[j] += 1 if ord(s[l])-ord('a') == j else 0 
            if all([x >= k for x in cnt]):
                flag = True
                break
            l += 1
        if not flag: return -1
        ret = l + 1
        while l >= 0:
            for j in range(3):
                cnt[j] -= 1 if ord(s[l])-ord('a') == j else 0 
            l -= 1
            while l < r and any([x < k for x in cnt]):
                r -= 1
                for j in range(3):
                    cnt[j] += 1 if ord(s[r])-ord('a') == j else 0 
            if all([x >= k for x in cnt]):
                ret = min(ret, l+1+n-r)
        return ret     







    


if __name__ == "__main__":
    # print(Solution().takeCharacters(s = "aabaaaacaabc", k = 2))
    # print(Solution().takeCharacters(s = "acba", k = 1))
    print(Solution().takeCharacters(s = "ccbabcc", k = 1))
    print(Solution().takeCharacters2(s = "ccbabcc", k = 1))

    print(Solution().takeCharacters(s = "aabaaaacaabc", k = 2))
    print(Solution().takeCharacters2(s = "aabaaaacaabc", k = 2))