'''



'''

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def averageHeightOfBuildings(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        points = []
        for x, y, h in buildings:
            points.append((x, 1, h))
            points.append((y, -1, h))
        points.sort()
        result = []
        total = cnt = 0
        prev = -1
        for curr, c, h in points:
            if cnt and curr != prev:
                if result and result[-1][1] == prev and result[-1][2] == total//cnt:
                    result[-1][1] = curr
                else:
                    result.append([prev, curr, total//cnt])
            total += h*c
            cnt += c
            prev = curr
        return result