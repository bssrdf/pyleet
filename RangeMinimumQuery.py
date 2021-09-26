'''
-Medium-

Design a data structure that takes an array of integers. Write a method that 

finds the position of the element with the minimum value between two given indices.



'''
import math

class RMQ(object):
    # Sparse Table (ST) Algorithm

    # O(NlogN) to construct ST table
    def __init__(self, nums):
        self.N = len(nums)
        self.A = nums
        self.M = [[0]*(int(math.log(self.N,2)+1)) for _ in range(self.N)]
        for i in range(self.N):
            self.M[i][0] = i
        j = 1
        while 1<<j <= self.N: 
            for i in range(self.N-(1<<j)+1):
                if nums[self.M[i][j-1]] <= nums[self.M[i+(1<<(j-1))][j-1]]:
                    self.M[i][j] = self.M[i][j-1]
                else:
                    self.M[i][j] = self.M[i+(1<<(j-1))][j-1]
            j += 1       
       # print(self.M)     

    # O(1) to query the minimum
    def minRange(self, l, r):
        k = int(math.log(r-l+1, 2))
        #print(k)
        return self.M[l][k] if self.A[self.M[l][k]] <= self.A[self.M[r-(1<<k)+1][k]] else self.M[r-(1<<k)+1][k]



if __name__ == "__main__":
    
    A = [2,4,3,1,6,7,8,9,1,7]
    rmq = RMQ(A)    
    print(rmq.minRange(2,7)) # 3
    print(rmq.minRange(0,9)) # 3
    print(rmq.minRange(0,2)) # 0
    print(rmq.minRange(4,7)) # 4    
    A = [1,2,3,2]
    rmq = RMQ(A)
    print(rmq.minRange(2,3)) # 0




