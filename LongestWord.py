'''
-Easy-

Given a dictionary, find all of the longest words in the dictionary.

样例
Example 1:
	Input: {
		"dog",
		"google",
		"facebook",
		"internationalization",
		"blabla"
		}
	Output: ["internationalization"]


Example 2:
	Input:  {
		"like",
		"love",
		"hate",
		"yes"		
		}
	Output: ["like", "love", "hate"]
	
挑战
It's easy to solve it in two passes, can you do it in one pass?

'''
from collections import defaultdict

class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        # write your code here
        m = defaultdict(list)
        mx = 0
        for word in dictionary:
            l = len(word)
            mx = max(mx, l)
            m[l].append(word)
        return m[mx]


if __name__ == "__main__":
    dict = ["dog",
		"google",
		"facebook",
		"internationalization",
		"blabla"]
    print(Solution().longestWords(dict))
    dict = ["like",
		"love",
		"hate",
		"yes"	]
    print(Solution().longestWords(dict))
    