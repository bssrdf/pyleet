'''

-Medium-
*BFS*

There are n people, each person has a unique id between 0 and n-1. Given the arrays 
watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of 
watched videos and the list of friends respectively for the person with id = i.

Level 1 of videos are all watched videos by your friends, level 2 of videos are all 
watched videos by the friends of your friends and so on. In general, the level k of 
videos are all watched videos by people with the shortest path exactly equal to k with you. 
Given your id and the level of videos, return the list of videos ordered by their 
frequencies (increasing). For videos with the same frequency order them alphabetically 
from least to greatest. 

 

Example 1:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
Output: ["B","C"] 
Explanation: 
You have id = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with id = 1 -> watchedVideos = ["C"] 
Person with id = 2 -> watchedVideos = ["B","C"] 
The frequencies of watchedVideos by your friends are: 
B -> 1 
C -> 2
Example 2:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
Output: ["D"]
Explanation: 
You have id = 0 (green color in the figure) and the only friend of your friends is the person with id = 3 (yellow color in the figure).
 

Constraints:

n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= id < n
1 <= level < n
if friends[i] contains j, then friends[j] contains i

'''

from collections import deque
from collections import Counter
import heapq

class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        n = len(friends)
        queue = deque([id])
        visited = [False] * n
        visited[id] = True
        c = Counter()
        k = 0
        while queue:
            q = deque()
            while queue:
               cur = queue.popleft()
               for i in friends[cur]:
                    if not visited[i]:
                       visited[i] = True
                       q.append(i)
            queue = q
            k += 1
            if k == level: break        
        c = Counter([v for idx in queue for v in watchedVideos[idx]])    
        return sorted(c.keys(),key=lambda x:(c[x],x))

    def watchedVideosByFriendsFast(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        # 96%
        bfs,visited={id},{id}
        for _ in range(level):
            bfs={j for i in bfs for j in friends[i] if j not in visited}
            visited|=bfs
        freq=Counter([v for idx in bfs for v in watchedVideos[idx]])
        return sorted(freq.keys(),key=lambda x:(freq[x],x))
        




if __name__ == '__main__':
    print(Solution().watchedVideosByFriends([["A","B"],["C"],["B","C"],["D"]], 
    [[1,2],[0,3],[0,3],[1,2]], 0, 1))

    print(Solution().watchedVideosByFriends([["xk","qvgjjsp","sbphxzm"],["rwyvxl","ov"]],
      [[1],[0]], 0, 1))

