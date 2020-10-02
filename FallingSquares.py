'''
On an infinite number line (x-axis), we drop given squares in the order they 
are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square 
with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and 
from a higher height than all currently landed squares. We wait for each 
square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain 
fixed to any positive length surface they touch (either the number line or 
another square). Squares dropped adjacent to each other will not stick 
together prematurely.

 
 highest height of any square we have dropped, after dropping squares 
 represented by positions[0], positions[1], ..., positions[i].

Example 1:

Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:
After the first drop of positions[0] = [1, 2]: _aa _aa ------- The maximum 
height of any square is 2.

After the second drop of positions[1] = [2, 3]: __aaa __aaa __aaa _aa__ _aa__ -------------- 
The maximum height of any square is 5. The larger square stays on top of 
the smaller square despite where its center of gravity is, because squares 
are infinitely sticky on their bottom edge.

After the third drop of positions[1] = [6, 1]: __aaa __aaa __aaa _aa _aa___a 
-------------- The maximum height of any square is still 5. Thus, we return 
an answer of [2, 5, 5].

 

 
Example 2:

Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom 
edge can stick to surfaces.
 

Note:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
 
'''

from sortedcontainers import SortedDict, SortedKeyList
import bisect
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        sd = SortedDict()
        curMax = 0
        for pos in positions:
            start, end, h = pos[0], pos[0]+pos[1], 0
            t = []
            keys = sd.keys()            
            index = sd.bisect_left((start, start))
            if index > 0:
                index -= 1 
                if keys[index][1] <= start:
                    index += 1            
            delete = []
            while index < len(keys) and keys[index][0] < end:
                if (start > keys[index][0]):
                     t.append((keys[index][0], start, sd[keys[index]]))
                if (end < keys[index][1]):
                     t.append((end, keys[index][1], sd[keys[index]]))
                h = max(h, sd[keys[index]])                
                delete.append(keys[index])               
                index += 1
            
            for d in delete:
                sd.pop(d)            
            sd[(start, end)] = h + pos[1]
            for a in t:
                sd[(a[0], a[1])] = a[2]
            curMax = max(curMax, h + pos[1])          
            
            res.append(curMax)
        return res

    def fallingSquaresFast(self, positions):
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            max_h = max(max_h, high)
            res.append(max_h)
            print(i,j,pos,height)
        return res





if __name__ == "__main__":
    print(Solution().fallingSquaresFast([[1, 2], [3, 3], [6, 1]]))
    #print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
    #print(Solution().fallingSquares([[100, 100], [200, 100]]))    
    #print(Solution().fallingSquares([[4,6],[4,2],[4,3]]))