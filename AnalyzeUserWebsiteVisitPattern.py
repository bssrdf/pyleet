'''
-Medium-

You are given three arrays username, timestamp and website of the same length N where the ith tuple means that the user 
with name username[i] visited the website website[i] at time timestamp[i].
A 3-sequence is a list of not necessarily different websites of length 3 sorted in ascending order by the time of their visits.
Find the 3-sequence visited at least once by the largest number of users. If there is more than one solution, 
return the lexicographically minimum solution.
A 3-sequence X is lexicographically smaller than a 3-sequence Y if X[0] < Y[0] or X[0] == Y[0] 
and (X[1] < Y[1] or X[1] == Y[1] and X[2] < Y[2]). 
It is guaranteed that there is at least one user who visited at least 3 websites. No user visits two websites at the same time.
Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], 
website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 
Note:
3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.

'''

from collections import defaultdict
from collections import Counter
from itertools import combinations


class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        d = defaultdict(list)

        for t, u, w in sorted(zip(timestamp, username, website)):
            d[u].append(w)
        c = Counter()
        for u in d:
            c += Counter(set(seq for seq in combinations(d[u], 3)))
        target = max(c.values())

        return min(list(k) for k in c if c[k] == target)
    
if __name__ == '__main__':
    username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    timestamp = [1,2,3,4,5,6,7,8,9,10]
    website = ["home","about","career","home","cart","maps","home","home","about","career"]

    print(Solution().mostVisitedPattern(username, timestamp, website))