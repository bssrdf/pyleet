'''
-Medium-

There is a forest with an unknown number of rabbits. We asked n rabbits 
"How many rabbits have the same color as you?" and collected the answers in an 
integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11
 

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000

'''

import math
from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        C = Counter(answers)
        res = 0
        #for k in sorted(C.keys(), reverse=True):            
        for k in C:
            #res += (k+1) * ( 1 if C[k]//(k+1) == 0 else math.ceil(C[k]/(k+1)) )
            res += (k+1) * math.ceil(C[k]/(k+1))
        #    print(k, C[k], res)
        return res    
                

        
if __name__ == "__main__":
    print(Solution().numRabbits([1,1,2]))
    print(Solution().numRabbits([10,10,10]))
    print(Solution().numRabbits([0,0,1,1,1]))