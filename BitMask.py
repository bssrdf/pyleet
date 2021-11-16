'''

Test of subset performance of bitmask vs Python's set


'''
import random
import time
from collections import defaultdict
maxLen = 20
n = 10000

if __name__ == "__main__":    
    list1 = []
    for i in range(n):
       list1.append(''.join(chr(random.randint(0, 25)+ord('a')) for _ in range(maxLen)))  
    print(list1[:10])
    list2 = random.choices(list1, k=5000)
    list3 = random.choices(list1, k=6000)
    
    #list2 = random.choices(list3, k=5000)
    starttime = time.time()
    print(set(list2) <= set(list3))
    endtime = time.time()
    print('Elapsed ', endtime-starttime)

    #starttime = time.time()
    m = defaultdict(int)
    idx = 1    
    for c in list2:
        if c in m: continue
        m[c] = idx
        idx += 1
    for c in list3:
        if c in m: continue
        m[c] = idx
        idx += 1    
    starttime = time.time()
    bit1 = 0
    for c in list2:
        bit1 |= 1 << m[c]
    bit2 = 0
    for c in list3:
        bit2 |= 1 << m[c]
    
    print(bit1 & bit2 == bit1)
    endtime = time.time()
    print('Elapsed ', endtime-starttime)




