'''
-Medium-

Given a numeric string str (all the characters are 
from the range [‘0’, ‘9’]). The task is to count the number of 
sub-strings of str that are divisible by 3.

Examples: 

Input: str = “303”, 
Output: 6 



'''
from collections import defaultdict

class Solution(object):
    
    def countSubStrDP(self, str):
        cnt=0
        (ss0,ss1,ss2)=(0,0,0)
        for i in range(len(str)):
            r = int(str[i])%3
            if r == 0:
                ss0 += 1
            elif r == 1:
                (ss0,ss1,ss2) = (ss2,ss0,ss1)
                ss1 += 1
            elif r == 2:
                (ss0,ss1,ss2) = (ss1,ss2,ss0)
                ss2 += 1
            cnt += ss0
        return cnt


if __name__ == '__main__':
    str = "303"
    print(Solution().countSubStrDP(str))
    str = "392301"
    print(Solution().countSubStrDP(str))

