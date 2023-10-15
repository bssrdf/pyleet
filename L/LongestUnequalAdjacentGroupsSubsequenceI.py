'''

-Medium-

*DP*

You are given an integer n, a 0-indexed string array words, and a 0-indexed binary array groups, both arrays having length n.

You need to select the longest subsequence from an array of indices [0, 1, ..., n - 1], such that for the subsequence denoted as [i0, i1, ..., ik - 1] having length k, groups[ij] != groups[ij + 1], for each j where 0 < j + 1 < k.

Return a string array containing the words corresponding to the indices (in order) in the selected subsequence. If there are multiple answers, return any of them.

A subsequence of an array is a new array that is formed from the original array by deleting some (possibly none) of the elements without disturbing the relative positions of the remaining elements.

Note: strings in words may be unequal in length.

 

Example 1:

Input: n = 3, words = ["e","a","b"], groups = [0,0,1]
Output: ["e","b"]
Explanation: A subsequence that can be selected is [0,2] because groups[0] != groups[2].
So, a valid answer is [words[0],words[2]] = ["e","b"].
Another subsequence that can be selected is [1,2] because groups[1] != groups[2].
This results in [words[1],words[2]] = ["a","b"].
It is also a valid answer.
It can be shown that the length of the longest subsequence of indices that satisfies the condition is 2.
Example 2:

Input: n = 4, words = ["a","b","c","d"], groups = [1,0,1,1]
Output: ["a","b","c"]
Explanation: A subsequence that can be selected is [0,1,2] because groups[0] != groups[1] and groups[1] != groups[2].
So, a valid answer is [words[0],words[1],words[2]] = ["a","b","c"].
Another subsequence that can be selected is [0,1,3] because groups[0] != groups[1] and groups[1] != groups[3].
This results in [words[0],words[1],words[3]] = ["a","b","d"].
It is also a valid answer.
It can be shown that the length of the longest subsequence of indices that satisfies the condition is 3.
 

Constraints:

1 <= n == words.length == groups.length <= 100
1 <= words[i].length <= 10
0 <= groups[i] < 2
words consists of distinct strings.
words[i] consists of lowercase English letters.


'''
from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        G = groups
        arr = [[] for _ in range(n)]
        maxl = [] 
        for i in range(n):
            l, cand = 0, arr[i]
            for j in range(i):
                if G[i] != G[j]:
                    if l < len(arr[j]):
                    #    print(j, i, l, arr[j])
                       l = len(arr[j])
                       cand = arr[j] 
            arr[i] = cand[:] + [i]
            # print(i, cand, arr)
            if len(maxl) < len(arr[i]):
                maxl = arr[i]
        # print(maxl)
        return [words[i] for i in maxl]      
    
if __name__ == "__main__":
    print(Solution().getWordsInLongestSubsequence(n = 4, words = ["a","b","c","d"], groups = [1,0,1,1]))