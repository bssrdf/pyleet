'''

-Medium-

An integer x is numerically balanced if for every digit d in the number x, there are exactly d occurrences of that digit in x.

Given an integer n, return the smallest numerically balanced number strictly greater than n.

 

Example 1:

Input: n = 1
Output: 22
Explanation: 
22 is numerically balanced since:
- The digit 2 occurs 2 times. 
It is also the smallest numerically balanced number strictly greater than 1.
Example 2:

Input: n = 1000
Output: 1333
Explanation: 
1333 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times. 
It is also the smallest numerically balanced number strictly greater than 1000.
Note that 1022 cannot be the answer because 0 appeared more than 0 times.
Example 3:

Input: n = 3000
Output: 3133
Explanation: 
3133 is numerically balanced since:
- The digit 1 occurs 1 time.
- The digit 3 occurs 3 times.
It is also the smallest numerically balanced number strictly greater than 3000.
 

Constraints:

0 <= n <= 106



'''


from collections import Counter

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def backtracking(i, numLen, curNum, counter):
            if i == numLen:
                isBalanceNumber = True
                for d, freq in counter.items():
                    if freq != 0 and d != freq:
                        isBalanceNumber = False
                if isBalanceNumber:
                    yield curNum
                return

            for d in range(1, numLen+1):
                if counter[d] >= d: continue   # Prune if number of occurrences of `d` is greater than `d`
                if counter[d] + (numLen - i) < d: continue  # Prune if not enough number of occurrences of `d`
                counter[d] += 1
                yield from backtracking(i + 1, numLen, curNum * 10 + d, counter)
                counter[d] -= 1

        for numLen in range(len(str(n)), len(str(n)) + 2):
            for num in backtracking(0, numLen, 0, Counter()):
                if num > n:
                    return num