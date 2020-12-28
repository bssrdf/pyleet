'''
-Medium-
*BFS*

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely 
 and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each 
 move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 
wheels.

You are given a list of deadends dead ends, meaning if the lock displays any 
of these codes, the wheels of the lock will stop turning and you will be 
unable to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if 
it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" 
-> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" 
would be invalid,
because the wheels of the lock become stuck after the display becomes the 
dead end "0102".
Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], 
target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1
 

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.

'''

from collections import deque

class Solution(object):

    def openLockBiBFS(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        qs = deque(['0000'])
        qd = deque([target])
        steps_s, steps_d = 0, 0
        visited_s = set(deadends)
        if '0000' in visited_s: return -1
        visited_s.add('0000')
        visited_d = set(deadends)        
        visited_d.add(target)
        def enqueue(nc, w, i, vis, q):
            nw = w[:i]+nc+w[i+1:]
            if nw not in vis:
                vis.add(nw)
                q.append(nw)
        while qs and qd:
            if qs: 
                sq = len(qs)
                for i in range(sq):
                    wheel = qs.popleft()
                    if wheel == target or wheel in visited_d:
                        return steps_s+steps_d
                    for i,c in enumerate(wheel):
                        nc = str(int(c)+1) if int(c) < 9 else '0'
                        enqueue(nc, wheel, i, visited_s, qs)
                        nc = str(int(c)-1) if int(c) > 0 else '9'
                        enqueue(nc, wheel, i, visited_s, qs)                        
                steps_s += 1
            if qd: 
                sq = len(qd)
                for i in range(sq):
                    wheel = qd.popleft()
                    if wheel == '0000' or wheel in visited_s:
                        return steps_s+steps_d
                    for i,c in enumerate(wheel):
                        nc = str(int(c)+1) if int(c) < 9 else '0'
                        enqueue(nc, wheel, i, visited_d, qd)                        
                        nc = str(int(c)-1) if int(c) > 0 else '9'
                        enqueue(nc, wheel, i, visited_d, qd)
                steps_d += 1
        return -1

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        q = deque(['0000'])
        steps = 0
        visited = set(deadends)
        if '0000' in visited: return -1
        visited.add('0000')
        while q:
            sq = len(q)
            for i in range(sq):
                wheel = q.popleft()
                if wheel == target: return steps
                for i,c in enumerate(wheel):
                    nc = str(int(c)+1) if int(c) < 9 else '0'
                    nw = wheel[:i]+nc+wheel[i+1:]
                    if nw not in visited:
                        visited.add(nw)
                        q.append(nw)
                    nc = str(int(c)-1) if int(c) > 0 else '9'
                    nw = wheel[:i]+nc+wheel[i+1:]
                    if nw not in visited:
                        visited.add(nw)
                        q.append(nw)
            steps += 1
        return -1
        


                 


if __name__ == "__main__":
    print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))
    print(Solution().openLock(["8888"],  "0009"))
    print(Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
    print(Solution().openLock(["0000"], "8888"))

    print(Solution().openLockBiBFS(["0201","0101","0102","1212","2002"], "0202"))
    print(Solution().openLockBiBFS(["8888"],  "0009"))
    print(Solution().openLockBiBFS(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"))
    print(Solution().openLockBiBFS(["0000"], "8888"))