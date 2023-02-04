'''
-Hard-

Given two integer arrays arr1 and arr2, return the minimum number of operations 
(possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length 
and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
 

Constraints:

1 <= arr1.length, arr2.length <= 2000
0 <= arr1[i], arr2[i] <= 10^9

Hints:

Use dynamic programming.

The state would be the index in arr1 and the index of the previous element in arr2 
after sorting it and removing duplicates.

'''
import collections
import bisect

class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # dp is the data structure storing all promising current states. A state here 
        # refers to a key-value pair, whose first element is the number we choose for 
        # current position. This can be either chosen from the original arr1 or from a 
        # replacement action from arr2. The second element is how many times we change 
        # the number. 
        # In the outer iteration, each time we first pick up the original element in arr1 
        # as i. Then we look up in dp, trying to prolong each valid state we generated from 
        # the previous iteration. For example, we have state (5,0), and now i=7, we say um, 
        # it looks good so far we can generate a new state (7,0) because 7>5 it is increasing. 
        # No need to pick up a number from arr2. Meanwhile, another road is to choose a number 
        # from arr2 to replace 7. This number should be slightly bigger than 5. We choose the 
        # minimum number in arr2 that is bigger than 5, say 6. We can also add state (6,1) to dp. 
        # When both roads die, we can claim that the previous state can not be extended in this 
        # round. After we finish the final round, we look up into dp to see who survived the 
        # procedure and choose the minimum change one
        arr2 = sorted(set(arr2))
        dp = {-1:0}
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i],dp[key])
                loc = bisect.bisect_right(arr2,key)                
                if loc < len(arr2):
                    print(i, key, loc, arr2[loc])
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            dp = tmp
            print(dp)
        if dp:
            return min(dp.values())
        return -1

if __name__ == "__main__":
    #print(Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]))
    print(Solution().makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,4]))