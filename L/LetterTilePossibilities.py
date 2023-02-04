'''
-Medium-


You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can 
make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.



'''
from typing import List
from collections import Counter 

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        def backtrack(cnt):
            sm = 0
            cntc = dict(cnt)
            for c in cnt:
                if cnt[c] == 0: continue
                sm += 1
                cntc[c] -= 1
                sm += backtrack(cntc)    
                cntc[c] += 1   
            return sm
       
        return backtrack(counter)
    
    def numTilePossibilities2(self, tiles: str) -> List[str]:
        counter = Counter(tiles)
        visited = set()
        def backtrack(cur, cnt, allstrs):
            cntc = dict(cnt)            
            for c in cnt:
                if cnt[c] == 0: continue
                cur += c
                allstrs.add(cur)
                cntc[c] -= 1
                backtrack(cur, cntc, allstrs)    
                cntc[c] += 1   
                cur = cur[:-1]
       
        backtrack('', counter, visited)
        print(len(visited))
        return list(visited)


if __name__ == "__main__":
    print(Solution().numTilePossibilities('AAB'))        
    print(Solution().numTilePossibilities2('AAB'))        
    print(Solution().numTilePossibilities('AABCC'))        
    print(Solution().numTilePossibilities2('AABCC'))        