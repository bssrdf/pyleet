

from collections import deque

NIL = 0
INF = float('inf')


class BipGraph(object):

 
    # To add edge from u to v and v to u
    def addEdge(self, u, v):
         
        #Add u to v’s list.
        self.adj[u].append(v)

    def __init__(self, m, n):
      # m and n are number of vertices on left
      # and right sides of Bipartite Graph
        self.m, self.n = m, n
      # adj[u] stores adjacents of left side
      # vertex 'u'. The value of u ranges
      # from 1 to m. 0 is used for dummy vertex
        self.adj = [[] for _ in range(m+1)]
 
      # These are basically pointers to arrays
     # needed for hopcroftKarp()
        # pairU[u] stores pair of u in matching where u
        # is a vertex on left side of Bipartite Graph.
        # If u doesn't have any pair, then pairU[u] is NIL
        self.pairU = [0]*(m+1)
       # pairV[v] stores pair of v in matching. If v
       # doesn't have any pair, then pairU[v] is NIL
        self.pairV = [0]*(n+1) 
       # dist[u] stores distance of left side vertices
       # dist[u] is one more than dist[u'] if u is next
       # to u'in augmenting path
        self.dist  = [0]*(m+1)
 
    # Returns size of maximum matching
    def hopcroftKarp(self):
         
        result = 0
 
        # Keep updating the result while
        # there is an augmenting path.
        k = 0
        while self.bfs():
            print('before dfs', self.dist)
            # Find a free vertex
            for u in range(1, self.m+1):
                # If current vertex is free and there is
                # an augmenting path from current vertex
                if self.pairU[u] == NIL and self.dfs(u):
                    result += 1
            k += 1
            print('After iteration ', k)
            print('PairU : ',self.pairU)
            print('PairV : ', self.pairV)
            print(self.dist)
            print('matchings: ', result)
        return result
 
    # Returns true if there is an augmenting
    # path, else returns false
    def bfs(self):
         
        # An integer queue
        Q = deque()
 
        # First layer of vertices (set distance as 0)
        for u in range(1, self.m+1):
             
            # If this is a free vertex,
            # add it to queue
            if self.pairU[u] == NIL:
                # u is not matched
                self.dist[u] = 0
                Q.append(u)
            # Else set distance as infinite
            # so that this vertex is
            # considered next time
            else:
                self.dist[u] = INF
 
        # Initialize distance to
        # NIL as infinite
        self.dist[NIL] = INF
 
        # Q is going to contain vertices
        # of left side only.
        while Q:
             
            # Dequeue a vertex
            u = Q.popleft()
 
            # If this node is not NIL and
            # can provide a shorter path to NIL
            if self.dist[u] < self.dist[NIL]:
                 
                # Get all adjacent vertices of
                # the dequeued vertex u
                for v in self.adj[u]:
 
                    # If pair of v is not considered
                    # so far (v, pairV[V]) is not yet
                    # explored edge.
                    if self.dist[self.pairV[v]] == INF:
                         
                        # Consider the pair and add
                        # it to queue
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        Q.append(self.pairV[v])
 
        # If we could come back to NIL using
        # alternating path of distinct vertices
        # then there is an augmenting path
        return self.dist[NIL] != INF
 
    # Returns true if there is an augmenting
    # path beginning with free vertex u
    def dfs(self,  u):
        if u != NIL:
            for v in self.adj[u]:
 
                # Follow the distances set by BFS
                if self.dist[self.pairV[v]] == self.dist[u] + 1:
                     
                    # If dfs for pair of v also returns
                    # true
                    if self.dfs(self.pairV[v]):
                        self.pairV[v] = u
                        self.pairU[u] = v
                        return True
 
            # If there is no augmenting path
            # beginning with u.
            self.dist[u] = INF
            return False
        return True
 
    
 
#Driver code
if __name__ == "__main__":
     
    g = BipGraph(5, 5);
    g.addEdge(1, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 1);
    g.addEdge(2, 5);
    g.addEdge(3, 3);
    g.addEdge(3, 4);
    g.addEdge(4, 1);
    g.addEdge(4, 5);
    g.addEdge(5, 2);
    g.addEdge(5, 4);
 
    print("Size of maximum matching is " +
                       str(g.hopcroftKarp()))