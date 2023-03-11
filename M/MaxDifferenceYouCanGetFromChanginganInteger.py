'''
-Medium-

You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888
Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8
 

Constraints:

1 <= num <= 108




'''


class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        mx, mi = -1, 10**9
        for i in range(10):            
            for j in range(10):
                if j == 0 and int(s[0]) == i:
                    continue
                s1 = ''
                for k in range(len(s)):
                    if int(s[k]) == i:
                        s1 += str(j)
                    else:
                        s1 += s[k]
                x = int(s1)
                mx = max(mx, x)
                mi = min(mi, x)
        return mx - mi        
                
                    

if __name__ == '__main__':
    print(Solution().maxDiff(123456))       
    print(Solution().maxDiff(111))       