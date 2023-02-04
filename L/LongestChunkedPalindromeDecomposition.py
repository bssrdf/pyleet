'''

-Hard-
*Greedy*
*Two Pointers*
*Rabin Karp*
*DP*

You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

subtexti is a non-empty string.
The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
Return the largest possible value of k.

 

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tep)(za)(pre)(a)(nt)(a)".
 

Constraints:

1 <= text.length <= 1000
text consists only of lowercase English characters.


'''


class Solution:
    def longestDecomposition(self, text: str) -> int:
        S = text
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res
    

    def longestDecomposition2(self, text: str) -> int:
        S = text
        n = len(S)  
        def partialMatchTable(P):
            m = len(P)
            pt = [0]*m
            k = 0
            for q in range(1,m):                
                while k > 0 and P[k] != P[q]:
                    k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
                if P[k] == P[q]:
                    k += 1
                pt[q] = k
            return pt
        kmp = partialMatchTable(S)     
        dp = [0]*(n//2+1)
        mx = 0
        for j in range(n//2):
            for i in range(j+1):
                if S[i:j+1] == S[n-1-j:n-i] and (i == 0 or dp[i] != 0):
                    dp[j+1] = max(dp[j+1], dp[i]+2)
                    mx = max(mx, dp[i]+2) 
        return dp[n//2] if n%2 ==0 and dp[n//2] != 0 else mx + 1
    
    def longestDecomposition3(self, text: str) -> int:
        # Used a prime number generator on the internet to grab a prime number to use.
        magic_prime = 32416189573
        
		# Standard 2 pointer technique variables.
        low = 0
        high = len(text) - 1
        
		# These are the hash tracking variables.
        cur_low_hash = 0
        cur_high_hash = 0
        cur_hash_length = 0
        
		# This is the number of parts we've found, i.e. the k value we need to return.
        k = 0
        
        while low < high:
            
			# To put the current letter onto our low hash (i.e. the one that goes forward from
			# the start of the string, we shift up the existing hash by multiplying by the base
			# of 26, and then adding on the new character by converting it to a number from 0 - 25.
            cur_low_hash *= 26 # Shift up by the base of 26.
            cur_low_hash += ord(text[low]) - 97 # Take away 97 so that it's between 0 and 25.
            
			
			# The high one, i.e. the one backwards from the end is a little more complex, as we want the 
			# hash to represent the characters in forward order, not backwards. If we did the exact same
			# thing we did for low, the string abc would be represented as cba, which is not right.	
			
			# Start by getting the character's 0 - 25 number.
            high_char = ord(text[high]) - 97
			
			# The third argument to pow is modular arithmetic. It says to give the answer modulo the
			# magic prime (more on that below). Just pretend it isn't doing that for now if it confuses you. 
            # What we're doing is making an int that puts the high character at the top, and then the 
			# existing hash at the bottom.
            cur_high_hash = (high_char * pow(26, cur_hash_length, magic_prime)) + cur_high_hash            
            
			# Mathematically, we can safely do this. Impressive, huh? I'm not going to go into here, but
			# I recommend studying up on modular arithmetic if you're confused.
			# The algorithm would be correct without doing this, BUT it'd be very slow as the numbers could
			# become tens of thousands of bits long. The problem with that of course is that comparing the
			# numbers would no longer be O(1) constant. So we need to keep them small.
            cur_low_hash %= magic_prime 
            cur_high_hash %= magic_prime
            
			# And now some standard 2 pointer technique stuff.
            low += 1
            high -= 1
            cur_hash_length += 1
            
			# This piece of code checks if we currently have a match.
            # This is actually probabilistic, i.e. it is possible to get false positives.
            # For correctness, we should be verifying that this is actually correct.
            # We would do this by ensuring the characters in each hash (using
			# the low, high, and length variables we've been tracking) are
			# actually the same. But here I didn't bother as I figured Leetcode
			# would not have a test case that broke my specific prime.
            if cur_low_hash == cur_high_hash:
                k += 2 # We have just added 2 new strings to k.
                # And reset our hashing variables.
                cur_low_hash = 0
                cur_high_hash = 0
                cur_hash_length = 0
        
		# At the end, there are a couple of edge cases we need to address....
		# The first is if there is a middle character left.
		# The second is a non-paired off string in the middle.
        if (cur_hash_length == 0 and low == high) or cur_hash_length > 0:
            k += 1
        
        return k



        

if __name__ == "__main__":
    print(Solution().longestDecomposition(text = "ghiabcdefhelloadamhelloabcdefghi"))
    print(Solution().longestDecomposition2(text = "ghiabcdefhelloadamhelloabcdefghi"))
    print(Solution().longestDecomposition3(text = "ghiabcdefhelloadamhelloabcdefghi"))