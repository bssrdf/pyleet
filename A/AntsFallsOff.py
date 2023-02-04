'''
-Hard-


'''

class Solution:
    def findOrderFalloff(self, arr, dirs, L): # dirs: 0: left, 1: right
        n = len(arr)
        events = []
        for i in range(n):
            if dirs[i] == 0:
                dis = arr[i]
                events.append([dis, 0])
            else:
                dis = L - arr[i]
                events.append([dis, 1])
        events.sort()
        l, r = 0, n-1
        res = []
        for _, dir in events:
            if dir == 0:
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res
    
if __name__ == "__main__":
    print(Solution().findOrderFalloff([4,  7,  11], [1, 0, 0], 14))




