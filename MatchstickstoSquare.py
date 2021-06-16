'''
-Medium-

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 10^9

'''

class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        n = len(matchsticks)
        sm = sum(matchsticks)
        if sm % 4 != 0: return False
        side = sm // 4
        sides = [0]*4
        matchsticks.sort(reverse=True)
        def dfs(i, sides):
            if i == n:
                return all(s == side for s in sides)
            for j in range(4):
                if sides[j] + matchsticks[i] > side: continue  
                sides[j] += matchsticks[i]
                if dfs(i+1, sides): return True
                sides[j] -= matchsticks[i]
            #print('Exit: ', i, sides)
            return False
        return dfs(0, sides)
        
    def makesquareAC(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def dfs(nums, pos, target):
            if pos == len(nums): return True
            for i in range(4):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos+1, target): return True
                    target[i] += nums[pos]
            return False
        if len(nums) < 4 : return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % 4 != 0: return False
        target = [numSum//4] * 4
        return dfs(nums,0, target)    



if __name__ == "__main__":
    #print(Solution().makesquare([1,1,2,2,2]))
    #print(Solution().makesquare([3,3,3,3,4]))
    matches = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
    #print(len(matches))
    #print(Solution().makesquareAC(matches))
    print(Solution().makesquare(matches))