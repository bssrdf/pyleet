'''
-Medium-

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

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
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
        for l in left:
            print(l)
        for l in right:
            print(l)   
        return 0
    

    def takeCharacters2(self, s: str, k: int) -> int:
        s2 = s + s
        n = len(s)
        j, i = 0, 0
        cnt = [0]*3
        ans = len(s)+1
        def check():
            return all([x >= k for x in cnt]) 
        while i < n:
            cnt[ord(s2[i])-ord('a')] += 1
            i += 1
            while check():  
                ans = min(ans, i-j)
                cnt[ord(s[j])-ord('a')] -= 1
                j += 1            
        return -1 if ans == len(s) + 1 else ans    








if __name__ == "__main__":
    print(Solution().takeCharacters2(s = "aabaaaacaabc", k = 2))