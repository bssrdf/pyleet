'''
-Hard-
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of 
lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the 
sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length 
turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may 
make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully 
contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most 
letter being stamped at each turn.  If the sequence is not possible to stamp, return an 
empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return 
the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp 
within 10 * target.length moves.  Any answers specifying more than this number of moves 
will not be accepted.

 

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
 

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.

'''
import collections

class Solution(object):

    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        res = []
        n, total = len(stamp), 0
        while True:
            isStamped = False
            for size in range(n, 0, -1):
                for i in range(n - size + 1):
                    t = '*'*i + stamp[i:i+size]+'*'*(n - size - i)   
                    print(size, i, t, target,isStamped)                  
                    pos = target.find(t)
                    while pos != -1:
                        res.append(pos)
                        isStamped = True
                        total += size
                        target = target[:pos]+'*'*n+target[pos+n:]  
                        pos = target.find(t)
            if not isStamped: break
        return res[::-1] if total == len(target) else []

    def movesToStampDP(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        """
        Try to find a path of target,
        where path[i] equals to index of target[i] in stamp

        Example 1:
        Input: stamp = "abc", target = "ababc"
        path = [0,1,0,1,2]

        Example 2:
        Input: stamp = "abca", target = "aabcaca"
        path = [0,0,1,2,3,2,3]

        The rule is that,
        rule 0. path[i + 1] can equal to path[i] + 1
        It means target[i] and target[i+1] are on the same stamp.

        rule 1. path[i + 1] can equal to 0.
        It means t[i + 1] is the start of another stamp

        rule 2. if path[i] == stamp.size - 1, we reach the end of a stamp.
        Under this stamp, it's another stamp, but not necessary the start.
        path[i + 1] can equal to 0 ~ stamp.size - 1.

        Step 2:
        We need to change path to required moves.
        This can be a medium problem on the Leetcode.

        """
        s, t = stamp, target
        if s[0] != t[0] or s[-1] != t[-1]: return []
        n, m = len(s), len(t)
        path = [0] * m
        pos = collections.defaultdict(set)
        for i, c in enumerate(s): pos[c].add(i)

        def dfs(i, index):
            path[i] = index
            if i == m - 1: return index == n - 1
            nxt_index = set()
            if index == n - 1:  # rule 2
                nxt_index |= pos[t[i + 1]]
            elif s[index + 1] == t[i + 1]:  # rule 0
                nxt_index.add(index + 1)
            if s[0] == t[i + 1]:  # rule 1
                nxt_index.add(0)
            return any(dfs(i + 1, j) for j in nxt_index)

        def path2res(path):
            down, up = [], []
            for i in range(len(path)):
                if path[i] == 0:
                    up.append(i)
                elif i and path[i] - 1 != path[i - 1]:
                    down.append(i - path[i])
            return down[::-1] + up

        if not dfs(0, 0): return []
        return path2res(path)

    def movesToStampMemoization(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        '''
        1. stamp[0] has to be equal with target[0]
        2. stamp[-1] has to be equal with target[-1]
        3. We keep checking pairs of (stamp[s], target[t]). When checking (s, t). 
        If stamp[s] equals to target[t], we can either move forward to (s+1, t+1), 
        or we add a new stamp at index t+1 and stamp[0] has to be equal with target[t+1]. 
        Then we move forward to (0, t+1). (If stamp[0] != target[t+1] here, there is no 
        way to stamp without overwriting previous stamped sequence).
        4. When a stamp is used up, s == len(stamp), and we can try any i that 
        stamp[i] == target[t]. In such case, we stamp at index t-i at the begining of the 
        sequence so that stamp[:i] will be overwritten by "later" stamps and we move forward 
        to (i, t).
        5. We finish our search when we reach the end of target or t == len(target). 
        Based on rule #2, if i == len(stamp) as well, we have a valid sequence.

        '''
        memo, ls, lt = {}, len(stamp), len(target)
        def dfs(s, t, seqs):
            if t == lt:
                memo[s, t] = seqs if s == ls else []
            if (s, t) not in memo:
                if s == ls:
                    for i in range(ls):
                        cand = dfs(i, t, [t-i]+seqs)
                        if cand:
                            print('a,',s,t,i,cand)
                            memo[s, t] = cand
                            break
                    else: 
                        memo[s, t] = []
                elif target[t] == stamp[s]:
                    cand = dfs(s+1, t+1, seqs)
                    #print('b,',s,t,cand)
                    memo[s, t] = cand if cand else dfs(0, t+1, seqs+[t+1])
                else:
                    memo[s, t] = []
            return memo[s, t]
        return dfs(0, 0, [0])


if __name__ == "__main__":
    #print(Solution().movesToStampDP(stamp = "abca", target = "aabcaca"))
    print(Solution().movesToStamp(stamp = "abca", target = "aabcaca"))
    #print(Solution().movesToStampMemoization(stamp = "abca", target = "aabcaca"))