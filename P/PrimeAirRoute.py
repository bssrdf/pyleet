'''
-Medium-
Given max. travel distance and forward and backward route list, return 
pair of ids of forward and backward routes that optimally utilized the 
max travel distance.:

eg: max travel distance is : 11000
forward route list : [1,3000],[2,5000],[3,4000],[4,10000]
backward route list : [1,2000],[2,3000],[3,4000]

Result : [2,3] ...2 is from forward and 3 is from backward...total distance 
is 9000...no other combination is there which is >9000 and <=11,000.......
O(n^2) solution is straight forward, thinking that sorting both might help.


'''

class Solution(object):
    def optimizedRoute(self, forward, backward, maxTarget):
        forward.sort(key = lambda x: x[1])
        backward.sort(key = lambda x: x[1])
        left, right = 0, len(backward)-1
        maxSofar = 0
        res = [0, 0]
        while left < len(forward) and right >= 0:
            sm = forward[left][1] + backward[right][1]
            if maxTarget >= sm:
                if maxSofar < sm:
                    maxSofar = sm
                    res[0], res[1] = forward[left][0], backward[right][0]
                left += 1
            else:
                right -= 1 
        return res
     #def optimizedRoute(self, forward, backward, maxTarget):


if __name__ == "__main__":
    print(Solution().optimizedRoute([[1,3000],[2,5000],[3,4000],[4,10000]],
      [[1,2000],[2,3000],[3,4000]], 11000))
    F = [[1,1000],[2,2000],[3,3000],[4,4000], [5,5000],[6,6000],[7,7000], [8, 8000]]
    B = [[1,2000],[2,3000],[3,3000],[4,4000], [5,5000],[6,6000]]
    print(Solution().optimizedRoute(F, B, 11000))

