'''
-Medium-

You are the technical director of WSPT radio, serving listeners nationwide. 
For simplicity’s sake we can consider each listener to live along a horizontal 
line stretching from 0 (west) to 1000 (east).
Given a list of N listeners, and a list of M radio towers, each placed at 
various locations along this line, determine what the minimum broadcast 
range would have to be in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15]. 
In this case the minimum range would be 5, since that would be required 
for the tower at position 15 to reach the listener at position 20

'''
class Solution(object):
    def argestTowerRange(self, tower, listener):
        """
        :type tower:    List[int]
        :type listener: List[int]
        :rtype: int
        """
        leftTower, rightTower = -1000, tower[0]
        res = 0
        m, n = len(listener), len(tower)
        i, j = 0, 0
        while i < m:
            if listener[i] < rightTower:
                l, r = listener[i]-leftTower, rightTower-listener[i]
                res = max(res, min(l, r))
                i += 1
            else:
                leftTower = tower[j]
                j += 1
                if j < n:
                    rightTower = tower[j]
                else:
                    rightTower = 2000
        return res

if __name__ == "__main__":
    print(Solution().argestTowerRange([4, 8, 15],  [1, 5, 11, 20]))        