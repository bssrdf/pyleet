'''
-Medium-

*Two Pointers*
*Binary Search*

You are given a 2D integer array tiles where tiles[i] = [li, ri] represents that every tile j in the range li <= j <= ri is colored white.

You are also given an integer carpetLen, the length of a single carpet that can be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.

 

Example 1:


Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
Output: 9
Explanation: Place the carpet starting on tile 10. 
It covers 9 white tiles, so we return 9.
Note that there may be other places where the carpet covers 9 white tiles.
It can be shown that the carpet cannot cover more than 9 white tiles.
Example 2:


Input: tiles = [[10,11],[1,1]], carpetLen = 2
Output: 2
Explanation: Place the carpet starting on tile 10. 
It covers 2 white tiles, so we return 2.
 

Constraints:

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
The tiles are non-overlapping.




'''
from operator import itemgetter
from typing import List
import bisect
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        T, n = tiles, len(tiles)
        tiles.sort()
        preSum = [0]*(n+1)
        arr = []
        for i in range(n):
            preSum[i+1] = preSum[i] + T[i][1]-T[i][0]+1
            arr.append((T[i][0],i))
            arr.append((T[i][1],i))
        ans = 0
        # print(preSum)
        # print(arr)

        for i in range(n):
            l = T[i][0] + carpetLen
            
            # idx = bisect.bisect_left(arr, (l, 0))            
            idx = bisect.bisect_left(arr, l, key=itemgetter(0))            

            if idx <len(arr) and arr[idx-1][1] == arr[idx][1]:
                sums =  preSum[arr[idx-1][1]] - preSum[i]          
                sums += l - arr[idx-1][0]
            else:
                sums =  preSum[arr[idx-1][1]+1] - preSum[i]
            ans = max(ans, sums)
            # print(ans, idx, sums)

        return ans     

    def maximumWhiteTiles2(self, tiles: List[List[int]], carpetLen: int) -> int:
        T, n = tiles, len(tiles)
        tiles.sort()
        preSum = [0]*(n+1)
        ans =  0
        for i in range(n):
            preSum[i+1] = preSum[i] + T[i][1]-T[i][0]+1
        j = 0
        for i in range(n):
            k = tiles[i][0]+carpetLen-1
            while j < n and k >= tiles[j][1]:
                j += 1
            l = preSum[j] - (0 if i==0 else preSum[i])
            if j < n:
                l += max(0, k - tiles[j][0]+1)
            ans = max(ans, l)            
        return ans






if __name__ == "__main__":
    print(Solution().maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))     
    print(Solution().maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2))     
    print(Solution().maximumWhiteTiles2(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))     
    print(Solution().maximumWhiteTiles2(tiles = [[10,11],[1,1]], carpetLen = 2))     

        