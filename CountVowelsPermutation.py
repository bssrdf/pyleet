'''
-Hard-

Given an integer n, your task is to count how many strings of length n can be formed 
under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4

'''

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        知道了上面这两个关系，我们可以将这道题想象成一个树结构，树的所有分支即是答案。
        
        比如当树的高度为1时，
        有5个分支分别为a，e，i，o，u。

        当高度为2时：

        a下面有1个分支e
        e下面有2个分支a和i
        i下面有4个分支a，e，o，u
        o下面有2个分支i，u
        u下面有1个分支a
        一共是10个分支，分别为3个a，2个e，2个i，1个0，2个u。

        当高度为3时，与高度2时的处理类似：

        a下面有1个分支e，此时有3个a因此有3个分支e
        e下面有2个分支a和i，此时有2个e，因此分别有2个分支a和i
        i下面有4个分支a，e，o，u，此时有2个i，因此分别有2个分支a，e，o，u
        o下面有2个分支i和u，此时有1个o，因此有1个分支i和1个分支u
        u下面有1个分支a，此时有2个u，因此有2个分支a
        一共是19个分支。

        上面就是基本的编程思路，首先我们先统计当前层分别有多少个a，e，i，o，u。他们的总和即是当层的结果。
        然后到下一层，分别看他们能出现多少分支，再统计出各个字母的个数，以此类推，直到循环至第n层结束。
        """
        MOD = 10**9 +7
        a = e = i = o = u = 1
        while n > 1:
            countA = (e+i+u)%MOD
            countE = (a+i)%MOD
            countI = (e+o)%MOD
            countO = i%MOD
            countU = (i+o)%MOD
            a, e, i, o, u = countA, countE, countI, countO, countU 
            n -=  1
        return (a+e+i+o+u)%MOD

    def countVowelPermutationDP(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        a: [e, i, u]; // 上层一共有多少e, i和u，本层就会出现多少a
        e: [a, i]; // 上层一共有多少a和i，本层就会出现多少e
        i: [e, o];
        o: [i];
        u: [i, o];
        """
        relation = [[1,2,4],[0,2],[1,3],[2],[2,3]]
        vowels = [1]*5 # When N=1 all vowels are used once to for 1 letter strings
        MOD = 10**9 +7
        while n > 1:
            # count layer by layer
            vowels_cp = vowels[:]
            for i in range(5):
                vowels[i] = 0
                for r in relation[i]:
                    #Add the # of strings that end with characters that can have 'i' after them.
                    vowels[i] = (vowels[i] + vowels_cp[r]) % MOD 
            n -= 1
        return sum(vowels)%MOD    

if __name__ == "__main__":
    print(Solution().countVowelPermutation(100))
    print(Solution().countVowelPermutationDP(100))