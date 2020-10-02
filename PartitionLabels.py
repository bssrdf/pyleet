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

        '''
        Figure out the rightmost index first and use it to denote the start
        of the next section.

        Reset the left pointer at the start of each new section.

        Store the difference of right and left pointers + 1 as in the 
        result for each section.

        '''
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
        
if __name__ == "__main__":
    print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

        