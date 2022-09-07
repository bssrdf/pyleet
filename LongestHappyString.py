'''

-Medium-

A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0




'''
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        pq = [(-i,ch) for i,ch in zip([a,b,c], 'abc') if i > 0] 
        heapq.heapify(pq)
        # print(pq)
        ans = ''
        while pq:
            cnt, ch = heapq.heappop(pq)
            # print('XX',cnt, ch)
            cnt = -cnt
            if len(ans) >= 2 and ans[-2] == ch and ans[-1] == ch:
                if pq:
                    cnt1, ch1 = heapq.heappop(pq)                    
                    cnt1 = -cnt1
                    ans += ch1
                    cnt1 -= 1
                    if cnt1 > 0:
                        heapq.heappush(pq, (-cnt1, ch1))
                    heapq.heappush(pq, (-cnt, ch))    
                else:
                    break
            else:
                ans += ch
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(pq, (-cnt, ch))
            # print(ans, pq)
        return ans
        


if __name__ == "__main__":
    print(Solution().longestDiverseString(a = 1, b = 1, c = 7))
    print(Solution().longestDiverseString(a = 7, b = 1, c = 0))
        