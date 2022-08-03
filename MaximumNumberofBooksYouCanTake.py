'''
-Hard-
*Monotonic Stack*
*DP*

You are given a 0-indexed integer array books of length n where books[i] denotes 
the number of books on the i-th shelf of a bookshelf.

You are going to take books from a contiguous section of the bookshelf spanning from l to r 
where 0 <= l <= r < n. 

For each index i in the range l <= i < r, you must take strictly fewer books from shelf i 
than shelf i + 1.

Return the maximum number of books you can take from the bookshelf.

 

Example 1:

Input: books = [8,5,2,7,9]
Output: 19
Explanation:
- Take 1 book from shelf 1.
- Take 2 books from shelf 2.
- Take 7 books from shelf 3.
- Take 9 books from shelf 4.
You have taken 19 books, so return 19.
It can be proven that 19 is the maximum number of books you can take.
Example 2:

Input: books = [7,0,3,4,5]
Output: 12
Explanation:
- Take 3 books from shelf 2.
- Take 4 books from shelf 3.
- Take 5 books from shelf 4.
You have taken 12 books so return 12.
It can be proven that 12 is the maximum number of books you can take.
Example 3:

Input: books = [8,2,3,7,3,4,0,1,4,3]
Output: 13
Explanation:
- Take 1 book from shelf 0.
- Take 2 books from shelf 1.
- Take 3 books from shelf 2.
- Take 7 books from shelf 3.
You have taken 13 books so return 13.
It can be proven that 13 is the maximum number of books you can take.


Example 4:

Input: books = [1,0,2,3,10,11,12]
Output: 38


Constraints:

1 <= books.length <= 105
0 <= books[i] <= 105


'''

from typing import List

class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        # 设dp[i]表示以books[i] 结尾时能取走的书的最大数量。
        # 若从 i 到 0 可以取成一个公差为 1 的等差数列，那么dp[i]可以直接通过等差数列求和算出。
        # 若从 i 到 0 不能取成一个公差为 -1 的等差数列，即这个规律在某个 j 处断掉了（0 <= j < i），
        # 那么一定有 books[j] < books[i] - (i-j) 也即 books[j] - j < books[i] - i 
        # 利用单调栈在新数组 books[i]-i 的每个位置，找到左边第一个比它严格小的数的位置，可以
        # 求出符合题意的 j，此时 
        # dp[i] = dp[j] + sum_k(books[k]-k) k=j+1,i

        # 答案为 max(dp[i])

        # 时间复杂度 O(n)
        nums = [v - i for i, v in enumerate(books)]
        n = len(nums)
        left = [-1] * n
        stk = []
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        # print(left)
        ans = 0
        dp = [0] * n
        dp[0] = books[0]
        for i, v in enumerate(books):
            j = left[i]
            cnt = min(v, i - j)
            u = v - cnt + 1
            s = (u + v) * cnt // 2
            dp[i] = s + (0 if j == -1 else dp[j])
            # print(i, dp[i], s, cnt, dp[j])
            ans = max(ans, dp[i])
        return ans
    
    def maximumBooks2(self, books: List[int]) -> int:
        # dp[i] := max # of books we can take from books[0..i]
        # with taking all of books[i]
        dp = [0] * len(books)
        stack = []  # possible indices we can reach

        for i, book in enumerate(books):
            # we may take all of books[j] where books[j] < books[i] - (i - j)
            while stack and books[stack[-1]] >= book - (i - stack[-1]):
                stack.pop()
            # we can now take books[j + 1..i]
            j = stack[-1] if stack else -1
            lastPicked = book - (i - j) + 1
            if lastPicked > 1:
                # book + (book - 1) + ... + (book - (i - j) + 1)
                dp[i] = (book + lastPicked) * (i - j) // 2
            else:
                # 1 + 2 + ... + book
                dp[i] = book * (book + 1) // 2
            if j >= 0:
                dp[i] += dp[j]
            stack.append(i)

        return max(dp)

if __name__ == "__main__":
    print(Solution().maximumBooks(books = [8,5,2,7,9]))
    print(Solution().maximumBooks(books = [8,2,3,7,3,4,0,1,4,3]))
    print(Solution().maximumBooks(books = [1,0,2,3,10,11,12]))

    print(Solution().maximumBooks2(books = [8,5,2,7,9]))
    print(Solution().maximumBooks2(books = [8,2,3,7,3,4,0,1,4,3]))
    print(Solution().maximumBooks2(books = [1,0,2,3,10,11,12]))