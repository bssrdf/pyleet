'''


-Hard-


$$$

Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...

Now, you will have a new integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...].

Given an integer n, return the nth (1-indexed) integer in the new sequence.

 

Example 1:

Input: n = 9
Output: 10
Example 2:

Input: n = 10
Output: 11
 

Constraints:

1 <= n <= 8 * 108

'''

class Solution:
  def newInteger(self, n: int) -> int:
    ans = []
    while n:
      ans.append(str(n % 9))
      n //= 9
    return ''.join(reversed(ans))

if __name__ == "__main__":
    print(Solution().newInteger(10))

    print(Solution().newInteger(23))
