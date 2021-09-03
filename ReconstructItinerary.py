'''
-Medium-

*DFS*
*Hierholzer’s algorithm*
*Euler Path*

Given a list of airline tickets represented by pairs of departure and arrival 
airports [from, to], reconstruct the itinerary in order. All of the tickets 
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that 
has the smallest lexical order when read as a single string. For example, the 
itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only onc8`e.
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
import heapq

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

    def findItineraryPQ(self, tickets):
        '''
        :type tickets: List[List[str]]
        :rtype: List[str]

        This is to find an Eulerian path in a directed graph. Thus, start 
        from “JFK”, we can apply the Hierholzer’s algorithm to find a Eulerian 
        path in the graph which is a valid reconstruction.

        Hierholzer’s algorithm is as follows:

        Choose any starting vertex v, and follow a trail of edges from that 
        vertex until returning to v. It is not possible to get stuck at any 
        vertex other than v, because the even degree of all vertices ensures 
        that, when the trail enters another vertex w there must be an unused 
        edge leaving w. The tour formed in this way is a closed tour, but 
        may not cover all the vertices and edges of the initial graph.

        As long as there exists a vertex u that belongs to the current tour 
        but that has adjacent edges not part of the tour, start another trail 
        from u, following unused edges until returning to u, and join the tour 
        formed in this way to the previous tour.

        By using a data structure such as a doubly linked list to maintain 
        the set of unused edges incident to each vertex, to maintain the 
        list of vertices on the current tour that have unused edges, and to 
        maintain the tour itself, the individual operations of the algorithm 
        (finding unused edges exiting each vertex, finding a new starting 
        vertex for a tour, and connecting two tours that share a vertex) may 
        be performed in constant time each, so the overall algorithm takes 
        linear time, O(E).

        First, we go DFS from JFK until we get stuck. Then, we construct 
        path backwards. When walking backwards through the DFS path, if a 
        node has outgoing path, then perform DFS there, which is guaranteed 
        to return to the starting node, forming a cycle. Then the cycle 
        is merged into the main DFS path.        

        '''
        targets = collections.defaultdict(list)
        for a, b in tickets:            
            heapq.heappush(targets[a], b)       
        route = deque()
        def visit(airport):            
            while targets[airport]:
                # When we perform DFS, we choose the outgoing edge 
                # with the lowest lexical order, as guranteed by the pq
                visit(heapq.heappop(targets[airport]))
            route.appendleft(airport)         
        visit('JFK')
        return list(route)

    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:            
            targets[a].append(b)       
        route = []
        def visit(airport):            
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)         
        visit('JFK')
        return route[::-1]

    def findItineraryPQ2(self, tickets):
        # Write your code here
        graph = collections.defaultdict(list)
        for s,t in tickets:
            heapq.heappush(graph[s], t)
        #res = deque()
        res = []
        def dfs(city):            
            while graph[city]:
                dst = heapq.heappop((graph[city]))
                dfs(dst)
            #res.appendleft(city)
            res.append(city)
        dfs('JFK')
        return res[::-1]                    

if __name__=="__main__":

    #tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #tickets = [("JFK","SFO"),("JFK","ATL"),("SFO","ATL"),("ATL","JFK"),("ATL","SFO")]
    #tickets=[("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    
    #print(Solution().ReconIter(tickets))
    print(Solution().findItinerary(tickets))
    print(Solution().findItineraryPQ(tickets))

    tickets= [["JFK","KUL"],["JFK","NRT"], ["NRT","JFK"]]
    print(Solution().findItineraryPQ2(tickets))

