'''
-Medium-

The i-th person has weight people[i], and each boat can carry a maximum weight 
of limit.

Each boat carries at most 2 people at the same time, provided the sum of the 
weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is 
guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

'''

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        n = len(people)
        res = 0
        l, r = 0, n-1
        while l <= r:
            if people[l]+people[r] <= limit:
                l += 1           
            r -= 1
            res += 1        
        return res
        

if __name__ == "__main__":
    print(Solution().numRescueBoats([1,2], 3))
    print(Solution().numRescueBoats([3,2,2,1], 3))
    print(Solution().numRescueBoats([3,5,3,4], 5))
    print(Solution().numRescueBoats([5,1,4,2], 6))