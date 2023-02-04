'''

-Medium-
*Hash Table*
*BFS*


You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of the ith node. The root of the tree is node 0, so parent[0] = -1 since it has no parent. You want to design a data structure that allows users to lock, unlock, and upgrade nodes in the tree.

The data structure should support the following functions:

Lock: Locks the given node for the given user and prevents other users from locking the same node. You may only lock a node using this function if the node is unlocked.
Unlock: Unlocks the given node for the given user. You may only unlock a node using this function if it is currently locked by the same user.
Upgrade: Locks the given node for the given user and unlocks all of its descendants regardless of who locked it. You may only upgrade a node if all 3 conditions are true:
The node is unlocked,
It has at least one locked descendant (by any user), and
It does not have any locked ancestors.
Implement the LockingTree class:

LockingTree(int[] parent) initializes the data structure with the parent array.
lock(int num, int user) returns true if it is possible for the user with id user to lock the node num, or false otherwise. If it is possible, the node num will become locked by the user with id user.
unlock(int num, int user) returns true if it is possible for the user with id user to unlock the node num, or false otherwise. If it is possible, the node num will become unlocked.
upgrade(int num, int user) returns true if it is possible for the user with id user to upgrade the node num, or false otherwise. If it is possible, the node num will be upgraded.
 

Example 1:


Input
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
Output
[null, true, false, true, true, true, false]

Explanation
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // return true because node 2 is unlocked.
                           // Node 2 will now be locked by user 2.
lockingTree.unlock(2, 3);  // return false because user 3 cannot unlock a node locked by user 2.
lockingTree.unlock(2, 2);  // return true because node 2 was previously locked by user 2.
                           // Node 2 will now be unlocked.
lockingTree.lock(4, 5);    // return true because node 4 is unlocked.
                           // Node 4 will now be locked by user 5.
lockingTree.upgrade(0, 1); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                           // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
lockingTree.lock(0, 1);    // return false because node 0 is already locked.
 

Constraints:

n == parent.length
2 <= n <= 2000
0 <= parent[i] <= n - 1 for i != 0
parent[0] == -1
0 <= num <= n - 1
1 <= user <= 104
parent represents a valid tree.
At most 2000 calls in total will be made to lock, unlock, and upgrade.




'''

from typing import List
from collections import defaultdict, deque

class LockingTree2:

    def __init__(self, parent: List[int]):
        self.n = len(parent)
        self.tree = defaultdict(list)
        for v, u in enumerate(parent):
            if u != -1:
                self.tree[u].append(v)
        self.locks = [0]*self.n         
        

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0:
            self.locks[num] = user
            print("user {} locked {}".format(user, num))
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = 0
            print("user {} unlocked {}".format(user, num))
            return True
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        def dfs(node, lockanc):
            locks = []
            if self.locks[node] > 0:
                lockanc += 1
            for child in self.tree[node]:
                res, clocks = dfs(child, lockanc)    
                locks += clocks
                if res: return True, locks
            if node == num and self.locks[num] == 0 and lockanc == 0 and len(locks) > 0:
                self.locks[num] = user
                for l in locks:
                    self.locks[l] = 0
                return True, locks    
            return False, locks + ([node] if self.locks[node] > 0 else [])
            
        if self.locks[num] != 0: return False 
        dfs(0, 0)
        if self.locks[num] == user: 
            # print("user {} upgraded {}".format(user, num))
            return True
        return False

class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = {}      
        self.par = parent  
        self.tree = defaultdict(list)
        for v, u in enumerate(parent):
            if u != -1:
                self.tree[u].append(v)
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locks:
            return False
        self.locks[num] = user    
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num] == user:
            self.locks.pop(num)            
            return True
        return False
        

    def upgrade(self, num: int, user: int) -> bool:

        anc = num
        while anc >= 0:
            if anc in self.locks:
                return False
            anc = self.par[anc]
        upgradable = False
        que = deque([num])
        while que:
            u = que.popleft()
            if u in self.locks:
                upgradable = True
                self.locks.pop(u)
            for v in self.tree[u]:
                que.append(v)
        if upgradable:
            self.locks[num] = user
        return upgradable    






if __name__ == "__main__":
    false, true = False, True
    #'''   
    lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    print(lockingTree.lock(2, 2))#    // return true because node 2 is unlocked.
                            # Node 2 will now be locked by user 2.
    print(lockingTree.unlock(2, 3))#  // return false because user 3 cannot unlock a node locked by user 2.
    print(lockingTree.unlock(2, 2))#  // return true because node 2 was previously locked by user 2.
                            # Node 2 will now be unlocked.
    print(lockingTree.lock(4, 5))#    // return true because node 4 is unlocked.
                            # Node 4 will now be locked by user 5.
    print(lockingTree.upgrade(0, 1))# // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                            # Node 0 will now be locked by user 1 and node 4 will now be unlocked.
    print(lockingTree.lock(0, 1))#    // return false because node 0 is already locked.
    #'''
    ins= ["upgrade","upgrade","upgrade","upgrade","unlock","unlock","upgrade","upgrade","upgrade","lock","lock","upgrade","upgrade","unlock","upgrade","upgrade","upgrade","upgrade","unlock","unlock"]
    lockingTree = LockingTree([-1,6,5,5,7,0,7,0,0,6])
    paras =[[5,3],[2,3],[7,39],[1,32],[5,44],[2,15],[1,11],[1,18],[3,7],[5,36],[5,42],[8,5],[1,19],[3,38],[0,27],[4,11],[9,2],[8,41],[5,36],[7,29]]
       
    ans = [false,false,false,false,false,false,false,false,false,true,false,false,false,false,true,false,false,false,false,false] 
    for i,p,a in zip(ins, paras, ans):
        sol = False
        if i == "upgrade":
            sol = lockingTree.upgrade(*tuple(p))
            # print("user {} upgrades {} result {}".format(p[1], p[0], sol))
        elif i == "unlock":
            sol = lockingTree.unlock(*tuple(p))
            # print("user {} unlock {} result {}".format(p[1], p[0], sol))
        else:
            sol = lockingTree.lock(*tuple(p))
            # print("user {} lock {} result {}".format(p[1], p[0], sol))
        if sol != a:
            print(sol, a, i, p)
    lockingTree = LockingTree([-1,4,1,2,8,0,8,0,0,7])
    ins = ["lock","unlock","upgrade","upgrade","unlock","upgrade","upgrade","upgrade","lock","upgrade","upgrade","unlock","upgrade","unlock","unlock","unlock","upgrade","lock","lock","lock"]
    paras = [[8,48],[8,48],[4,47],[8,16],[4,23],[7,39],[6,39],[9,33],[5,32],[8,8],[6,5],[6,42],[5,19],[3,45],[7,45],[1,25],[0,15],[5,42],[5,16],[4,25]]
    ans = [true,true,false,false,false,false,false,false,true,false,false,false,false,false,false,false,true,true,false,true]

    for i,p,a in zip(ins, paras, ans):
        sol = False
        if i == "upgrade":
            sol = lockingTree.upgrade(*tuple(p))
            print("user {} upgrades {} result {}".format(p[1], p[0], sol))
        elif i == "unlock":
            sol = lockingTree.unlock(*tuple(p))
            print("user {} unlock {} result {}".format(p[1], p[0], sol))
        else:
            sol = lockingTree.lock(*tuple(p))
            print("user {} lock {} result {}".format(p[1], p[0], sol))
        if sol != a:
            print(sol, a, i, p)

