'''
-Hard-

There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms 
where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi 
and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. 
The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id. 
If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.

 

Example 1:

Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
Output: [3,-1,3]
Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.
Example 2:

Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
Output: [2,1,3]
Explanation: The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.
 

Constraints:

n == rooms.length
1 <= n <= 10^5
k == queries.length
1 <= k <= 104
1 <= roomIdi, preferredj <= 10^7
1 <= sizei, minSizej <= 10^7

'''

from collections import defaultdict
import bisect
from bisect import bisect_right

class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda x: x[1], reverse=True)  # Sort by decreasing order of room size
        qArr = [[i, q] for i, q in enumerate(queries)]  # Zip queries with their index
        qArr.sort(key=lambda x: x[1][1], reverse=True)  # Sort by decreasing order of query minSize

        def searchClosestRoomId(preferredId):
            if not roomIdsSoFar:  return -1
            cands = []
            i = bisect_right(roomIdsSoFar, preferredId)
            if i > 0:
                cands.append(roomIdsSoFar[i - 1])
            if i < len(roomIdsSoFar):
                cands.append(roomIdsSoFar[i])
            return min(cands, key=lambda x: abs(x - preferredId))

        roomIdsSoFar = []  # Room id is sorted in increasing order
        n, k = len(rooms), len(queries)
        i = 0
        ans = [-1] * k
        for index, (prefferedId, minSize) in qArr:
            while i < n and rooms[i][1] >= minSize:
                bisect.insort(roomIdsSoFar, rooms[i][0])  # Add id of the room which its size >= query minSize
                i += 1
            ans[index] = searchClosestRoomId(prefferedId)
        return ans
    
    def closestRoomWithStreamQueries(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """ 
        def closer(target, alt1, alt2):
            if alt1 == -1: return alt2
            if alt2 == -1: return alt1
            if abs(alt1 - target) < abs(alt2 - target): return alt1
            if abs(alt1 - target) == abs(alt2 - target) and alt1 < alt2: return alt1
            return alt2

        rooms.sort()
        
        # vector of indices with closest element by ID, which has a room
        # size greater than this; if non-existing: -1 (from left and right)       
        n = len(rooms)
        left, right = [-1]*n, [-1]*n

        for i in range(1, n): # look only at the left side
            idx = i - 1
            while (idx >= 0 and rooms[i][1] >= rooms[idx][1]):
                idx = left[idx]
            left[i] = idx

        for i in range(n-2, -1,-1): # look only at the right side
            idx = i + 1
            while (idx >= 0 and idx < n and 
                   rooms[i][1] >= rooms[idx][1]):
                idx = right[idx]
            right[i] = idx
        print(rooms)
        ans = []
        for q in queries:
            idx = bisect.bisect_left(rooms, [q[0],0]) # compare by ID
            if idx == n: idx = n-1
            id = -1 
            i = idx
            while i >= 0 and rooms[i][1] < q[1]:
                i = left[i]
            if q == [7,7]:
                print('l', q, idx, i)
            if i >= 0: id = closer(q[0], rooms[i][0], id)
            i = idx
            while i >= 0 and rooms[i][1] < q[1]:
                i = right[i]
            if i >= 0: id = closer(q[0], rooms[i][0], id)
            if q == [7,7]:
                print('r', q, idx, i)
            if rooms[idx][0] > q[0]:
                i = idx - 1
                while i >= 0 and rooms[i][1] < q[1]:
                    i = left[i]
                if i >= 0: id = closer(q[0], rooms[i][0], id)
                i = idx - 1
                while i >= 0 and rooms[i][1] < q[1]:
                    i = right[i]
                if i >= 0: id = closer(q[0], rooms[i][0], id)
            ans.append(id)
        return ans
        

if __name__ == "__main__":
    #print(Solution().closestRoom(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]))
    #print(Solution().closestRoomWithStreamQueries(rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]))
    #print(Solution().closestRoom([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]]))
    #print(Solution().closestRoomWithStreamQueries([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]]))
    print(Solution().closestRoom([[11,6],[6,11],[1,22],[20,2],[21,7],[8,15],[4,17],[13,22],[17,16],[22,11]],
      [[21,20],[23,24],[6,20],[5,23],[8,1],[1,4],[10,11],[24,10],[7,12],[7,7]]))
    print(Solution().closestRoomWithStreamQueries([[11,6],[6,11],[1,22],[20,2],[21,7],[8,15],[4,17],[13,22],[17,16],[22,11]],
      [[21,20],[23,24],[6,20],[5,23],[8,1],[1,4],[10,11],[24,10],[7,12],[7,7]]))