'''
A string S of lowercase letters is given. We want to partition this 
string into as many parts as possible so that each letter appears in 
at most one part, and return a list of integers representing the size 
of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because 
it splits S into less parts.

'''

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        book={}
        for i,s in enumerate(S):
            book[s] = i
        print(book)
        lo = hi = 0
        res = []
        for i,s in enumerate(S):
            hi = max(hi, book[s])
            if hi == i:
                res.append(hi-lo+1)
                lo = hi + 1
        return res
        

print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

        