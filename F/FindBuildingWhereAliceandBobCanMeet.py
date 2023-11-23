'''

-Hard-

You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

 

Example 1:

Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.  
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
Example 2:

Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

 

Constraints:

1 <= heights.length <= 5 * 104
1 <= heights[i] <= 109
1 <= queries.length <= 5 * 104
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1



'''

from typing import List

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(heights), len(queries)
        a, q = heights, queries
        st = []
        res = [-1]*len(q)
        # rearrange the query, sort by right boarder
        q = [(q[i][0],q[i][1],i) for i in range(len(q))]
        q.sort(key=lambda x: max(x[0],x[1]))
        for i in range(n-1,-1,-1):
            # process the query with i as the right boarder 
            while q and max(q[-1][1],q[-1][0])==i:
                x, y, pos = q.pop()
                if x > y: x, y = y, x
                if x == y or a[x] < a[y]: 
                    res[pos] = y; continue
                #from here a[x] >= a[y]    
                if len(st) == 0 or st[0][0] <= a[x]: 
                    continue
                if st[-1][0] > a[x]: 
                    res[pos] = st[-1][1]; continue
                lo, hi = 0, len(st)-1
                while lo < hi-1:
                    md = (lo + hi) // 2
                    if st[md][0] > a[x]: 
                        lo = md
                    else: 
                        hi = md
                res[pos] = st[lo][1]
            # maintain the monotonic stack
            while st and st[-1][0] <= a[i]:
                st.pop()
                # else: break
            st.append((a[i],i))
        return res

    def leftmostBuildingQueries2(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(heights), len(queries)
        a, q = heights, queries
        st = []
        res = [-1]*m
        # rearrange the query, sort by right boarder
        q = [(q[i][0],q[i][1],i) for i in range(len(q))]
        q.sort(key=lambda x: max(x[0],x[1]))
        for i in range(n-1,-1,-1):
            # process the query with i as the right boarder 
            while q and max(q[-1][1],q[-1][0])==i:
                x, y, pos = q.pop()
                if x > y: x, y = y, x
                if x == y or a[x] < a[y]: 
                    res[pos] = y; continue
                #from here a[x] >= a[y]    
                lo, hi = 0, len(st)
                while lo < hi:
                    md = (lo + hi) // 2
                    if st[md][0] > a[x]: 
                        lo = md + 1
                    else: 
                        hi = md
                if lo == 0: continue         
                res[pos] = st[lo-1][1]
            # maintain the monotonic stack
            while st and st[-1][0] <= a[i]:
                st.pop()
            st.append((a[i],i))
        return res
    


if __name__ == "__main__":
    print(Solution().leftmostBuildingQueries(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))   
    print(Solution().leftmostBuildingQueries(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]])) 
    print(Solution().leftmostBuildingQueries(heights = [5,3,8,2,6,4,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))     
    print(Solution().leftmostBuildingQueries(heights = [3,4,1,2], queries=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]))

    print(Solution().leftmostBuildingQueries2(heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]))   
    print(Solution().leftmostBuildingQueries2(heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))
    print(Solution().leftmostBuildingQueries(heights = [5,3,8,2,6,4,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]))      
    print(Solution().leftmostBuildingQueries2(heights = [3,4,1,2], queries=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]))
