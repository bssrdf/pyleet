'''
-Hard-
*DP*
*Bitmask*
Given an array of strings words, return the smallest string that contains each 
string in words as a substring. If there are multiple valid strings of the 
smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.

 

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
 

Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.

'''
import sys

class Solution(object):
    def shortestSuperstringTLE(self, words):
        """
        :type words: List[str]
        :rtype: str
        """        
        n, mn = len(words), [sys.maxsize]
        order, best_order = [0]*n, [0]*n
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
        	for j in range(n):
        		if i == j: continue
        		for k in range(min(len(words[i]), len(words[j])), 0, -1):
        			if words[i][len(words[i]) - k:] == words[j][:k]:
        				overlap[i][j] = k
        				break
        def helper(cur, used, curLen):
            if curLen >= mn[0]: return
            if cur == len(words):
                mn[0] = curLen 
                best_order[:] = order
                return
            for i in range(len(words)):
                if used & (1 << i): continue
                order[cur] = i
                nextLen = len(words[i]) if cur == 0 else curLen + len(words[i]) - overlap[order[cur - 1]][i]
                helper(cur + 1, used | (1 << i), nextLen)
        helper(0, 0, 0)
        res = words[best_order[0]]
        for k in range(1, n):
            i, j = best_order[k - 1], best_order[k]
            res += words[j][overlap[i][j]:]
        return res

    def shortestSuperstring(self, words):
        """
        :type words: List[str]
        :rtype: str
        """        
        n = len(words)
        # dp[mask][j]: shortest superstring ending with words[j] \
        # and including all strings indicated by on bits in mask    
        dp = [['']*n for _ in range(1<<n)]
        # overlap[i][j]: index where common substring b.w. words[i] and words[j] starts 
        overlap = [[0]*n for _ in range(n)]
        for i in range(n):
        	for j in range(n):
        		if i == j: continue
        		for k in range(min(len(words[i]), len(words[j])), 0, -1):
        			if words[i][len(words[i]) - k:] == words[j][:k]:
        				overlap[i][j] = k
        				break
        for i in range(n): dp[1 << i][i] += words[i]
        for p in dp:
           print(p)
        for mask in range(1, 1 << n): # try each permutation of all strings
                                      # update values of dp[mask][j]
        	for j in range(n):
        		if (mask & (1 << j)) == 0: continue # words[j] not included, skip
        		for i in range(n):
        			if i == j or mask & (1 << i) == 0: continue # same word or words[i] not included, skip
                    # all other combinations not including words[j] (as enforced 
                    # by mask ^ 1<<j) and ending with words[i] plus words[j] is a candidate superstring
        			t = dp[mask ^ (1 << j)][i] + words[j][overlap[i][j]:]
        			if not dp[mask][j] or len(t) < len(dp[mask][j]):
        				dp[mask][j] = t
        #for p in dp:
         #  print(p)
        last = (1 << n) - 1 # this is the only mask where all words are included 
        res = dp[last][0]
        for i in range(1, n): # check all superstrings for this mask
        	if len(dp[last][i]) < len(res):
        		res = dp[last][i] # pick the shortest
        return res
    
        
   

if __name__ == "__main__":
    print(Solution().shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"]))
    #print(Solution().shortestSuperstring(["nbsgonqmpreelpbr","hnysjajtiguehrokus","udgzbzmevnkzzba","axtbmcpbmoubyoscn","vqnbsgonqmpreel","xvqnbsgonqmpree","ajtiguehrokustktudgz","brgkgihuetpqrhhbhn","dgzbzmevnkzzbaxtbmcp","ehrokustktudgzbzmevn","uetpqrhhbhnysjaj","vnkzzbaxtbmcpbmo"]))