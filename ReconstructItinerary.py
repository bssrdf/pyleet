
#import graph
import collections

class Solution(object):
    def ReconIter(self, tickets):
        #G=graph.Graph(tickets, directed=True)
        from collections import deque
        graph = {}
        for ticket in tickets:
            graph[ticket[0]] = graph.get(ticket[0], []) + [ticket[1]]
        for start in graph:
            graph[start] = deque(sorted(graph[start]))
            
        def dfs(root, graph, path, maxLen):
            if len(path) == maxLen:
                return True
            for k in xrange(len(graph.get(root, []))):
                end = graph[root].popleft()
                path.append(end)
                if dfs(end, graph, path, maxLen):
                    return True
                path.pop()
                graph[root].append(end)

        path = ["JFK"]
        dfs("JFK", graph, path, len(tickets) + 1)
        return path    
        #for g in graph:
         #   print g, graph[g]
#        print G
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            #targets[a] += b,
            targets[a].append(b)
        for t in targets:
            print t, targets[t]
        route = []
        def visit(airport):            
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            print route
        visit('JFK')
        return route[::-1]       
            

if __name__=="__main__":

    #tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    #tickets = [("JFK","SFO"),("JFK","ATL"),("SFO","ATL"),("ATL","JFK"),("ATL","SFO")]
    #tickets=[("MUC", "LHR"), ("JFK", "MUC"), ("SFO", "SJC"), ("LHR", "SFO")]
    #print Solution().ReconIter(tickets)
    print Solution().findItinerary(tickets)
