'''


'''
from collections import defaultdict
from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        m = defaultdict(int)
        res = []
        for name in names:
            print(name, m)
            if name in m:  
                newname = name+'({})'.format(m[name])
                m[name] += 1
                while newname in m:
                    newname = name+'({})'.format(m[name])
                    m[name] += 1
                m[newname] = 1    
                res.append(newname)                
            else:
                m[name] = 1
                res.append(name)
        return res

if __name__ == "__main__":
    print(Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)","kaido(2)"]))