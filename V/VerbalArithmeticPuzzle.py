'''

-Hard-

*Backtracking*


Given an equation, represented by words on the left side and the result on the right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
No two characters can map to the same digit.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on the left side (words) will equal to the number on the right side (result).
Return true if the equation is solvable, otherwise return false.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
Explanation: There is no possible mapping to satisfy the equation, so we return false.
Note that two different characters cannot map to the same digit.
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contain only uppercase English letters.
The number of different characters used in the expression is at most 10.

'''


from typing import List
from functools import lru_cache

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        n = len(words)
        def helper(i, num, used, mp):
            if i == len(result):
                # print('sm = ', sm)
                return checkSum(0, 0, used, "", 0, int(num), mp)
            c = result[i]
            if c in mp:
                return helper(i+1, num+mp[c], used, mp)
            else:
                for k in range(0 if i > 0 else 1, 10):
                    if not used[k]:
                        mp[c] = str(k)
                        used[k] = True
                        ret = helper(i+1, num+str(k), used, mp)
                        if ret: return True
                        mp.pop(c)
                        used[k] = False
            return False

        def checkSum(i, j, used, num, sm, rsum, mp):
            if i == n:
                return sm == rsum
            if j == len(words[i]):
                if sm+int(num) > rsum: return False                
                return checkSum(i+1, 0, used, "", sm+int(num), rsum, mp)
            c = words[i][j]
            if c in mp:
                if checkSum(i, j+1, used, num+mp[c], sm, rsum, mp):
                    return True
            else:
                for k in range(10):
                    if not used[k]:
                        mp[c] = str(k)
                        used[k] = True
                        ret = checkSum(i, j+1, used, num+str(k), sm, rsum, mp)
                        if ret: return True
                        mp.pop(c)
                        used[k] = False
            return False
        u = [False]*10
        return helper(0, "", u, {})

    def isSolvable2(self, words: List[str], result: str) -> bool:
        # TLE because of no early pruning
        words = [result] + words
        n = len(words)
        mp = {}       
        # @lru_cache(None)
        def checkSum(i, j, used, num, sm):           
            if i == n:
                return sm == 0 
            if j == len(words[i]):                
                if i >= 1:        
                    if sm-num < 0: return False      
                    return checkSum(i+1, 0, used, 0, sm-num)
                else:
                    return checkSum(i+1, 0, used, 0, sm+num)    
            c = words[i][j]
            if c in mp:
               if checkSum(i, j+1, used, num*10+mp[c], sm):
                    return True
            else:
                for k in range(0 if j > 0 else 1, 10):
                    if used & (1<<k) == 0:
                        mp[c] = k
                        ret = checkSum(i, j+1, used | (1<<k), num*10+k, sm)
                        if ret: return True
                        mp.pop(c)
            return False
        
        return checkSum(0, 0, 0, 0, 0)
    
    def isSolvable3(self, words: List[str], result: str) -> bool:
        for word in words:
            if len(word) > len(result): # 每個單字的長度都不能長於result的長度
                return False
       
        c2i = [-1]*26 #把每個字母映射到數字 (確保每個字母只會映射到同1個數字) 把所有的26個字母的映射初始成-1，代表我們還沒有為此字母分配過數字
        i2c = [-1]*10 #把每個數字映射到字母 (確保數字不會被重複使用) //把所有10的數字的映射初始成-1,代表我們還沒有分配過此數字給任何字母
        
        w = words  # words的全域變數是w
        r = result # result的全域變數是r
        for i in range(len(words)): #把所有的單字反轉，以便我們能從個位、十位、百位遍歷到最大位數
            w[i] = w[i][::-1]
        
        r = r[::-1] #把結果對應的字串反轉，以便我們能從個位、十位、百位遍歷到最大位數
        
        def dfs(index, l,  s):  
             #遍歷順序是把當前的位數中的所有單字處理完後，才會進展到下一個位數，直到所有位數被處理完為止
            # index代表當前到了words中的哪1個單字 
            # (eg. words[index], index從0~words.length()-1)
            # l代表當前走到了words中單字或result的哪1個位數(因為我們要統計完所有當前位數才能進位) 
            # (eg. words[index][l], result[l], l從0~result.length()-1或是l從0~words[index].length()-1)
            # s是所有單字在當前的位數的總合;s%10是當前位數所有單字合的個位數, s/10就是我們傳遞的進位值
            if l == len(r): #如果已經遍歷完所有的位數，就抵達終止條件
                return s == 0 #我們要確保當前的s進位值已經是0
            
            if index == len(w): # 如果對於所有單字words[0]~words[end]，都已經遍歷完當前位數l，就遍歷下個位數
            
                if c2i[ord(r[l])-ord('A')] != -1: #如果result當中，當前位數對應的字母已經被分配過數字
                    if c2i[ord(r[l])-ord('A')] == s % 10: #確認此字母映射到的數字是否為s的個位數 (s是所有的單字在當前位數的總合)
                        return dfs(0, l+1, s//10) #因為所有單字的當前位數都遍歷完了，所以我們從下個位數的words[0]開始遍歷，並且傳遞進位值(s/10)
                elif i2c[s%10] == -1:  #如果字母還沒映射過，我們要確認我們該使用的數字(s%10)是否還沒被用過
                    if l == len(r)-1 and s % 10 == 0: #最大位數不能為0
                        return False
                    c2i[ord(r[l])-ord('A')] = s % 10  #把所有單字的當前位數的總和之個位數分配給result的當前位數對應的字母
                    i2c[s%10] = ord(r[l])-ord('A')  #確保所有單字當前位數的總和對應的個位數字已經被分配給字母r[l]，避免重複分配
                    temp = dfs(0, l+1, s//10)  #我們先把backtracking的結果存下來，因為此後還要把前面2個操作的結果復原, 而傳遞的index=0代表對於下個位數從words[0]開始遍歷, 把位數l增加1以前進到下個位數,傳遞進位值(s/10)
                    c2i[ord(r[l])-ord('A')] = -1  #把前面的操作復原，這是回溯法backtracking的一部份
                    i2c[s%10] = -1 #把前面的操作復原，這是回溯法backtracking的一部份
                    return temp #回傳結果
                return False #如果沒辦法符合以上的if或else if中的條件，代表此路不通，沒辦法形成正確等式

            if l >= len(w[index]):  #如果當前處理的位數已經大於當前單字的長度，就直接跳過此單字
                return dfs(index+1, l, s) #直接跳過words[index]，從words[index+1]繼續遍歷當前的位數，s不會被改變，因為此單字已經被跳過了

            if c2i[ord(w[index][l])-ord('A')] != -1: #如果此字母已經分配過數字了
                if l != len(w[index])-1 or c2i[ord(w[index][l])-ord('A')] != 0: #避免首位數為0
                    return dfs(index+1, l, s+c2i[ord(w[index][l])-ord('A')]) #把此字母對應的數字加到s，並且從下個單字words[index+1]繼續遍歷
                return False    
            
            for i in range(10): #如果此字母還沒被分配過任何數字

                if i2c[i] != -1: #如果此數字已經被用過，就不能重複使用
                    continue
            
                if i == 0 and len(w[index]) > 1 and l == len(w[index]) - 1: #word[index]的首位數不能是0    
                    continue
                
                i2c[i] = ord(w[index][l])-ord('A') #我們分配數字i給了字母w[index][l]，因此數字i不能再次被使用
                c2i[ord(w[index][l])-ord('A')] = i # 我們把字母w[index][l]映射的值設成數字i，因此該字母不能再被映射成其他數字
                temp = dfs(index+1, l, s+i)  #我們先把backtracking的結果存下來，因為此後還要把前面2個操作的結果復原。並且從下個單字words[index+1]開始遍歷此位數(此位數被遍歷完才會再進位)，並且把s加上此操作所分配的數字
                i2c[i] = -1 #把前面的操作復原，這是回溯法backtracking的一部份
                c2i[ord(w[index][l])-ord('A')] = -1 #把前面的操作復原，這是回溯法backtracking的一部份(讓我們能開始嘗試下一種可能)
                if temp: #如果任何一種單字分配的方式能形成正確等式，就回傳true
                    return True
            return False #如果所有的數字分配都嘗試過也不能成功，就回傳false


        return dfs(0, 0, 0)  # 我們從words[0]的最小位數(個位數)開始遍歷，個位數的總和初始為0
        

   


if __name__ == "__main__":
    # print(Solution().isSolvable(words = ["SEND","MORE"], result = "MONEY"))
    # print(Solution().isSolvable(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
    # print(Solution().isSolvable(words = ["LEET","CODE"], result = "POINT"))
    # print(Solution().isSolvable2(words = ["SEND","MORE"], result = "MONEY"))
    # print(Solution().isSolvable2(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
    # print(Solution().isSolvable2(words = ["LEET","CODE"], result = "POINT"))
    print(Solution().isSolvable3(words = ["SEND","MORE"], result = "MONEY"))
    print(Solution().isSolvable3(words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"))
    print(Solution().isSolvable3(words = ["LEET","CODE"], result = "POINT"))
    print(Solution().isSolvable3(words = ["A","B"], result = "A"))