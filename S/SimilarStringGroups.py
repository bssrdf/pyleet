'''
-Hard-

*Union Find*

Two strings X and Y are similar if we can swap two letters (in different positions) of X, 
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" 
and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and 
{"star"}.  Notice that "tars" and "arts" are in the same group even though they are not 
similar.  Formally, each group is such that a word is in the group if and only if it is 
similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every 
other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.


'''

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        roots = [i for i in range(n)]        
        self.ans = n
        def find(i):        
            while roots[i] != i:            
               roots[i] = roots[roots[i]] 
               i = roots[i]
            return i
        def union(i, j):
            x, y = find(j), find(i)
            if x != y: 
                roots[x] = y 
                self.ans -= 1
        def similar(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: 
                    cnt += 1
                    if cnt > 2: return False
            return True
        for i in range(n):
            for j in range(i + 1, n):
                if strs[i] == strs[j] or similar(strs[i], strs[j]):
                    union(i, j)
        return self.ans
                    



if __name__ == "__main__":
    print(Solution().numSimilarGroups(["tars","rats","arts","star"]))
    print(Solution().numSimilarGroups(["omv", "ovm"]))