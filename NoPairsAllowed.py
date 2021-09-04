'''

-Medium-

You have a boutique that specializes in words that don't have adjacent matching characters. 
Bobby, a competitor, has decided to get out of the word business altogether and you have 
bought his inventory, your idea is to modify his inventory of words so they are suitabble for 
sale in your store. To do this, you find all adjacent pairs of matching charcaters and replace 
one of the charcters with a different one. Detemine the minimum number of characters that must 
be replaced to make a salable word. For example, you purchased words = ["odd","boook","treak"]. 
You will create an array with your results form the tests. Change 'd' in "odd", change 'o' in 
"boook" and no change is necessary in "treak". The return array result = [1,1,0].

Complete the function minimalOperation in the editor below. The function must return an array of 
integers, each result[i] being the minimum operations needed to fix words[i].

1 <= n <= 100
2 <= len(words[i]) <= 10^5
Each character of words[i] in ascii['a'-'z']
样例
Example 1:

Input: ["ab","aab","abb","abab","abaaaba"]
Output: [0,1,1,0,1]
Example 2:

Input: ["odd","boook","treak"]
Output: [1,1,0]

'''

class Solution:
    """
    @param words: The array words that you need to calculate minimal operation .
    @return: Return an array of integers, each result[i] being the minimum operations needed to fix words[i].
    """
    def minimalOperation (self, words):
        # Write your code here.
        res = [0]*len(words)
        for i,w in enumerate(words):
            start, cnt = 0, 1
            for j in range(1,len(w)):
                if w[j] == w[start]:
                    cnt += 1                    
                else:
                    if cnt > 1:
                        res[i] += cnt//2
                        cnt = 1
                    start = j                  
            if cnt > 1:
                res[i] += cnt//2
        return res    


if __name__ == "__main__":
    print(Solution().minimalOperation(["ab","aab","abb","abab","abaaaba"]))
    print(Solution().minimalOperation(["odd","boook","treak"]))