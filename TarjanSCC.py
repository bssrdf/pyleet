'''

Tarjan缩点

首先什么是强连通分量呢？

有向图强连通分量：在有向图G中，如果两个顶点vi,vj间（vi>vj）有一条从vi到vj的有向路径，同时还有一条
从vj到vi的有向路径，则称两个顶点强连通(strongly connected)。如果有向图G的每两个顶点都强连通，称G是
一个强连通图。有向图的极大强连通子图，称为强连通分量(strongly connected components)。


那我们可以在强连通分量上做什么算法呢？——缩点，将一个强连通分量变成一个点

为啥我们可以将一个强连通分量变成一个点?因为强连通分量中的点是可以互相到达的，在某些情况下，这些点是等价的

为啥我们要把他们缩成一个点因为缩完点后的图没有环，是一张有向无环图，这种图有很多性质，能解决一些题目

引入dfn数组存储时间戳，low存储这个点可以到达的点的最早时间戳，栈st存储点的情况，用于统计哪些点是
在环上的，vis用于当前这一轮找点的情况。

得到一个点x，首先先入栈，然后将点的dfn和low均初始化为时间戳tt，然后开始查看与这个点相连的点，假设
是to，如果这个点还没被访问过，也就是时间戳还是0，那么继续深搜，然后更新这个点的low值，
也就是low[x]=min(low[x],low[to])；如果时间戳不是0，那么就看vis看是不是访问过，然后还是
执行上面句子，为什么是这样呢，因为第一种是没有访问过，那么这个点的low值你是不知道的，所以无法更新，而
访问过的可以直接得到值。在更新完所有与这个点连接的点之后就得到了这个点最终的low值。

在一轮更新之后，此时有着相同low值的就构成了一个强联通图，其中任意两点都可以互相达到。为什么？因为
我们在更新时遇到访问过的点会停止搜索，那么遇到访问过的那么这个点的时间戳一定早于我走来到达这个点的
这一条环(深搜是一条边走到黑)任意一点的时间戳，在回溯进行low[x]=min(low[to],low[x])的操作之后，
这一条环上的所有low值都被置为了访问到的那个点的，一条环一定是强连通图，因为更新的过程中有许多
交叉，其实都会被置为最小的那个，所以最终一个low相同的图可能由多个环组成，环组成的还是强连通图。

因为相同low值的是一个强连通图，而这个low值其实就是这个连通图最早被搜索到的值，我们就可以把
这个点，也就是low[x]=dfn[x]的点作为这个强连通图的代表点，把这个连通图缩到这个点，至于如何找
到这个代表点所代表的的块的所有节点就利用栈，一直弹到这个代表点出栈为止(因为这个点的low最小，所以最早进入栈)。


Application: Codeforce 1000 E. We Need More Bosses


time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Description:

Your friend is developing a computer game. He has already decided how the game world should 
look like — it should consist of n locations connected by m two-way passages. The passages 
are designed in such a way that it should be possible to get from any location to any other location.

Of course, some passages should be guarded by the monsters (if you just can go everywhere without 
any difficulties, then it's not fun, right?). Some crucial passages will be guarded by really 
fearsome monsters, requiring the hero to prepare for battle and designing his own tactics of 
defeating them (commonly these kinds of monsters are called bosses). And your friend wants 
you to help him place these bosses.

The game will start in location s and end in location t, but these locations are not 
chosen yet. After choosing these locations, your friend will place a boss in each passage 
such that it is impossible to get from s to t without using this passage. Your friend 
wants to place as much bosses as possible (because more challenges means more fun, right?), 
so he asks you to help him determine the maximum possible number of bosses, considering 
that any location can be chosen as s or as t.

Input
The first line contains two integers n and m (2≤n≤3⋅10^5, n−1≤m≤3⋅10^5) — the number of 
locations and passages, respectively.

Then m lines follow, each containing two integers x and y (0≤x,y≤n-1, x≠y) describing the 
endpoints of one of the passages.

It is guaranteed that there is no pair of locations directly connected by two or more passages, 
and that any location is reachable from any other location.

Output
Print one integer — the maximum number of bosses your friend can place, considering all 
possible choices for ss and tt


'''


from collections import defaultdict

from random import randint, choice



# n = 5; edges = [[0,1], [1,2], [2,0], [0,3], [1,4]]
# n = 5; edges = [[0,1], [1,2], [2,0], [0,3], [1,4], [2,4]]
# n = 4; edges = [[0,1], [2,3], [1,2]]

n, m = 200, 2
edges = []


nodes = {randint(0, n-1)}
for i in range(n):    
    if i not in nodes:
        st = set()
        L = list(nodes)
        for k in range(randint(1, m)):
            j = choice(L)
            if j not in st and i != j :
                st.add(j)
                edges.append([i,j])
        nodes.add(i)
     
