'''

-Easy-

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
 

Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.



'''

class Solution:
    def isLongPressedNameWrong(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            print('Z', i, j, name[i], typed[j])
            if name[i] == typed[j]:
                i += 1; j += 1; continue
            if i == 0 or name[i] == name[i-1]:
                j += 1; continue
            print('A', i, j, name[i], typed[j])
            k = j
            while k < len(typed) and typed[k] == typed[j-1]:
                k += 1
            print('B', i, j, k, name[i], typed[j], typed[k])    
            j = k     
            if j > len(typed)-1: break   
            print('C', i, j, k, name[i], typed[j], typed[k])        
            if name[i] != typed[j]:
                j += 1
        while j < len(typed):
            if typed[j] == typed[j-1]:
                j += 1
            else: break

        print('final', i, j)    
        return i == len(name) and j == len(typed)

    def isLongPressedName(self, name: str, typed: str) -> bool:
        s, t = [], []
        cnt, ch = 1, name[0]
        for c in name[1:]:
            if c == ch: cnt += 1
            else:                
                s.append((c,cnt))
                cnt = 1; ch = c 
        s.append((ch, cnt))
        cnt, ch = 1, typed[0]
        for c in typed[1:]:
            if c == ch: cnt += 1
            else:                
                t.append((c,cnt))
                cnt = 1; ch = c 
        t.append((ch, cnt))
        if len(s) != len(t): return False 
        for p, q in zip(s, t):
            if p[0] != q[0] or p[1] > q[1]: 
                return False
        return True

        

if __name__ == "__main__": 
    print(Solution().isLongPressedName(name = "alex", typed = "aaleex"))
    print(Solution().isLongPressedName(name = "saeed", typed = "ssaaedd"))
    print(Solution().isLongPressedName(name = "leelee", typed = "lleeelee"))
    print(Solution().isLongPressedName("xnhtq", "xhhttqq"))
    print(Solution().isLongPressedName("alex","aaleexa"))
    print(Solution().isLongPressedName("vtkgn","vttkgnn"))
    print(Solution().isLongPressedName("alex","aaleelx"))