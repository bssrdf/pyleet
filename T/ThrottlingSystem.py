
'''

-Easy-

%Amazon%



'''

class Solution:
    def droppedRequests(self, requestTime):

        dropped = 0

        # you can include reqTime in enumerate for print purpose - debugging ( i.e., for i, reqTime in enumerate(requestTime) )
        for i, _  in enumerate(requestTime):
            if i > 2 and requestTime[i] == requestTime[i-3]:
                dropped += 1

            elif i > 19 and requestTime[i] - requestTime[i-20] < 10:
                dropped += 1

            elif i > 59 and requestTime[i] - requestTime[i-60] < 60:
                dropped += 1
        
        return dropped

if __name__ == "__main__":
    reqs = [1,1,1,1,2]
    print(Solution().droppedRequests(reqs))
    reqs = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
    print(Solution().droppedRequests(reqs))
    reqs = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]
    print(Solution().droppedRequests(reqs))