'''

-Medium-

You are given a 0-indexed binary string s which represents the types of buildings 
along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. 
However, to ensure variety, no two consecutive buildings out of the selected 
buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings 
as that would form "011" which is not allowed due to having two consecutive 
buildings of the same type.
Return the number of valid ways to select 3 buildings.

 

Example 1:

Input: s = "001101"
Output: 6
Explanation: 
The following sets of indices selected are valid:
- [0,2,4] from "001101" forms "010"
- [0,3,4] from "001101" forms "010"
- [1,2,4] from "001101" forms "010"
- [1,3,4] from "001101" forms "010"
- [2,4,5] from "001101" forms "101"
- [3,4,5] from "001101" forms "101"
No other selection is valid. Thus, there are 6 total ways.
Example 2:

Input: s = "11100"
Output: 0
Explanation: It can be shown that there are no valid selections.
 

Constraints:

3 <= s.length <= 105
s[i] is either '0' or '1'.




'''


class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        c0, c1, dp10, dp01, dp = 0, 0, 0, 0, 0
        for i in range(n):
            if s[i] == '0': 
                dp += dp01
                c0 += 1
                dp10 += c1                
            else: 
                dp += dp10
                c1 += 1
                dp01 += c0  
            # print(i, s[i], c0, c1, dp10, dp01, dp0, dp)
        return dp

            

            

if __name__ == "__main__":
    print(Solution().numberOfWays("001101"))        
    print(Solution().numberOfWays("11100"))        