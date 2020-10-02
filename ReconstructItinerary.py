'''
Given a list of airline tickets represented by pairs of departure and arrival 
airports [from, to], reconstruct the itinerary in order. All of the tickets 
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that 
has the smallest lexical order when read as a single string. For example, the 
itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.


'''


#import graph
import collections
from collections import deque

class Solution(object):
    def ReconIter(self, tickets): 
        '''
        The solution to this problem demonstrate a pattern for getting an Eulerian
        path in a directed graph with cycles. The Eulerian path would walk over 
        every edge exactly once.
        '''      
        
        graph = collections.defaultdict(list)
        for ticket in tickets:            
            graph[ticket[0]].append(ticket[1])
        # **very important: convert adjacent list to a queue (deque in python)
        for start in graph:            
            graph[start] = deque(sorted(graph[start]))
        
        # dfs function returns True if success;
        # the meaning of success depends on the problem;
        # here success is achieved when the length of the path = maxLen
        def dfs(root, path, maxLen):            
            # return True immediately if success
            if len(path) == maxLen:
                return True         
            for k in range(len(graph[root])):
                # remove and return one neighbor from front
                end = graph[root].popleft()             
                # add the neighbor to the path
                path.append(end)
                # ***IMPORTANT***
                # do dfs on that neighbor; if dfs return true,
                # we immediately return true as well; this way the path
                # will contain the final answer.
                if dfs(end, path, maxLen):
                    return True
                # if we get here, that means the neighbor dfs is not 
                # successful, we backtrack after doing two things that
                # are exactly the opposite to opertions prior to dfs
                # 1) remove neighbor from the path 
                path.pop()
                # 2) add that neighbor to the back of the queue
                graph[root].append(end)

        path = ["JFK"]
        dfs("JFK", path, len(tickets) + 1)
        return path    
       
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            #targets[a] += b,
            targets[a].append(b)
       # for t in targets:
       #     print t, targets[t]
        route = []
        def visit(airport):            
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
         #   print route
        visit('JFK')
        return route[::-1]       
            

if __name__=="__main__":

    #tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    #tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #tickets = [("JFK","SFO"),("JFK","ATL"),("SFO","ATL"),("ATL","JFK"),("ATL","SFO")]
    #tickets=[("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    tickets= [["JFK","KUL"],["JFK","NRT"], ["NRT","JFK"]]
    print(Solution().ReconIter(tickets))
    #print(Solution().findItinerary(tickets))
