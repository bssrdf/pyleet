'''
-Medium-

Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have 
unique characters.

Return the maximum possible length of s.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible solutions are "chaers" and "acters".
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lower case English letters.

'''

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        n = len(arr) 
        res = [0]
        uniques = []
        for a in arr:
            uniques.append(True if len(set(a)) == len(a) else False)
        def helper(start, str):
            res[0] = max(res[0], len(str))
            if start == n:            
                return
            for i in range(start, n):
                if not uniques[i]: continue
                isUnique = True 
                for c in arr[i]:
                    if c in str:
                        isUnique = False
                        break                
                if isUnique:
                    helper(i+1, str | set(arr[i]))
        helper(0, set())
        return res[0]        

        

if __name__ == "__main__":
    print(Solution().maxLength(["un","iq","ue"]))
    print(Solution().maxLength(["cha","r","act","ers"]))
    print(Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]))
    print(Solution().maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
    print(Solution().maxLength(["yy","bkhwmpbiisbldzknpm"]))