

from collections import deque

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use('TkAgg')


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
            print('before dfs, dist = ', self.dist)
            print('before dfs, pairU = ', self.pairU)
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
            print('after dfs, dist = ',self.dist)
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
            else: # if this vertex has been matched, set dist to INF
                self.dist[u] = INF
 
        # Initialize distance to
        # NIL as infinite
        self.dist[NIL] = INF

        print("size of Q: ", len(Q))
 
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
                    # we require in our BFS that when going from V to U, 
                    # we always select a matched edge. 
                    if self.dist[self.pairV[v]] == INF:
                         
                        # Consider the pair and add
                        # it to queue
                        #if self.pairV[v] == NIL: 
                         #   print('u,v', u, v, self.dist[u])
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        Q.append(self.pairV[v])
 
        # If we could come back to NIL using
        # alternating path of distinct vertices
        # then there is an augmenting path
        # If no path has been found, then there are no augmenting paths left 
        # and the matching is maximal. bfs returns false to terminate the while loop
        return self.dist[NIL] != INF
 
    # Returns true if there is an augmenting
    # path beginning with free vertex u
    def dfs(self,  u):
        if u != NIL:
            for v in self.adj[u]:
 
                # Follow the distances set by BFS
                # Note that the code ensures that all augmenting paths 
                # that we consider are vertex disjoint. Indeed, after 
                # doing the symmetric difference for a path, none of its 
                # vertices could be considered again in the DFS, just because 
                # the Dist[Pair_V[v]] will not be equal to Dist[u] + 1 (it would be exactly Dist[u]).
                if self.dist[self.pairV[v]] == self.dist[u] + 1:
                     
                    # If dfs for pair of v also returns
                    # true
                    print(u, v, self.pairV[v], self.dist[self.pairV[v]], self.dist[u] )
                    if self.dfs(self.pairV[v]):
                        self.pairV[v] = u
                        self.pairU[u] = v
                        return True
 
            # If there is no augmenting path
            # beginning with u.
            # When we were not able to find any shortest augmenting path from a vertex u, 
            # then the DFS marks vertex u by setting Dist[u] to infinity, so that these 
            # vertices are not visited again.
            self.dist[u] = INF
            return False
        return True
 
    
 
#Driver code
if __name__ == "__main__":
    # the graph is from the link below
    # https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm#/media/File:HopcroftKarpExample.png 
    g = BipGraph(5, 5);

    edges = [(1,1), (1,2), (2,1), (3,3), (2,5), (4,1), (5,2), (5,4)]
    '''
    g.addEdge(1, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 1);
    g.addEdge(2, 5);
    g.addEdge(3, 3);
    #g.addEdge(3, 4);
    g.addEdge(4, 1);
    #g.addEdge(4, 5);
    g.addEdge(5, 2);
    g.addEdge(5, 4);
    '''
    for e in edges:
        g.addEdge(*e)
    
    print("Size of maximum matching is " +
                       str(g.hopcroftKarp()))
    B = nx.Graph()
    B.add_nodes_from(list(range(1,6)), bipartite=0, label='left')
    B.add_nodes_from(list('ABCDE'), bipartite=1, label='right')
    edges = [(1,'A'), (1,'B'), (2,'A'), (3,'C'), (2, 'E'), (4,'A'), (5,'B'), (5,'D')]
    #B.add_edges_from(edges, label='connect')
    for e in edges:
        if ord(e[1])-ord('A')+1 == g.pairU[e[0]]: 
            B.add_edge(e[0],e[1],color='r')
        else:
            B.add_edge(e[0],e[1],color='g')



    # Now instead of spring_layout, use bipartite_layout

    # First specify the nodes you want on left or top
    left_or_top = list(range(1,6))

    # Then create a bipartite layout
    pos = nx.bipartite_layout(B, left_or_top)
    colors = nx.get_edge_attributes(B,'color').values()
    # Pass that layout to nx.draw
    nx.draw(B,pos,node_color='#A0CBE2',edge_color=colors,width=2,
        edge_cmap=plt.cm.Blues,with_labels=True)
    plt.show()
   
