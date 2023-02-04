'''
-Medium-

Yash is a student at MIT and has to do a lot of work. He has finished k homeworks and 
the deadlines of these homeworks lie between 0 to 𝑘^2 - 1.

Help Yash sort these homeworks in non-decreasing order of deadlines with expected time 
and space complexity O(k).


Input: k = 5, homeworks = [13, 24, 1, 17, 8] 
Output: [1, 8, 13, 17, 24] 

'''

class RadixSort(object):    
    def sort(self, n, arr):
        digitNum = 2
        size = n
        dataCopy = [[i,v] for i,v in enumerate(arr)]
        #print(dataCopy)
        def countingSortDigit():
            digitData =[]
            for i in range(size):
                digitData.append((i, dataCopy[i][1] % size))
                dataCopy[i][1] //= size
            
            countArray = [0]*size
            for digit in digitData:
                countArray[digit[1]] += 1

            for i in range(1,size):
                countArray[i] += countArray[i-1]
            #print(digitData, countArray)
            auxData = dataCopy[:]
            for i in range(size - 1, -1, -1):
                countArray[digitData[i][1]] -= 1
                curIdx = countArray[digitData[i][1]]
                dataCopy[curIdx] = auxData[digitData[i][0]]
           # print(dataCopy)

        for _ in range(1,digitNum+1):
           countingSortDigit()
        auxData = arr[:]
        for i in range(size):
           arr[i] = auxData[dataCopy[i][0]]
        return arr

from random import randint
import time
if __name__ == "__main__":
    print(RadixSort().sort(5, [13, 24, 1, 15, 8]))
    #print(RadixSort().sort(5, [ 100, 24, 70, 99, 8]))
    k = 1000000
    mx = k**2-1
    arr = []
    for i in range(k):
        arr.append(randint(0, mx))
    starttime = time.time()
    RadixSort().sort(k, arr)
    print("elapsed {}s".format(time.time()-starttime))
    starttime = time.time()
    arr.sort()
    print("elapsed {}s".format(time.time()-starttime))
    



