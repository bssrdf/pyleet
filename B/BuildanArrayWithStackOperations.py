'''
-Medium-
*Queue*
*Stack*

You are given an integer array target and an integer n.

You have an empty stack with the two following operations:

"Push": pushes an integer to the top of the stack.
"Pop": removes the integer on the top of the stack.
You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:

If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
If the stack is not empty, pop the integer at the top of the stack.
If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.
Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].
Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].
Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.
 

Constraints:

1 <= target.length <= 100
1 <= n <= 100
1 <= target[i] <= n
target is strictly increasing.
Accepted
70.2K
Submissions
98K
Acceptance Rate
71.6%

'''

from typing import List
from collections import deque

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        que = deque(target)
        ans, i = [], 1
        while que:
            while que and que[0] != i:
                ans.append('Push')
                ans.append('Pop')
                i += 1
            que.popleft()
            ans.append('Push')
            i += 1
        return ans
    
    def buildArray2(self, target: List[int], n: int) -> List[str]:
        stack = target[::-1]
        ans, i = [], 1
        while stack:
            while stack and stack[-1] != i:
                ans.append('Push')
                ans.append('Pop')
                i += 1
            stack.pop()
            ans.append('Push')
            i += 1
        return ans


if __name__ == "__main__":
    print(Solution().buildArray(target = [1,3], n = 3))
    print(Solution().buildArray(target = [1,2,3], n = 3))
    print(Solution().buildArray(target = [1,2], n = 4))
    print(Solution().buildArray2(target = [1,3], n = 3))
    print(Solution().buildArray2(target = [1,2,3], n = 3))
    print(Solution().buildArray2(target = [1,2], n = 4))