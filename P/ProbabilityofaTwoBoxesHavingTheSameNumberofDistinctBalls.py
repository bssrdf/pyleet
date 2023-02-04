'''

-Hard-
Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

Return the probability that the two boxes have the same number of distinct balls. Answers within 10-5 of the actual value will be accepted as correct.

 

Example 1:

Input: balls = [1,1]
Output: 1.00000
Explanation: Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1
Example 2:

Input: balls = [2,1,1]
Output: 0.66667
Explanation: We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equal probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that, we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667
Example 3:

Input: balls = [1,2,1,2]
Output: 0.60000
Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6
 

Constraints:

1 <= balls.length <= 8
1 <= balls[i] <= 6
sum(balls) is even.

'''

from typing import List
import math
from functools import reduce
import operator

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        from math import factorial
        
        firstHalf = {}
        secondHalf = {}
        
        # successful permutations
        self.good = 0
        # total number of valid permutations
        self.all = 0
        def dfs(i):
            if i == len(balls):
                s1 = sum(firstHalf.values())
                s2 = sum(secondHalf.values())
                # invalid permutation if the total number of balls in each
                # half is not equal, because we only consider permutations
                # with equal balls in each half
                if s1 != s2:
                    return 0
                
                # Get the number of permutations in the FIRST HALF of the result array.
				# If you don't understand, search "geeks for geeks number of distinct permutations" on Google.
                prod1 = 1
                for k in firstHalf:
                    prod1 *= factorial(firstHalf[k])
                p1 = factorial(s1) / prod1
                
                # Same as above but for the SECOND HALF of the array.
                prod2 = 1
                for k in secondHalf:
                    prod2 *= factorial(secondHalf[k])
                p2 = factorial(s2) / prod2
                
                # We can use each permutation as many times as possible since the problem
                # tells us they're all unique regardless of order. So [1, 2 / 1, 3] is separate
                # from [2, 1 / 3, 1].
                self.all += p1 * p2
                # only add to the "successful" permutations if we meet our success criteria: equal number 
                # of unique balls in each half of the array.
                self.good += p1 * p2 if len(firstHalf) == len(secondHalf) else 0
            else:
                # This will calculate every permutation of splitting the number of balls of color i
                # into each half. We So if there are 3 balls of color i, the iterations will split like this,
                # in order:
                # 0 -> first: 3, second: 0
                # 1 -> first: 2, second: 1
                # 2 -> first: 1, second: 2
                # 3 -> first: 0, second: 3
                firstHalf[i] = balls[i]
                for _ in range(balls[i] + 1):
                    dfs(i + 1)
                    
                    if i in firstHalf:
                        firstHalf[i] -= 1
                        if firstHalf[i] == 0:
                            del firstHalf[i]
                    secondHalf[i] = secondHalf.get(i, 0) + 1
                    
                del secondHalf[i]
                
        dfs(0)
        # print(self.good, self.all)
        # if we have X good permutations and Y total permutations, the odds that a randomly
        # selected permutation will be "good" is X / Y AS LONG AS each permutation is equally likely.
        return self.good / self.all
    
    def getProbability2(self, balls: List[int]) -> float:
        self.total = 0
        self.good = 0
        self.sum = sum(balls)
        left, right = {}, {}
        permutation = lambda n, x:math.factorial(n)/reduce(operator.mul,[math.factorial(i) for i in x.values()])
        def dfs(i, sum1, sum2, color1, color2):
            if abs(sum1 - sum2) > self.sum - sum1 - sum2: return
            if i == len(balls):
                if sum1 != sum2: return
                p1, p2 = permutation(sum1, left), permutation(sum2, right)
                self.total += p1 * p2
                self.good += p1 * p2 * (color1 == color2)
            else:
                for j in range(balls[i] + 1):
                    left[i], right[i] = j, balls[i] - j
                    dfs(i+1, sum1 + j, sum2 + balls[i] - j, color1 + (j != 0), color2 + (balls[i] != j))
        dfs(0, 0, 0, 0, 0)
        return self.good/self.total


if __name__ == "__main__":
    print(Solution().getProbability(balls = [1,2,1,2]))