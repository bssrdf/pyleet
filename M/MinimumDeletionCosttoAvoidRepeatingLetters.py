'''
-Medium-

Given a string s and an array of integers cost where cost[i] is the cost of 
deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical 
letters next to each other.

Notice that you will delete the chosen characters at the same time, in other 
words, after deleting a character, the costs of deleting other characters 
will not change.

 

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).
Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.
Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
 

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.

'''

from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n = len(s)
        sm, mx, c = 0, 0, '_'
        ans = 0
        for i in range(n):
            if s[i] == c:
                sm += cost[i]
                mx = max(mx, cost[i])
            else:
                ans += sm - mx
                c = s[i]
                sm, mx = cost[i], cost[i]
        ans += sm - mx
        return ans

if __name__ == "__main__":
    print(Solution().minCost(s = "abaac", cost = [1,2,3,4,5]))
    print(Solution().minCost(s = "abc", cost = [1,2,3]))
    print(Solution().minCost(s = "aabaa", cost = [1,2,3,4,1]))