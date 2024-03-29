'''

-Hard-

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].

You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:

The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert "abcd" to "acbe", do the following operations:
- Change substring source[1..1] from "b" to "c" at a cost of 5.
- Change substring source[2..2] from "c" to "e" at a cost of 1.
- Change substring source[2..2] from "e" to "b" at a cost of 2.
- Change substring source[3..3] from "d" to "e" at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
Output: 9
Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
- Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
- Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
- Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
The total cost incurred is 1 + 3 + 5 = 9.
It can be shown that this is the minimum possible cost.
Example 3:

Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
Output: -1
Explanation: It is impossible to convert "abcdefgh" to "addddddd".
If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
 

Constraints:

1 <= source.length == target.length <= 1000
source, target consist only of lowercase English characters.
1 <= cost.length == original.length == changed.length <= 100
1 <= original[i].length == changed[i].length <= source.length
original[i], changed[i] consist only of lowercase English characters.
original[i] != changed[i]
1 <= cost[i] <= 106


'''

from typing import List
from collections import defaultdict
from math import inf
class Node(defaultdict):
    def __init__(self):
        super().__init__(Node)
        self.idx = -1

class Trie(object):

    def __init__(self):        
        self.root = Node()        

    def add_word(self, word, i):
        node = self.root
        for j in range(len(word)-1, -1, -1):
            node = node[word[j]]
        node.idx = i

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        dist = defaultdict(lambda: inf)
        v_to_idx = defaultdict(int)
        N, M = len(source), len(original)
        trie = Trie()

        # Construct trie and graph
        for i in range(M):
            oi, ci = original[i], changed[i]            
            # Map substr to idx and add (s, idx of s) to trie
            if oi not in v_to_idx:
                v_to_idx[oi] = len(v_to_idx)
                trie.add_word(oi, v_to_idx[oi])

            if ci not in v_to_idx:
                v_to_idx[ci] = len(v_to_idx)
                trie.add_word(ci, v_to_idx[ci])

            u, v = v_to_idx[oi], v_to_idx[ci]
            # Dup edges, take the min cost
            dist[(u, v)] = min(dist[(u, v)], cost[i])
        
        V = len(v_to_idx)
        for k in range(V):
            for i in range(V):
                for j in range(V):
                    dist[(i,j)] = min(dist[(i,j)], dist[(i,k)] + dist[(k,j)])
        dp = [inf]*N 
        for i in range(N):
            s, t = trie.root, trie.root 
            for j in range(i, -1, -1):
                if source[j] not in s or target[j] not in t:
                    break
                s, t = s[source[j]], t[target[j]]
                if s.idx != -1 and t.idx != -1:
                    u, v = s.idx, t.idx
                    dp[i] = min(dp[i], (dp[j-1] if j-1 >= 0 else 0) + dist[(u,v)])
            if source[i] == target[i]:
                dp[i] = min(dp[i], dp[i-1] if i-1 >= 0 else 0)
        return dp[-1] if dp[-1] != inf else -1
     
if __name__ == "__main__":
    print(Solution().minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))
    source = "cdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqv"
    target = "tpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcf"
    original = ["cdnitv","mwqvcdn","itvmwqvcdn","it","vmwqvcdn","itv","mw","qvcdni","tv","mwqvcdn","itvmwqvcdn","itvmwqv","cdnitvmwqv","cdnit","vmw","qvcdnitvm","wqvcdn","it","vmwqvc","dnitvmwqv","cdnitvmwq","vcdn","itvmwq","vcd","nitvmw","qvcd","ni","tvmwqvcdni","tv","mwqvcd","nitvmw","qvcd","nitvmwqvc","dnitvmwq","vcdnitvm","wqvcdni","tvmwqv","cdni","tvmw","qv","cdnit","vmwqvcd","nitvmwqvcd","nitvmw","qvcdn","itv","mwqvcdnit","vmwqvcdn","itvmwqvcdn","itv","mwq","vcdnitvm","wqvcdni","tvm","wqvcdn","it","vmw","qvcdni","tvmwq","vcdnit","vmw","qvcdnitvm","wqvcdnitvm","wqvcdn","itvmw","qvc","dnitvm","wq","vcdni","tvmwqvcd","nitvmw","qvcdnitvm","wqvc","dnit","vmw","qvcd","ni","tvmwqvcd","ni","tvmwqv","cdni","tvmwqvcd","nitvmwqvc","dni","tvmwqvc","dnitvm","wqvcdnit","vmw","qvcdnitvm","wqvcdn","itvmwqvcdn","itvmwqvcdn","itvmwqv","cdnitvmwqv","cdnit","vmwqvc","dnitvmwqvc","dnitvmwqvc","dnit","cdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqvcdnitvmwqv"]
    changed = ["tpelbg","wfcftpe","lbgwfcftpe","lb","gwfcftpe","lbg","wf","cftpel","bg","wfcftpe","lbgwfcftpe","lbgwfcf","tpelbgwfcf","tpelb","gwf","cftpelbgw","fcftpe","lb","gwfcft","pelbgwfcf","tpelbgwfc","ftpe","lbgwfc","ftp","elbgwf","cftp","el","bgwfcftpel","bg","wfcftp","elbgwf","cftp","elbgwfcft","pelbgwfc","ftpelbgw","fcftpel","bgwfcf","tpel","bgwf","cf","tpelb","gwfcftp","elbgwfcftp","elbgwf","cftpe","lbg","wfcftpelb","gwfcftpe","lbgwfcftpe","lbg","wfc","ftpelbgw","fcftpel","bgw","fcftpe","lb","gwf","cftpel","bgwfc","ftpelb","gwf","cftpelbgw","fcftpelbgw","fcftpe","lbgwf","cft","pelbgw","fc","ftpel","bgwfcftp","elbgwf","cftpelbgw","fcft","pelb","gwf","cftp","el","bgwfcftp","el","bgwfcf","tpel","bgwfcftp","elbgwfcft","pel","bgwfcft","pelbgw","fcftpelb","gwf","cftpelbgw","fcftpe","lbgwfcftpe","lbgwfcftpe","lbgwfcf","tpelbgwfcf","tpelb","gwfcft","pelbgwfcft","pelbgwfcft","pelb","tpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcftpelbgwfcf"]
    cost = [776,96,624,817,25,165,542,339,515,88,162,925,528,446,789,428,33,882,80,853,776,866,659,385,860,21,167,901,314,522,831,993,638,704,982,800,356,767,858,768,598,127,366,460,954,909,874,828,203,879,26,766,391,280,330,985,558,50,673,327,579,766,803,307,860,176,895,722,87,877,411,911,776,983,103,643,582,239,977,861,750,218,91,233,571,149,79,319,80,663,399,710,725,174,964,988,819,207,285,61510]
    print(Solution().minimumCost(source = source, target = target, original = original, changed = changed, cost = cost))
