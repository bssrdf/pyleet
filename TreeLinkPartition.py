
from collections import defaultdict

# n=8; edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
n=9; edges = [[2,5],[3,4],[4,1],[1,7],[6,7],[7,0],[0,5],[5,8]]

G = defaultdict(list)

# Build undirected graph
for u,v in edges:
    G[u].append(v)
    G[v].append(u)

f = [-1]*n
d = [-1]*n
size = [0]*n
son = [-1]*n
top = [-1]*n
id = [-1]*n
rk = [-1]*n
cnt = 0
def dfs1(u, fa, depth):
    f[u] = fa
    d[u] = depth
    size[u] = 1
    for v in G[u]:        
        if v == fa: continue
        dfs1(v,u,depth+1)
        size[u] += size[v]
        if size[v] > size[son[u]]:
            son[u] = v

def dfs2(u,  t):
    global cnt
    top[u] = t     
    id[u] = cnt
    rk[cnt] = u
    cnt += 1
    if son[u] < 0:
        return
    dfs2(son[u], t)
    for v in G[u]:
        if v != son[u] and v != f[u]:
            dfs2(v,v)


def lca(u, v):
    while top[u] != top[v]:
        if d[top[u]] > d[top[v]]:
            u = f[top[u]]
        else:
            v = f[top[v]]
    return v if d[u] > d[v] else u     


dfs1(0, -1, 1)
print('fa = ', f)
print('size = ', size)
print('son = ', son)
dfs2(0, 0)
print('id = ', id)
print('rk = ', rk)
print('top = ', top)
print(lca(2, 3))