print(n, edges)
# n =20; edges = [[0, 2], [1, 2], [3, 2], [4, 1], [5, 1], [5, 4], [6, 2], [7, 0], [8, 0], [9, 6], [10, 4], [11, 9], [12, 7], [12, 4], [13, 12], [14, 
# 7], [15, 9], [15, 11], [16, 0], [17, 15], [18, 10], [18, 15], [19, 13]]
# n=100; edges = [[0, 83], [1, 83], [2, 83], [3, 0], [3, 2], [4, 0], [4, 2], [5, 83], [6, 1], [6, 3], [7, 6], [8, 3], [9, 2], [9, 6], [10, 2], [11, 4], [12, 11], [13, 9], [13, 1], [14, 0], [14, 1], [15, 5], [15, 10], [16, 14], [17, 7], [17, 16], [18, 7], [18, 2], [19, 16], [20, 19], [20, 6], [21, 20], [21, 19], [22, 15], [23, 10], [24, 10], [24, 23], [25, 9], [26, 15], [27, 26], [27, 21], [28, 26], [28, 17], [29, 23], [30, 11], [31, 27], [32, 1], [32, 83], [33, 32], [33, 23], [34, 83], [35, 5], [35, 16], [36, 10], [37, 7], [38, 13], [38, 9], [39, 7], [39, 3], [40, 29], [40, 19], [41, 26], [41, 11], [42, 26], [43, 40], [44, 33], [45, 41], [45, 32], [46, 39], [47, 10], [48, 40], [49, 39], [50, 36], [51, 27], [51, 30], [52, 29], [52, 46], [53, 0], [53, 12], [54, 34], [55, 44], [55, 39], [56, 26], [57, 30], [58, 13], [59, 50], [59, 27], [60, 10], [61, 25], [62, 51], [62, 37], [63, 1], [64, 18], [64, 11], [65, 55], [66, 58], [67, 58], [68, 51], [68, 33], [69, 48], [70, 7], [70, 36], [71, 13], [71, 24], [72, 34], [73, 44], [73, 31], [74, 1], [74, 24], [75, 65], [76, 71], [77, 45], [78, 29], [79, 78], [80, 12], [81, 28], [81, 51], [82, 20], [84, 12], [85, 82], [86, 37], [87, 2], [87, 19], [88, 39], [89, 75], [90, 80], [90, 73], [91, 16], [91, 20], [92, 83], [92, 30], [93, 89], [94, 58], [95, 56], [96, 0], [97, 12], [98, 54], [98, 91], [99, 38]]
print(n, len(edges))
for u,v in edges:
    print(u+1, v+1)

G = defaultdict(list)

# Build undirected graph
for u,v in edges:
    G[u].append(v)
    G[v].append(u)


dfn = [0]*n # 代表编号为 i 的点的DFS序序号
low = [0]*n # 代表编号为 i 的点所在的强连通分量中所有点中的最小dfn值
# vis = [0]*n
bl  = [-1]*n # 缩点之后重新给点编号
stack = [] # 栈，代表所有已经遍历到的但是还没有遍历完所有的边的节点
tt = 0 # time stamp
scc_cnt = -1 # 强连通分量编号 
sz = [] # 每个强连通分量的点的数量
def tarjan(u, fa):
    # nonlocal tt
    # nonlocal scc_cnt
    global tt, scc_cnt
    tt += 1
    low[u] = dfn[u] = tt
    # vis[u] = 1
    stack.append(u)
    for v in G[u]:
        if v == fa: continue
        if dfn[v] == 0:
            tarjan(v, u)
            low[u] = min(low[u], low[v])
        # elif vis[v]:
        else:
            low[u] = min(low[u], dfn[v])
        
      
    if low[u] == dfn[u]:
        scc_cnt += 1
        sz.append(0)
        while True:
            sz[scc_cnt] += 1
            k = stack.pop()
            bl[k] = scc_cnt
            if k == u: break

NG = defaultdict(list) 
dist = [0]*n
# DFS to find maximum distance 
def dfs(u, fa):
    if fa == -1:
        dist[u] = 1
    else:
        dist[u] = dist[fa] + 1
    for v in NG[u]:
        if v != fa:
            dfs(v, u)

tarjan(0, -1)
# print(dfn)
# print(low)

# print(scc_cnt)
# print(sz)
# print(bl)

# rebuild new graph formed by SCC of the original graph
for u in range(n):
    for v in G[u]:
        if bl[u] != bl[v]: # if u and v belong to different SCCs, connect them in new graph
            NG[bl[u]].append(bl[v])

# print(NG)
dfs(0, -1)
S = 0
# print(dist)
for i in range(scc_cnt+1):
    if dist[i] > dist[S]:
        S = i
# print(S)
dfs(S, -1)
# print(dist)
ans = 0
for i in range(scc_cnt+1):
    ans = max(ans, dist[i]-1)
print('ans = ', ans)
    
    



