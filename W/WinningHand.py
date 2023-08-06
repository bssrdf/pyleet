'''





'''


from typing import List
from itertools import combinations_with_replacement
class Solution:
    def winningHand(self, s: str) -> List[str]:
        pairs = [str(i)*2 for i in range(1,10)] 
        straights = [str(i-1)+str(i)+str(i+1) for i in range(2,9)]         
        sets = [str(i)*3 for i in range(1,10)] 
        # print(pairs)
        # print(straights)
        # print(sets)
        allwins = set()
        for com in combinations_with_replacement(straights+sets, 4):
           for p in pairs:
               allwins.add(''.join(sorted(''.join(list(com)+[p]))))

        # print(len(allwins))
        ans = []
        for i in range(1,10):
            if ''.join(sorted(s+str(i))) in allwins:
                ans.append(str(i))          
        return ans




if __name__ == "__main__":
    print(Solution().winningHand(s='1116667788899'))