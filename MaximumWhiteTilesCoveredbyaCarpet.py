
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
            
            idx = bisect.bisect_left(arr, (l, 0))            

            if idx <len(arr) and arr[idx-1][1] == arr[idx][1]:
                sums =  preSum[arr[idx-1][1]] - preSum[i]          
                sums += l - arr[idx-1][0]
            else:
                sums =  preSum[arr[idx-1][1]+1] - preSum[i]
            ans = max(ans, sums)
            # print(ans, idx, sums)

        return ans     




if __name__ == "__main__":
    print(Solution().maximumWhiteTiles(tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10))     
    print(Solution().maximumWhiteTiles(tiles = [[10,11],[1,1]], carpetLen = 2))     

        