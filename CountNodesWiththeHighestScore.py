'''
-Medium-

There is a binary tree rooted at 0 consisting of n nodes. The nodes are 
labeled from 0 to n - 1. You are given a 0-indexed integer array parents 
representing the tree, where parents[i] is the parent of node i. Since 
node 0 is the root, parents[0] == -1.

Each node has a score. To find the score of a node, consider if the 
node and the edges connected to it were removed. The tree would become 
one or more non-empty subtrees. The size of a subtree is the number of 
the nodes in it. The score of the node is the product of the sizes of 
all those subtrees.

Return the number of nodes that have the highest score.

 

Example 1:

example-1
Input: parents = [-1,2,0,2,0]
Output: 3
Explanation:
- The score of node 0 is: 3 * 1 = 3
- The score of node 1 is: 4 = 4
- The score of node 2 is: 1 * 1 * 2 = 2
- The score of node 3 is: 4 = 4
- The score of node 4 is: 4 = 4
The highest score is 4, and three nodes (node 1, node 3, and node 4) have the highest score.
Example 2:

example-2
Input: parents = [-1,2,0]
Output: 2
Explanation:
- The score of node 0 is: 2 = 2
- The score of node 1 is: 2 = 2
- The score of node 2 is: 1 * 1 = 1
The highest score is 2, and two nodes (node 0 and node 1) have the highest score.
 

Constraints:

n == parents.length
2 <= n <= 105
parents[0] == -1
0 <= parents[i] <= n - 1 for i != 0
parents represents a valid binary tree.


'''

from typing import List
from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        subnodes = [[0,0] for _ in range(n)]
        tree = defaultdict(list)
        scores = defaultdict(int)
        for i,p in enumerate(parents[1:], start=1):
            tree[p].append(i)
        def dfs(root):
            if len(tree[root]) == 0: return 1
            for i, child in enumerate(tree[root]):
                subnodes[root][i] = dfs(child)
            return sum(subnodes[root]) + 1
        dfs(0)
        max_score = 0
        for i in range(n):
            nums = [subnodes[i][0], subnodes[i][1], n-sum(subnodes[i])-1]
            score = 1
            for c in nums:
                if c > 0 : score *= c
            scores[score] += 1
            max_score = max(max_score, score)
        return scores[max_score]
        

    def countHighestScoreNodes2(self, parents: List[int]) -> int:
        n = len(parents)
        tree = defaultdict(list)
        scores = defaultdict(int)
        max_score = [0]
        for i,p in enumerate(parents[1:], start=1):
            tree[p].append(i)
        def dfs(root):
            if len(tree[root]) == 0: 
                scores[n-1] += 1
                max_score[0] = max(max_score[0], n-1)
                return 1
            score, subs = 1, 0
            for i, child in enumerate(tree[root]):
                c = dfs(child)
                subs += c
                if c > 0: score *= c
            c = n-subs-1
            if c > 0: score *= c
            scores[score] += 1
            max_score[0] = max(max_score[0], score)
            return subs + 1
        dfs(0)
        return scores[max_score[0]]
            



        
if __name__ == "__main__":
    #print(Solution().countHighestScoreNodes([-1,2,0,2,0]))
    #print(Solution().countHighestScoreNodes([-1,2,0]))
    print(Solution().countHighestScoreNodes2([-1,2,0,2,0]))
    print(Solution().countHighestScoreNodes2([-1,2,0]))

