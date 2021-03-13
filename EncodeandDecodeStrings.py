'''
-Medium-

Design an algorithm to encode a list of strings to a string. The encoded string is then 
sent over the network and is decoded back to the original list of strings.

Please implement encode and decode


Example1

Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
Example2

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"

'''


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ''
        if not strs: return ':;'
        for s in strs:
            enc = ''
            for c in s:
                if c == ':': enc += "::"
                elif c == ';': enc += ";;"
                else: enc += c 
            res += enc + ':;'
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        if len(str) == 2: return ''
        res, start = [], 0
        for i in range(len(str)-1):            
            if str[i:i+2] == ':;':
                dec, j = '', start
                while j < i-1: 
                    if str[j:j+2] == '::': 
                        dec += ':'; j += 2
                    elif str[j:j+2] == ';;': 
                        dec += ';'; j += 2
                    else:
                        dec += str[j]; j += 1
                if j == i-1: dec += str[j]
                res.append(dec)
                start = i+2
        return res   


if __name__ == "__main__":
    s = Solution().encode(["lint","code","love","you"])
    print(s)
    print(Solution().decode(s))
    s = Solution().encode(["we", "say", ":", "yes"])
    print(s)
    print(Solution().decode(s))
