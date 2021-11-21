'''

-Medium-
*Sorting*
*Monotonic Stack*

You are playing a game that contains multiple characters, and each of the characters 
has two main properties: attack and defense. You are given a 2D integer array properties 
where properties[i] = [attacki, defensei] represents the properties of the ith 
character in the game.

A character is said to be weak if any other character has both attack and defense 
levels strictly greater than this character's attack and defense levels. More formally, 
a character i is said to be weak if there exists another character j where attackj > attacki 
and defensej > defensei.

Return the number of weak characters.

 

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
 

Constraints:

2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5

'''

from typing import List

from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        P = properties
        n, ans, max_y = len(P), 0, -1
        groups = defaultdict(list)
        for a,d in P:
            groups[a].append(d)
        for t in sorted(list(groups.keys()))[::-1]:
            for q in groups[t]:
                if q < max_y: ans += 1
            for q in groups[t]:
                max_y = max(max_y, q)
        return ans

    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        P = properties
        P.sort(key=lambda x: (x[0], -x[1]))
        n, ans, max_ = len(P), 0, -1
        print(P)
        for a, d in P[::-1]:
            if d < max_:
                ans += 1
            max_ = max(max_, d)
        return ans
    
    def numberOfWeakCharacters3(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))        
        stack = []
        ans = 0        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                ans += 1
            stack.append(d)
        return ans
        


if __name__ == "__main__":
    print(Solution().numberOfWeakCharacters([[5,5],[6,3],[3,6]]))        
    print(Solution().numberOfWeakCharacters([[2,2],[3,3]]))        
    print(Solution().numberOfWeakCharacters([[1,5],[10,4],[4,3]]))        
    print(Solution().numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]]))        
    print(Solution().numberOfWeakCharacters2([[5,5],[6,3],[3,6]]))        
    print(Solution().numberOfWeakCharacters2([[2,2],[3,3]]))        
    print(Solution().numberOfWeakCharacters2([[1,5],[10,4],[4,3]]))        
    print(Solution().numberOfWeakCharacters2([[1,1],[2,1],[2,2],[1,2]]))        