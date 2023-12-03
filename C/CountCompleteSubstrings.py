'''

-Medium-

*Sliding Window*
*Deque*
*Sliding Window Maximum*

You are given a string word and an integer k.

A substring s of word is complete if:

Each character in s occurs exactly k times.
The difference between two adjacent characters is at most 2. That is, for any two adjacent characters c1 and c2 in s, the absolute difference in their positions in the alphabet is at most 2.
Return the number of complete substrings of word.

A substring is a non-empty contiguous sequence of characters in a string.

 

Example 1:

Input: word = "igigee", k = 2
Output: 3
Explanation: The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: igigee, igigee, igigee.
Example 2:

Input: word = "aaabbbccc", k = 3
Output: 6
Explanation: The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc, aaabbbccc.
 

Constraints:

1 <= word.length <= 105
word consists only of lowercase English letters.
1 <= k <= word.length

'''

from collections import Counter, deque
import heapq


class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        # mp = Counter()
        mp= [Counter() for _ in range(26)]
        for i in range(26):
            mp[i][(0,)*5] = 1
        cnt = [0]*26
        ans = 0
        for c in word:
            j = ord(c)-ord('a')
            cnt[j] += 1
            l = []
            for i in range(-2,3):
                if j+i >= 0 and j+i < 26:
                    l.append(cnt[j+i]%k)
                else:
                    l.append(0)    
            print(c, tuple(l), mp[j])
            # print(mp)    
            
            ans0 = ans
            ans += mp[j][tuple(l)]
            print(ans0, ans, mp[j][tuple(l)])

            for i in range(-2,3):
                ii = j+i
                if ii >= 0 and ii < 26:
                    l = []
                    for kk in range(-2,3):
                        if ii+kk >= 0 and ii+kk < 26:
                            l.append(cnt[ii+kk]%k)
                        else:
                            l.append(0) 
                        
                    mp[ii][tuple(l)] = 1
            # print(c, ans, mp)
        return ans                

    def countCompleteSubstrings2(self, word: str, k: int) -> int:
        n = len(word)
        def count(l):
            ret = 0
            cnt = [0]*26
            pq = []
            mp = [None for _ in range(n)]
            st = set()
            for j in range(n):
                c = ord(word[j])-ord('a')
                cnt[c] += 1
                if c in st and cnt[c] == k:
                    st.remove(c)
                elif cnt[c] != k:
                    st.add(c)
                # print(j, l, cnt, st)        
                if j > 0:
                    mp[j-1] = [-abs(ord(word[j]) - ord(word[j-1])), False]
                    heapq.heappush(pq, mp[j-1])
                if j >= l:
                    c = ord(word[j-l])-ord('a')
                    cnt[c] -= 1
                    if c in st and (cnt[c] == 0 or cnt[c] == k):
                        st.remove(c)
                    elif cnt[c] != 0 and cnt[c] != k:
                        st.add(c)
                    mp[j-l][1] = True  
                if j >= l-1:
                    while pq and pq[0][1]:
                        heapq.heappop(pq) 
                    if (not st) and ((not pq) or (pq and (-pq[0][0]) <= 2)): ret += 1
                    # if l == 1:
                    #     print(j, st, ret, cnt)
                
                # if l == 2:
                #     print(j, word[j], ret, pq, cnt)    
            # print(l, ret)
            return ret

        return sum(count(i*k) for i in range(1,27))    


    def countCompleteSubstrings3(self, word: str, k: int) -> int:
        n = len(word)
        m = len(Counter(word))
        def count(l):
            ret = 0
            cnt = [0]*26
            stk = deque()
            st = set()
            for j in range(n):
                c = ord(word[j])-ord('a')
                cnt[c] += 1
                if c in st and cnt[c] == k:
                    st.remove(c)
                elif cnt[c] != k:
                    st.add(c)
                if j > 0:      
                    t = abs(ord(word[j]) - ord(word[j-1]))
                    while stk and stk[-1][0] <= t:
                        stk.pop()
                    stk.append((t, j-1))    
                if j >= l:
                    c = ord(word[j-l])-ord('a')
                    cnt[c] -= 1
                    if c in st and (cnt[c] == 0 or cnt[c] == k):
                        st.remove(c)
                    elif cnt[c] != 0 and cnt[c] != k:
                        st.add(c)
                    if stk[0][1] == j-l:
                        stk.popleft() 
                if j >= l-1:
                    if (not st) and ((not stk) or (stk and stk[0][0] <= 2)): 
                        ret += 1
            return ret

        return sum(count(i*k) for i in range(1,m+1))    



if __name__ == "__main__":
    # print(Solution().countCompleteSubstrings2(word = "igigee", k = 2))
    # print(Solution().countCompleteSubstrings2(word = "aaabbbccc", k = 3))
    # print(Solution().countCompleteSubstrings2(word = "aaabbbzzz", k = 3))
    # print(Solution().countCompleteSubstrings2(word = "aaa", k = 1))
    # print(Solution().countCompleteSubstrings2(word = "acca", k = 1))
    # word = "jvm"*16690
    # # print('l = ', len(word))
    # print(Solution().countCompleteSubstrings2(word = word, k = 9710))

    # print(Solution().countCompleteSubstrings2(word = "ppjuukkukkpkpppujujupukkjjujuukkupjkjjppkju", k = 8))
    print(Solution().countCompleteSubstrings3(word = "ppjuukkukkpkpppujujupukkjjujuukkupjkjjppkju", k = 8))

    print(Solution().countCompleteSubstrings3(word = "igigee", k = 2))
    print(Solution().countCompleteSubstrings3(word = "aaabbbccc", k = 3))
    print(Solution().countCompleteSubstrings3(word = "aaabbbzzz", k = 3))
    print(Solution().countCompleteSubstrings3(word = "aaa", k = 1))
    print(Solution().countCompleteSubstrings3(word = "acca", k = 1))
    word = "jvm"*16690
    # print('l = ', len(word))
    print(Solution().countCompleteSubstrings3(word = word, k = 9710))